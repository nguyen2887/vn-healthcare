-- Phân hệ bệnh án ngoại trú của "ClinicOne" (SaaS cho chuỗi phòng khám tư, có khám BHYT)
-- Hosting: AWS ap-southeast-1 (Singapore), backup S3 cùng region.

CREATE TABLE patients (
  id            BIGSERIAL PRIMARY KEY,
  cccd          VARCHAR(12) UNIQUE,          -- dùng làm khóa định danh, cho phép NULL
  full_name     TEXT NOT NULL,
  dob           DATE,
  phone         VARCHAR(15),
  hiv_status    TEXT,                        -- 'positive' | 'negative' | NULL, ai có quyền xem hồ sơ đều thấy
  created_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE encounters (
  id            BIGSERIAL PRIMARY KEY,
  patient_id    BIGINT REFERENCES patients(id),
  doctor_id     BIGINT,
  icd10_main    VARCHAR(10),                 -- nhập tự do, không kiểm tra danh mục
  diagnosis_txt TEXT,
  notes         TEXT,
  signed        BOOLEAN DEFAULT false,
  signature_img TEXT,                        -- URL ảnh chữ ký bác sĩ chèn vào phiếu in
  updated_at    TIMESTAMPTZ DEFAULT now()    -- sửa trực tiếp (UPDATE), kể cả sau khi signed = true
);

CREATE TABLE prescriptions (
  id            BIGSERIAL PRIMARY KEY,
  encounter_id  BIGINT REFERENCES encounters(id),
  code          VARCHAR(20),                 -- 'DT' || lpad(id::text, 10, '0')  (tăng dần)
  items         JSONB,
  sent_national BOOLEAN DEFAULT false,       -- gửi lên hệ thống đơn thuốc quốc gia bằng job cuối ngày
  created_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE audit_logs (
  id         BIGSERIAL PRIMARY KEY,
  user_id    BIGINT,                         -- tài khoản 'letan' dùng chung cho cả quầy
  action     TEXT,
  entity     TEXT,
  entity_id  BIGINT,
  created_at TIMESTAMPTZ DEFAULT now()
);
-- Cron: DELETE FROM audit_logs WHERE created_at < now() - interval '90 days';
-- Cron: DELETE FROM encounters WHERE updated_at < now() - interval '5 years';
