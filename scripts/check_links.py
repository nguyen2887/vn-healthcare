#!/usr/bin/env python3
"""Kiểm tra mọi link trong các file markdown: có mở được không, có bị đẩy về
trang chủ không, và (nếu biết) trang có chứa số hiệu văn bản được dẫn không.

Dùng:
    python3 scripts/check_links.py research/*.md            # in báo cáo
    python3 scripts/check_links.py --json out.json skill/**/*.md

Số hiệu văn bản được đoán từ chính dòng chứa link; so khớp theo "số/năm" (vd "13/2025")
hoặc "số/loại" (vd "17/CT"), đã chuẩn hóa Đ/Ð/D và chữ Kirin giống Latin.
Với PDF chỉ kiểm tra status + content-type, không đọc nội dung.
URL nằm trong `code` (địa chỉ hệ thống, API) được bỏ qua — chúng không phải link nguồn.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

CODE_SPAN_RE = re.compile(r"`[^`]*`")
URL_RE = re.compile(r"https?://[^\s\]>\"'`|]+")


def trim_url(raw: str) -> str:
    """Bỏ dấu câu cuối và ")" thừa của cú pháp markdown, giữ "(1)" trong tên file."""
    url = raw.rstrip(".,;:")
    while url.endswith(")") and url.count(")") > url.count("("):
        url = url[:-1].rstrip(".,;:")
    return url
# Khóa so khớp: "332/2026" (số/năm) hoặc "17/CT" , "2439/QD" (số/loại, không năm).
DOC_KEY_RE = re.compile(r"\b(\d{1,5})/(\d{4}|[A-Za-zĐÐđ]{2,4})(?=[/\-;,\s)]|$)")
# Chữ Kirin hay bị gõ lẫn vào số hiệu trên trang chính phủ (vd "NĐ-CР").
LOOKALIKE = str.maketrans({"Đ": "D", "Ð": "D", "đ": "d", "Р": "P", "С": "C", "А": "A", "Т": "T",
                           "О": "O", "Н": "H", "В": "B", "Е": "E", "К": "K", "М": "M", "Х": "X"})


def doc_keys(text: str) -> set[str]:
    return {f"{n}/{t}".translate(LOOKALIKE).upper() for n, t in DOC_KEY_RE.findall(text)}
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
TIMEOUT = 25


def extract(paths: list[Path]) -> dict[str, dict]:
    links: dict[str, dict] = {}
    for p in paths:
        for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            docs = doc_keys(line)
            # Địa chỉ hệ thống/API viết trong `code` không phải link nguồn → bỏ qua.
            for raw in URL_RE.findall(CODE_SPAN_RE.sub("", line)):
                url = trim_url(raw)
                e = links.setdefault(url, {"refs": [], "docs": set()})
                e["refs"].append(f"{p}:{lineno}")
                e["docs"].update(docs)
    return links


def check(url: str, docs: set[str]) -> dict:
    """Fetch bằng curl (dùng kho chứng chỉ hệ thống như trình duyệt; urllib
    hay fail chuỗi chứng chỉ của các trang .gov.vn)."""
    out = {"url": url, "status": None, "final_url": None, "verdict": "", "doc_match": None}
    with tempfile.NamedTemporaryFile() as tmp:
        try:
            r = subprocess.run(
                ["curl", "-sL", "-m", str(TIMEOUT), "-A", UA, "-H", "Accept-Language: vi,en",
                 "--max-filesize", "30000000", "-o", tmp.name,
                 "-w", "%{http_code}\t%{url_effective}\t%{content_type}", url],
                capture_output=True, text=True, timeout=TIMEOUT + 5,
            )
        except subprocess.TimeoutExpired:
            out["verdict"] = "LỖI: timeout"
            return out
        if r.returncode != 0:
            out["verdict"] = f"LỖI: curl exit {r.returncode}"
            return out
        code, final, ctype = (r.stdout.split("\t") + ["", ""])[:3]
        out["status"], out["final_url"] = int(code or 0), final
        body = b"" if "pdf" in ctype else Path(tmp.name).read_bytes()[:3_000_000]

    if out["status"] >= 400 or out["status"] == 0:
        out["verdict"] = f"HTTP {out['status']}"
        return out
    src, dst = urlparse(url), urlparse(final)
    if dst.path in ("", "/") and not dst.query and (src.path not in ("", "/") or src.query):
        out["verdict"] = "BỊ ĐẨY VỀ TRANG CHỦ"
        return out
    if body and docs:
        found = doc_keys(html.unescape(body.decode("utf-8", "ignore")).translate(LOOKALIKE).upper())
        out["doc_match"] = bool(docs & found)
        if not out["doc_match"]:
            out["verdict"] = "MỞ ĐƯỢC NHƯNG KHÔNG THẤY SỐ HIỆU"
            return out
    out["verdict"] = "OK"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json")
    a = ap.parse_args()
    links = extract([Path(f) for f in a.files])
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(lambda kv: {**check(kv[0], kv[1]["docs"]), "refs": kv[1]["refs"],
                                           "docs": sorted(kv[1]["docs"])}, links.items()))
    bad = [r for r in results if r["verdict"] != "OK"]
    for r in sorted(bad, key=lambda r: r["verdict"]):
        print(f"[{r['verdict']}] {r['url']}\n    dẫn ở: {', '.join(r['refs'][:3])}")
    print(f"\nTổng {len(results)} link — OK {len(results) - len(bad)}, có vấn đề {len(bad)}")
    if a.json:
        Path(a.json).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
