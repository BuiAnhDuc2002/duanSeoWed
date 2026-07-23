"use client";

import { FormEvent, useCallback, useEffect, useState } from "react";

const API = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";
const identityHeaders = {
  "X-User-Id": "00000000-0000-0000-0000-000000000001",
  "X-Organization-Id": "10000000-0000-0000-0000-000000000001",
};

type Clinic = {
  id: string;
  legal_name: string;
  brand_name: string;
  address: string;
  verification_status: string;
};

export default function Home() {
  const [clinics, setClinics] = useState<Clinic[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const loadClinics = useCallback(async () => {
    setLoading(true);
    try {
      const response = await fetch(`${API}/api/v1/clinics`, { headers: identityHeaders });
      if (!response.ok) throw new Error("Không thể tải danh sách cơ sở.");
      setClinics(await response.json());
      setError("");
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Đã có lỗi xảy ra.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => void loadClinics(), [loadClinics]);

  async function createClinic(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    const response = await fetch(`${API}/api/v1/clinics`, {
      method: "POST",
      headers: { ...identityHeaders, "Content-Type": "application/json" },
      body: JSON.stringify({
        legal_name: form.get("legal_name"),
        brand_name: form.get("brand_name"),
        address: form.get("address"),
      }),
    });
    if (!response.ok) {
      setError("Không thể tạo cơ sở. Hãy kiểm tra dữ liệu và quyền truy cập.");
      return;
    }
    event.currentTarget.reset();
    await loadClinics();
  }

  return (
    <main>
      <header>
        <div>
          <p className="eyebrow">FOUNDATION / CLINIC OPERATIONS</p>
          <h1>AI SEO Clinic</h1>
          <p className="lede">Nền tảng nội dung thẩm mỹ có truy vết, kiểm duyệt và kiểm soát rủi ro.</p>
        </div>
        <span className="status">Development identity</span>
      </header>

      <section className="grid">
        <article className="panel">
          <p className="kicker">Tạo cơ sở</p>
          <h2>Hồ sơ pháp lý bắt đầu từ đây</h2>
          <form onSubmit={createClinic}>
            <label>Tên pháp lý<input name="legal_name" required minLength={2} /></label>
            <label>Tên thương hiệu<input name="brand_name" required minLength={2} /></label>
            <label>Địa chỉ<textarea name="address" required minLength={3} /></label>
            <button type="submit">Tạo hồ sơ cơ sở</button>
          </form>
        </article>

        <article className="panel">
          <div className="sectionTitle">
            <div><p className="kicker">Cơ sở hiện có</p><h2>{clinics.length} hồ sơ</h2></div>
            <button className="secondary" onClick={loadClinics}>Làm mới</button>
          </div>
          {error && <p className="error" role="alert">{error}</p>}
          {loading ? <p className="muted">Đang tải…</p> : clinics.length === 0 ? (
            <div className="empty"><strong>Chưa có cơ sở</strong><p>Tạo hồ sơ đầu tiên để thêm giấy phép và dịch vụ.</p></div>
          ) : (
            <div className="clinicList">{clinics.map((clinic) => (
              <div className="clinic" key={clinic.id}>
                <div><strong>{clinic.brand_name}</strong><p>{clinic.legal_name}</p><small>{clinic.address}</small></div>
                <span>{clinic.verification_status}</span>
              </div>
            ))}</div>
          )}
        </article>
      </section>
    </main>
  );
}

