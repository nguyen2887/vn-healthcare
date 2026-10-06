#!/usr/bin/env python3
"""Kiểm tra ID trong các file domain của skill:
- ID được định nghĩa (tiêu đề `### <CODE>-Rnn`, `### <CODE>-Pnn`, dòng bảng `| <CODE>-Ann |`) có trùng không.
- Mọi ID được dẫn chiếu (vd "xem DLCN-R22", "CLS-R17–R21") có tồn tại không.

Dùng:
    python3 scripts/check_ids.py            # chạy từ thư mục skill
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "references" / "domains"
CODES = ["BHYT-DATA", "BHYT-GD", "HTTT-BC", "MA-LT", "TC-MS", "BAOMAT-CB", "CHUYENKHOA",
         "EMR", "DUOC", "DLCN", "ANM", "SKDT", "GIAYTO", "CLS", "TELE"]
CODE_RE = "|".join(sorted(map(re.escape, CODES), key=len, reverse=True))
DEF_HEAD = re.compile(rf"^#{{2,4}}\s+\**({CODE_RE})-([RP])(\d{{2}})\b", re.M)
DEF_ROW = re.compile(rf"^\|\s*\**({CODE_RE})-(A)(\d{{2}})\b(?!\s*…)", re.M)
# Tham chiếu đơn hoặc dải: EMR-R10, CLS-R17–R21, HTTT-BC-R32-R35
REF = re.compile(rf"\b({CODE_RE})-([RPA])(\d{{2}})(?:\s*[–-]\s*(?:[RPA])?(\d{{2}}))?\b")


def main() -> int:
    defined: Counter[str] = Counter()
    files = sorted(DOMAINS.glob("*.md"))
    for f in files:
        text = f.read_text(encoding="utf-8")
        for code, kind, num in DEF_HEAD.findall(text) + DEF_ROW.findall(text):
            defined[f"{code}-{kind}{num}"] += 1

    problems = 0
    for ident, n in sorted(defined.items()):
        if n > 1:
            print(f"[TRÙNG] {ident} được định nghĩa {n} lần")
            problems += 1

    searched = files + [ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md"))
    for f in searched:
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for code, kind, start, end in REF.findall(line):
                lo = int(start)
                hi = int(end) if end else lo
                for k in range(lo, min(hi, lo + 60) + 1):
                    ident = f"{code}-{kind}{k:02d}"
                    if ident not in defined:
                        print(f"[KHÔNG TỒN TẠI] {ident} — {f.relative_to(ROOT)}:{lineno}")
                        problems += 1

    per_code = Counter(i.rsplit("-", 1)[0] for i in defined if "-R" in i)
    print("\nSố yêu cầu (R) theo domain:", ", ".join(f"{c} {per_code[c]}" for c in CODES))
    print(f"Tổng ID định nghĩa: {len(defined)} · vấn đề: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
