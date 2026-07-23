# ĐẶC TẢ MVP — NỀN TẢNG AI SEO CHO PHÒNG KHÁM PHẪU THUẬT TẠO HÌNH & THẨM MỸ

> Tài liệu triển khai dành cho Codex và đội phát triển  
> Phiên bản: `1.0`  
> Trạng thái: `Implementation-ready draft`  
> Thị trường ban đầu: Việt Nam  
> Kênh xuất bản MVP: WordPress  
> Ngôn ngữ nội dung MVP: Tiếng Việt

---

## 1. Mục đích tài liệu

Tài liệu này mô tả yêu cầu sản phẩm và kỹ thuật cho một ứng dụng web hỗ trợ phòng khám phẫu thuật tạo hình và thẩm mỹ:

1. Thu thập và phân tích từ khóa SEO.
2. Phân nhóm từ khóa theo dịch vụ và ý định tìm kiếm.
3. Lập kế hoạch nội dung.
4. Tạo brief và bản nháp bài viết bằng AI từ nguồn đã kiểm soát.
5. Phát hiện nhận định y khoa cần nguồn hoặc cần bác sĩ duyệt.
6. Chọn ảnh theo dịch vụ, quyền sử dụng và trạng thái đồng ý của khách hàng.
7. Kiểm tra SEO, chất lượng, y khoa và tuân thủ trước khi đăng.
8. Đẩy bài lên WordPress ở trạng thái bản nháp.
9. Theo dõi hiệu suất và đề xuất cập nhật nội dung.
10. Lưu đầy đủ phiên bản, lịch sử duyệt và nhật ký thao tác.

Tài liệu được thiết kế để có thể đưa trực tiếp cho Codex làm đầu vào triển khai repository.

---

## 2. Tầm nhìn và định vị

### 2.1 Tầm nhìn

Trở thành nền tảng vận hành nội dung SEO chuyên ngành thẩm mỹ có khả năng kết hợp:

- Dữ liệu tìm kiếm.
- Kiến thức nội bộ của phòng khám.
- Nguồn y khoa đã duyệt.
- Quy trình kiểm duyệt của bác sĩ.
- Quản lý ảnh và sự đồng ý sử dụng.
- Quy tắc tuân thủ có phiên bản.
- Dữ liệu hiệu suất sau xuất bản.

### 2.2 Định vị

Sản phẩm không phải là công cụ tạo hàng loạt bài viết rồi tự động xuất bản. Sản phẩm là:

> Nền tảng AI SEO có kiểm duyệt y khoa, quản trị tuân thủ và quản lý quyền sử dụng hình ảnh dành cho phòng khám phẫu thuật tạo hình và thẩm mỹ.

### 2.3 Giá trị khác biệt

- **Evidence Engine:** theo dõi nguồn của các nhận định y khoa.
- **Compliance Engine:** kiểm tra nội dung quảng cáo và phạm vi chuyên môn.
- **Image Consent Ledger:** kiểm soát quyền sử dụng ảnh, phạm vi và thời hạn đồng ý.
- **Approval Workflow:** bác sĩ và marketing duyệt theo vai trò.
- **SEO Feedback Loop:** dùng dữ liệu thực tế để đề xuất tối ưu và cập nhật.

---

## 3. Mục tiêu sản phẩm

### 3.1 Mục tiêu MVP

- Kết nối được ít nhất một website WordPress cho mỗi tổ chức.
- Quản lý hồ sơ pháp lý và danh mục dịch vụ của phòng khám.
- Nhập hoặc lấy dữ liệu từ khóa, sau đó phân nhóm và chấm điểm ưu tiên.
- Lập kế hoạch nội dung tránh trùng chủ đề và keyword cannibalization.
- Tạo brief và bài nháp có cấu trúc, metadata SEO và đề xuất liên kết nội bộ.
- Gắn nguồn cho nhận định y khoa và đánh dấu nội dung cần duyệt.
- Quản lý ảnh theo nguồn, bản quyền, consent và phạm vi sử dụng.
- Chặn luồng xuất bản khi chưa vượt qua các kiểm tra bắt buộc.
- Tạo bài nháp hoàn chỉnh trên WordPress.
- Lưu lịch sử phiên bản, duyệt, xuất bản và lỗi tích hợp.

### 3.2 Chỉ số thành công ban đầu

- Thời gian từ keyword được duyệt đến WordPress draft giảm ít nhất 60% so với quy trình thủ công.
- 100% bài có nhận định y khoa rủi ro cao phải được bác sĩ duyệt.
- 100% ảnh trước–sau phải có bản ghi consent hợp lệ trước khi được gắn vào bài.
- 100% thao tác duyệt và xuất bản có audit log.
- Không có bài nào được tự xuất bản trong phạm vi MVP.
- Ít nhất 90% publishing job thành công ở lần đầu sau khi cấu hình WordPress hợp lệ.
- Không có secret hoặc thông tin xác thực được ghi vào log ứng dụng.

### 3.3 Ngoài mục tiêu

- Không thay thế bác sĩ, luật sư hoặc chuyên gia pháp chế.
- Không chẩn đoán hoặc tư vấn cá nhân hóa cho bệnh nhân.
- Không tạo ảnh trước–sau giả hoặc sửa ảnh làm sai lệch kết quả điều trị.
- Không cam kết thứ hạng Google.
- Không tự scrape Google Search ở quy mô lớn.
- Không tự động xuất bản bài trong MVP.

---

## 4. Phạm vi MVP

### 4.1 Trong phạm vi

- Multi-tenant theo tổ chức/phòng khám.
- Đăng nhập, phân quyền và audit log.
- Hồ sơ phòng khám, giấy phép, bác sĩ, dịch vụ và website.
- Knowledge Base chứa tài liệu nội bộ và nguồn y khoa đã duyệt.
- Nhập từ khóa qua CSV và tích hợp nhà cung cấp dữ liệu khi có khóa API.
- Tích hợp Google Search Console.
- Tùy chọn tích hợp Google Ads Keyword Planning.
- Keyword clustering, intent classification và priority scoring.
- Content planner và lịch nội dung.
- AI brief, AI draft và structured output.
- Medical claims review.
- Compliance rules có phiên bản.
- Image library và consent ledger.
- Automated QA.
- Quy trình duyệt bác sĩ và marketing.
- WordPress draft publishing.
- Đồng bộ chỉ số SEO cơ bản.
- Hàng đợi cho tác vụ dài và cơ chế retry.

### 4.2 Ngoài phạm vi MVP

- CMS ngoài WordPress.
- Quản lý quảng cáo trả phí.
- Social media publishing.
- Mobile app native.
- Billing/subscription tự động.
- Scraper SERP tự vận hành.
- Auto-publish không cần người duyệt.
- Hồ sơ bệnh án điện tử.
- Nhận diện hoặc chẩn đoán từ ảnh bệnh nhân.
- Tạo nội dung đa ngôn ngữ.

### 4.3 Phạm vi dịch vụ pilot

Nên giới hạn 4–6 dịch vụ, ví dụ:

- Nâng mũi.
- Cắt mí.
- Nâng ngực.
- Hút mỡ.
- Căng da.
- Tạo hình thành bụng.

Danh mục phải cấu hình được, không hard-code trong logic nghiệp vụ.

---

## 5. Giả định và nguyên tắc

1. WordPress hỗ trợ REST API và tài khoản tích hợp có quyền tối thiểu cần thiết.
2. Dữ liệu từ khóa có thể đến từ CSV, Search Console, Google Ads hoặc nhà cung cấp SERP.
3. Mọi nguồn y khoa dùng để tạo nội dung phải có trạng thái phê duyệt.
4. AI chỉ tạo bản nháp; con người chịu trách nhiệm phê duyệt.
5. Quy tắc pháp lý thay đổi theo thời gian và phải được version hóa.
6. Tất cả thông tin giấy phép, bác sĩ, giá, số ca và cam kết của cơ sở phải lấy từ dữ liệu đã xác minh, không để AI tự suy diễn.
7. Dữ liệu cá nhân và ảnh nhạy cảm được thu thập ở mức tối thiểu.
8. MVP ưu tiên modular monolith để giảm độ phức tạp vận hành.

---

## 6. Người dùng và phân quyền

### 6.1 Vai trò

| Vai trò | Mục đích | Quyền chính |
|---|---|---|
| `ORG_ADMIN` | Quản trị tổ chức | Quản lý người dùng, phòng khám, website, cấu hình, tích hợp |
| `SEO_MANAGER` | Lập kế hoạch SEO | Quản lý keyword, cluster, kế hoạch, brief, SEO QA |
| `CONTENT_EDITOR` | Biên tập nội dung | Tạo/sửa bài, metadata, internal link, ảnh minh họa |
| `MEDICAL_REVIEWER` | Bác sĩ/người duyệt chuyên môn | Duyệt/reject claim và toàn bài về chuyên môn |
| `COMPLIANCE_REVIEWER` | Pháp chế/tuân thủ | Duyệt cảnh báo pháp lý, license và consent |
| `PUBLISHER` | Quản lý xuất bản | Kết nối WordPress, tạo draft, lên lịch nội bộ |
| `VIEWER` | Chỉ xem | Xem dữ liệu và báo cáo được cấp quyền |
| `SYSTEM_WORKER` | Tác vụ hệ thống | Chỉ dùng cho job nội bộ, không đăng nhập UI |

Một người có thể có nhiều vai trò trong một tổ chức.

### 6.2 Ma trận quyền tối thiểu

| Hành động | Admin | SEO | Editor | Medical | Compliance | Publisher |
|---|---:|---:|---:|---:|---:|---:|
| Sửa hồ sơ cơ sở | ✓ |  |  |  | ✓ |  |
| Xác minh giấy phép | ✓ |  |  |  | ✓ |  |
| Quản lý keyword | ✓ | ✓ |  |  |  |  |
| Tạo/sửa bài | ✓ | ✓ | ✓ |  |  |  |
| Duyệt claim y khoa | ✓* |  |  | ✓ |  |  |
| Duyệt compliance | ✓* |  |  |  | ✓ |  |
| Duyệt marketing | ✓ | ✓ | ✓ |  |  |  |
| Gửi WordPress draft | ✓ |  |  |  |  | ✓ |
| Quản lý user/role | ✓ |  |  |  |  |  |

`✓*`: chỉ khi admin đồng thời được gán năng lực chuyên môn tương ứng. Không mặc định cho mọi admin.

### 6.3 Yêu cầu RBAC

- Mọi truy vấn nghiệp vụ phải bị giới hạn theo `organization_id`.
- Backend là nguồn quyết định quyền; không dựa vào việc ẩn nút ở frontend.
- Mọi hành động nhạy cảm phải ghi audit log.
- Từ chối truy cập theo nguyên tắc mặc định (`deny by default`).

---

## 7. Luồng nghiệp vụ tổng thể

```text
Tạo tổ chức và phòng khám
  → Xác minh hồ sơ, giấy phép, dịch vụ, bác sĩ
  → Kết nối WordPress và nguồn dữ liệu SEO
  → Nhập/quét từ khóa
  → Phân loại intent, cluster, chấm điểm
  → Duyệt keyword và tạo content plan
  → Tạo brief từ Knowledge Base đã duyệt
  → Sinh bản nháp có structured output
  → Trích xuất medical claims và nguồn
  → Chọn ảnh có quyền sử dụng phù hợp
  → Automated QA: y khoa + compliance + SEO + chất lượng
  → Medical review
  → Compliance review nếu có cảnh báo
  → Marketing review
  → Approved
  → Tạo WordPress draft
  → Con người kiểm tra/xuất bản trong WordPress
  → Đồng bộ hiệu suất
  → Đề xuất cập nhật
```

### 7.1 Happy path

1. SEO Manager chọn keyword đã được cluster.
2. Hệ thống tạo brief dựa trên intent, trang đang có và nguồn đã duyệt.
3. Editor tạo bản nháp AI.
4. Hệ thống trích claims, gắn citations và chạy QA.
5. Editor xử lý lỗi chặn.
6. Medical Reviewer duyệt claims.
7. Compliance Reviewer xử lý cảnh báo nếu có.
8. Marketing Reviewer duyệt bài.
9. Publisher gửi bài sang WordPress dưới dạng `draft`.
10. Hệ thống lưu `wp_post_id`, URL preview và phiên bản đã gửi.

### 7.2 Luồng sửa lại

- Reviewer có thể `REQUEST_CHANGES` kèm nhận xét bắt buộc.
- Bài quay về `DRAFT_GENERATED` hoặc `AUTOMATED_QA` tùy loại thay đổi.
- Mọi lần sửa tạo `article_version` mới.
- Approval cũ hết hiệu lực khi nội dung đã duyệt thay đổi đáng kể.

---

## 8. Trạng thái và chuyển trạng thái

### 8.1 Trạng thái bài viết

```text
IDEA
→ KEYWORD_APPROVED
→ BRIEF_CREATED
→ DRAFT_GENERATED
→ AUTOMATED_QA
→ MEDICAL_REVIEW
→ COMPLIANCE_REVIEW (khi cần)
→ MARKETING_REVIEW
→ APPROVED
→ WP_DRAFT
→ SCHEDULED
→ PUBLISHED
→ MONITORING
→ UPDATE_REQUIRED
```

Trạng thái phụ:

- `CHANGES_REQUESTED`
- `REJECTED`
- `ARCHIVED`
- `PUBLISH_FAILED`

### 8.2 Guard conditions

| Chuyển trạng thái | Điều kiện bắt buộc |
|---|---|
| `IDEA → KEYWORD_APPROVED` | Keyword có intent, cluster và không bị từ chối |
| `KEYWORD_APPROVED → BRIEF_CREATED` | Có dịch vụ mục tiêu và nguồn KB phù hợp |
| `DRAFT_GENERATED → AUTOMATED_QA` | Structured output hợp lệ |
| `AUTOMATED_QA → MEDICAL_REVIEW` | Không còn lỗi hệ thống; lỗi blocking đã xử lý |
| `MEDICAL_REVIEW → COMPLIANCE_REVIEW` | Medical approval hợp lệ |
| `MEDICAL_REVIEW → MARKETING_REVIEW` | Medical approval hợp lệ và không cần compliance review riêng |
| `COMPLIANCE_REVIEW → MARKETING_REVIEW` | Compliance approval hợp lệ |
| `MARKETING_REVIEW → APPROVED` | Tất cả review bắt buộc đã duyệt; consent và SEO gate hợp lệ |
| `APPROVED → WP_DRAFT` | WordPress connection hợp lệ; snapshot nội dung không đổi |
| `WP_DRAFT → PUBLISHED` | Nhận xác nhận từ WordPress hoặc đồng bộ trạng thái |
| `MONITORING → UPDATE_REQUIRED` | Thỏa rule suy giảm/CTR thấp/nội dung hết hạn |

### 8.3 Quy tắc invalidation

Nếu thay đổi một trong các trường sau sau khi duyệt, phải vô hiệu hóa approval liên quan:

- Nội dung chính.
- Medical claim.
- Nguồn tham khảo.
- Dịch vụ hoặc phạm vi chuyên môn.
- Ảnh trước–sau.
- CTA, giá hoặc cam kết.
- Thông tin giấy phép.

---

## 9. Yêu cầu chức năng

### FR-01 — Tổ chức và phòng khám

- Tạo/sửa tổ chức và nhiều cơ sở trực thuộc.
- Lưu tên pháp lý, tên thương hiệu, địa chỉ, liên hệ, giờ hoạt động.
- Lưu bác sĩ chịu trách nhiệm chuyên môn.
- Lưu tài liệu xác minh và ngày xác minh gần nhất.
- Hiển thị cảnh báo khi giấy phép/tài liệu sắp hết hạn hoặc chưa xác minh.

### FR-02 — Giấy phép và phạm vi chuyên môn

- Lưu số giấy phép, cơ quan cấp, ngày hiệu lực, ngày hết hạn nếu có.
- Lưu danh sách phạm vi chuyên môn đã phê duyệt.
- Ánh xạ dịch vụ marketing sang phạm vi chuyên môn.
- Chặn bài dịch vụ nếu không có ánh xạ hợp lệ hoặc trạng thái xác minh không đạt.
- Không cho AI tự tạo dữ liệu giấy phép.

### FR-03 — Quản lý dịch vụ

- CRUD dịch vụ, tên thay thế, mô tả, nhóm dịch vụ.
- Gắn bác sĩ, cơ sở, phạm vi chuyên môn và tài liệu KB.
- Khai báo mức rủi ro nội dung: `LOW`, `MEDIUM`, `HIGH`.
- Cấu hình disclaimer, CTA và từ ngữ không được dùng theo dịch vụ.

### FR-04 — Website và tích hợp

- Mỗi tổ chức có thể cấu hình một hoặc nhiều WordPress site.
- Kiểm tra kết nối, quyền và REST endpoint.
- Mã hóa thông tin xác thực.
- Đồng bộ category, tag, author và bài hiện có.
- Cho phép bật/tắt từng nguồn SEO.

### FR-05 — Keyword ingestion

- Nhập CSV với mapping cột.
- Nhận keyword từ Search Console.
- Nhận keyword ideas/metrics từ provider khi đã cấu hình.
- Chuẩn hóa chữ hoa/thường, dấu cách và bản ghi trùng.
- Lưu nguồn, locale, thiết bị, khoảng thời gian và thời điểm thu thập.

### FR-06 — Keyword classification

- Phân loại intent:
  - `INFORMATIONAL`
  - `COMPARISON`
  - `RISK`
  - `COST`
  - `PROCEDURE`
  - `RECOVERY`
  - `SERVICE`
  - `LOCAL_PROVIDER`
  - `AFTERCARE`
  - `CONTRAINDICATION`
- Gán dịch vụ và giai đoạn funnel.
- Cho phép người dùng sửa kết quả AI.
- Lưu model/prompt/version tạo phân loại.

### FR-07 — Clustering và priority score

- Cluster theo semantic similarity và SERP overlap khi có dữ liệu.
- Cho phép merge/split cluster thủ công.
- Phát hiện keyword cannibalization dựa trên keyword mục tiêu, semantic similarity và trang hiện có.
- Công thức mặc định:

```text
priority_score =
  0.30 × service_relevance
  + 0.20 × lead_potential
  + 0.20 × search_demand
  + 0.15 × inverse_difficulty
  + 0.10 × site_strength
  + 0.05 × freshness_need
```

- Mọi thành phần chuẩn hóa về thang `0..100`.
- Trọng số phải cấu hình được theo tổ chức.

### FR-08 — Content planner

- Tạo pillar page, supporting articles và topic cluster.
- Chọn primary/secondary keyword.
- Hiển thị bài hiện có cạnh tranh cùng chủ đề.
- Đề xuất thứ tự ưu tiên và ngày dự kiến.
- Gán owner, reviewer, service và website.

### FR-09 — Knowledge Base

- Upload hoặc nhập:
  - Quy trình của cơ sở.
  - Hướng dẫn trước/sau phẫu thuật.
  - Hồ sơ bác sĩ đã xác minh.
  - Bảng giá và chính sách.
  - FAQ.
  - Nguồn y khoa.
  - Brand/compliance rules.
- Trạng thái tài liệu: `DRAFT`, `UNDER_REVIEW`, `APPROVED`, `EXPIRED`, `REVOKED`.
- Chỉ tài liệu `APPROVED` và còn hiệu lực được dùng trong generation.
- Chunking, embedding và retrieval phải giữ liên kết về nguồn gốc.
- Không ingest hồ sơ bệnh án đầy đủ nếu không cần thiết.

### FR-10 — Tạo brief

Brief phải gồm:

- Primary keyword và secondary keywords.
- Search intent và đối tượng đọc.
- Mục tiêu chuyển đổi.
- Suggested title, slug, meta description.
- Outline H1/H2/H3.
- Câu hỏi cần trả lời.
- Internal links đề xuất.
- External/evidence sources được phép.
- Claims dự kiến.
- Image requirements.
- Required clinic facts.
- Compliance notes.
- CTA và disclaimer phù hợp.
- Độ dài gợi ý, không coi số từ là mục tiêu chất lượng tuyệt đối.

### FR-11 — AI Writer

- Nhận brief, nguồn KB được phép và rule set đang hiệu lực.
- Trả structured output theo JSON Schema.
- Không tự bịa bác sĩ, giấy phép, công nghệ, giá, thời gian hoạt động, số ca hoặc kết quả.
- Mọi clinic-specific fact phải chứa `source_id`.
- Mọi medical claim phải chứa nguồn hoặc `review_required=true`.
- Khi thiếu dữ liệu, dùng marker rõ ràng như `[CẦN PHÒNG KHÁM XÁC NHẬN]`, không tự điền.
- Lưu prompt template version, model, input source IDs, output và token/cost metadata.

Ví dụ output:

```json
{
  "primary_keyword": "nâng mũi cấu trúc",
  "search_intent": "COMMERCIAL_INFORMATIONAL",
  "title": "string",
  "slug": "string",
  "meta_description": "string",
  "outline": [],
  "article_html": "string",
  "medical_claims": [
    {
      "claim": "string",
      "source_ids": ["uuid"],
      "risk_level": "MEDIUM",
      "review_required": true
    }
  ],
  "internal_links": [],
  "image_requirements": [],
  "compliance_warnings": [],
  "seo_score": 0
}
```

### FR-12 — Trình soạn thảo và versioning

- Rich-text editor hỗ trợ heading, list, table, link, callout và ảnh.
- Hiển thị citation và cảnh báo cạnh đoạn liên quan.
- Autosave draft.
- Mỗi lần submit review hoặc publish tạo immutable version.
- So sánh diff giữa hai phiên bản.
- Khôi phục bằng cách tạo phiên bản mới từ phiên bản cũ, không xóa lịch sử.

### FR-13 — Medical claims

- Tự trích xuất claim từ bài.
- Gắn vị trí claim trong article version.
- Phân loại loại claim: hiệu quả, rủi ro, phục hồi, chống chỉ định, quy trình, thời gian duy trì.
- Gán mức rủi ro.
- Reviewer có thể approve, reject, request source hoặc rewrite.
- Approval ghi reviewer, thời gian, version và comment.
- Claim không có nguồn không nhất thiết luôn sai, nhưng phải được đánh dấu và xử lý theo risk rule.

### FR-14 — Compliance Engine

- Rule có:
  - `rule_code`
  - phiên bản
  - ngày hiệu lực
  - phạm vi áp dụng
  - mức độ `INFO/WARNING/BLOCKING`
  - logic kiểm tra
  - thông báo
  - remediation
  - nguồn/căn cứ nội bộ
  - trạng thái phê duyệt pháp chế
- Hỗ trợ rule dạng deterministic và AI-assisted.
- AI-assisted result không được tự động bỏ qua blocking rule.
- Cho phép exception có lý do, người duyệt và thời hạn.
- Lưu rule snapshot đã áp dụng cho mỗi article version.

### FR-15 — Image library

- Upload ảnh, đọc metadata, tạo checksum.
- Lưu nguồn ảnh: `CLINIC`, `PATIENT`, `STOCK`, `AI_ILLUSTRATION`.
- Lưu owner/copyright/license.
- Tag theo dịch vụ, loại ảnh và nội dung.
- Tạo thumbnail và phiên bản web tối ưu.
- Xóa EXIF/GPS trước khi xuất bản.
- Alt text mô tả đúng ảnh, không nhồi keyword.
- Không dùng AI để thay đổi kết quả lâm sàng trong ảnh.

### FR-16 — Consent ledger

Với ảnh khách hàng/trước–sau, lưu:

- `consent_id`
- subject/patient reference dạng pseudonymous
- bằng chứng đồng ý
- ngày ký và thời hạn
- kênh được phép: website, social, paid ads, internal
- mục đích sử dụng
- dịch vụ
- phạm vi lãnh thổ nếu có
- trạng thái nhận dạng/che nhận dạng
- người xác minh
- trạng thái: `PENDING`, `VALID`, `EXPIRED`, `REVOKED`
- thời điểm và lý do thu hồi

Quy tắc:

- Chỉ dùng ảnh khi consent `VALID`, đúng kênh `website`, đúng mục đích và chưa hết hạn.
- Khi consent bị thu hồi, tạo job tìm toàn bộ nơi ảnh đang được dùng và cảnh báo gỡ.
- Bằng chứng consent phải có kiểm soát truy cập riêng.
- Không đưa dữ liệu nhận dạng vào alt text hoặc tên file.

### FR-17 — Automated QA

Chạy bốn nhóm:

1. Medical.
2. Compliance.
3. SEO.
4. Content quality.

Mỗi finding có:

- category
- rule code
- severity
- blocking status
- article location
- explanation
- proposed remediation
- resolved status
- resolver

### FR-18 — Approval workflow

- Cấu hình reviewer bắt buộc theo loại dịch vụ và risk.
- Hỗ trợ approve, reject, request changes.
- Không cho người tạo tự duyệt bước chuyên môn nếu policy của tổ chức không cho phép.
- Approval gắn với checksum của article version.
- Nội dung thay đổi làm checksum đổi phải invalidation theo mục 8.3.

### FR-19 — WordPress publishing

- Chỉ gửi `status=draft` trong MVP.
- Upload media trước, sau đó tạo/update post.
- Mapping title, slug, content HTML, excerpt, featured media, categories, tags, author và metadata SEO.
- Lưu `wp_post_id`, `wp_media_ids`, preview URL, response và thời gian.
- Idempotency: retry không được tạo bài trùng.
- Cho phép update một WordPress draft đã liên kết.
- Không ghi đè bài đã `publish` nếu chưa có hành động rõ ràng của người có quyền.
- Nếu plugin SEO không hỗ trợ API metadata, cảnh báo và dùng fallback được cấu hình.

### FR-20 — Performance monitoring

- Đồng bộ click, impression, CTR và average position từ Search Console.
- Lưu theo query, page, date, device và country khi được phép.
- Đề xuất `UPDATE_REQUIRED` khi:
  - traffic/position giảm vượt ngưỡng;
  - impression cao nhưng CTR thấp;
  - tài liệu nguồn hết hạn;
  - license/service fact thay đổi;
  - content freshness rule đến hạn;
  - phát hiện cannibalization mới.

### FR-21 — Notifications

- In-app notification cho review task, job failed, consent expiry và license expiry.
- Email là tùy chọn sau MVP hoặc bật nếu provider đã cấu hình.
- Không gửi dữ liệu y tế/PII nhạy cảm trong nội dung notification.

### FR-22 — Audit log

Ghi:

- actor
- organization
- action
- resource type/id
- timestamp
- request/correlation ID
- before/after summary đã loại secret
- IP/user agent nếu chính sách cho phép
- reason/comment với hành động nhạy cảm

Audit log không được sửa bởi người dùng thông thường.

---

## 10. Quy tắc an toàn nội dung và tuân thủ tại Việt Nam

### 10.1 Lưu ý pháp lý

Phần này là yêu cầu thiết kế sản phẩm, không phải tư vấn pháp lý. Trước khi vận hành thương mại, rule set phải được luật sư hoặc bộ phận pháp chế y tế tại Việt Nam xác minh theo văn bản đang có hiệu lực.

Các thông tin pháp lý nêu trong bản thảo nghiệp vụ ban đầu—bao gồm quy định quảng cáo dịch vụ khám chữa bệnh và bảo vệ dữ liệu cá nhân có hiệu lực trong năm 2026—phải được coi là **đầu vào cần xác minh**, không hard-code số hiệu văn bản hoặc kết luận pháp lý chưa được phê duyệt.

### 10.2 Thiết kế compliance bắt buộc

- Rule engine có phiên bản và ngày hiệu lực.
- Mỗi rule có nguồn, chủ sở hữu nghiệp vụ và trạng thái pháp chế phê duyệt.
- Cho phép áp dụng rule theo loại nội dung, dịch vụ, kênh và thời gian.
- Giữ snapshot rule khi bài được duyệt.
- Có quy trình cập nhật, regression test và re-check bài cũ.

### 10.3 Nội dung phải cảnh báo hoặc chặn

Các phát biểu sau mặc định là `BLOCKING` nếu không có rule ngoại lệ hợp lệ:

- “Đảm bảo đẹp 100%”.
- “Không có rủi ro”.
- “Không đau tuyệt đối”.
- “Cam kết không biến chứng”.
- “Duy trì vĩnh viễn”.
- “Tốt nhất Việt Nam” hoặc tuyên bố xếp hạng không có căn cứ.
- Kết quả chắc chắn hoặc đồng nhất cho mọi người.
- Chẩn đoán cá nhân từ dữ liệu chung.
- Che giấu hoặc làm nhẹ rủi ro đáng kể.
- Dịch vụ ngoài phạm vi chuyên môn đã xác minh.
- Thông tin bác sĩ, giấy phép, kinh nghiệm, giá, công nghệ hoặc số ca không có nguồn.

### 10.4 Thông tin cơ sở cần kiểm tra

Rule set pháp chế được phê duyệt phải xác định vị trí và trường bắt buộc, có thể gồm:

- Tên pháp lý của cơ sở.
- Địa chỉ hoạt động.
- Số giấy phép hoạt động.
- Thời gian hoạt động.
- Phạm vi hoạt động chuyên môn.
- Bác sĩ chịu trách nhiệm chuyên môn.

Không tự động chèn dữ liệu chưa xác minh.

### 10.5 Phân loại rủi ro nội dung

| Mức | Ví dụ | Quy trình tối thiểu |
|---|---|---|
| `LOW` | Giới thiệu cơ sở, checklist chung | Marketing review |
| `MEDIUM` | Quy trình, hồi phục, chi phí | Medical + marketing review |
| `HIGH` | Biến chứng, chống chỉ định, kết quả, trước–sau | Medical + compliance + marketing review |

### 10.6 Dữ liệu cá nhân

- Data minimization và purpose limitation.
- Pseudonymize định danh bệnh nhân.
- Mã hóa khi truyền và lưu trữ.
- Phân quyền bằng vai trò và tenant.
- Retention policy cấu hình được.
- Cơ chế truy xuất, sửa, thu hồi và xóa theo quy trình được phê duyệt.
- Không gửi dữ liệu bệnh án đầy đủ sang LLM.
- Redact PII trước khi gọi model khi có thể.
- Vendor/LLM phải được cấu hình về retention và khu vực xử lý theo quyết định pháp lý của tổ chức.

### 10.7 An toàn AI

- Prompt injection defense cho tài liệu nhập vào.
- Nội dung retrieval được coi là dữ liệu, không phải instruction.
- Allowlist loại nguồn được dùng.
- Structured output validation.
- Không cho model gọi trực tiếp WordPress.
- Không để model quyết định cuối cùng về compliance hoặc medical approval.
- Log model/version/prompt, nhưng redact secret và PII.
- Có kill switch để tắt generation hoặc publishing connector.

---

## 11. Kiểm tra SEO

### 11.1 Blocking checks

- Primary keyword đã được xác định.
- Không có bài đã duyệt khác cùng organization/site nhắm chính xác cùng primary keyword nếu chưa có quyết định merge/canonical.
- Title và slug không trùng.
- Chỉ có một H1.
- Heading hierarchy hợp lệ.
- Có canonical strategy.
- Không có broken internal link đã biết.
- Ảnh có quyền sử dụng hợp lệ.
- Không có placeholder chưa xử lý.
- Không có metadata vượt rule hard limit do tổ chức cấu hình.

### 11.2 Warning checks

- Title và meta description quá ngắn/dài.
- Keyword stuffing.
- Thiếu internal link tới trang dịch vụ hoặc nội dung liên quan.
- Alt text không mô tả ảnh.
- Đoạn văn lặp hoặc nội dung quá chung chung.
- Search intent không khớp format bài.
- Thiếu author/medical reviewer/date updated.
- Thiếu FAQ khi intent cho thấy có ích.
- Ảnh quá lớn hoặc chưa có WebP/AVIF fallback phù hợp.
- Nội dung tương tự cao với bài hiện có.

### 11.3 SEO score

SEO score chỉ là chỉ báo, không thay thế gate. Gợi ý trọng số:

- Intent match: 20%.
- Topic coverage: 20%.
- Metadata/structure: 15%.
- Internal linking: 15%.
- Original clinic value: 15%.
- Media/accessibility: 10%.
- Technical readiness: 5%.

Không được cho bài qua khi còn blocking finding dù score cao.

### 11.4 Structured data

- Hỗ trợ cấu hình schema phù hợp theo loại trang.
- Không tự thêm rating, review, medical credential hoặc FAQ không có dữ liệu thật.
- Kiểm tra JSON-LD hợp lệ trước khi gửi WordPress.
- Schema phải tắt được theo site.

---

## 12. Kiến trúc đề xuất

### 12.1 Phong cách

Modular monolith với worker tách tiến trình:

```text
Next.js Web App
      ↓
Backend API (FastAPI hoặc NestJS)
      ↓
PostgreSQL + pgvector
      ↓
Redis + Task Queue
      ↓
Background Workers
      ├── Keyword processing
      ├── Embedding/clustering
      ├── AI generation
      ├── Image processing
      ├── WordPress publishing
      └── Search Console sync

Object Storage (S3-compatible)
External APIs:
  LLM Provider
  WordPress REST API
  Google Search Console
  Google Ads / Keyword provider
  Optional SERP provider
```

### 12.2 Stack mặc định đề xuất

- Frontend: Next.js, TypeScript, Tailwind CSS, component library có accessibility.
- Backend: FastAPI, Python 3.12, Pydantic, SQLAlchemy, Alembic.
- Database: PostgreSQL 16 + pgvector.
- Queue: Redis + Celery/Dramatiq.
- Object storage: S3-compatible.
- Auth: secure session/OIDC provider; không tự xây password auth nếu không cần.
- Observability: OpenTelemetry, structured logs, error tracking.
- Test: Pytest, Playwright, contract tests.
- Local development: Docker Compose.

Nếu đội chọn NestJS thay FastAPI, phải giữ nguyên module boundary, API contract và acceptance criteria.

### 12.3 Module boundaries

- `identity`
- `organizations`
- `clinics`
- `licenses`
- `services`
- `websites`
- `keywords`
- `content_planning`
- `knowledge_base`
- `ai_generation`
- `articles`
- `medical_review`
- `compliance`
- `media`
- `consents`
- `publishing`
- `analytics`
- `notifications`
- `audit`
- `jobs`

Module không truy cập trực tiếp bảng private của module khác ngoài repository/service contract đã định nghĩa.

### 12.4 Luồng generation an toàn

```text
Request
→ Authorization
→ Load article/brief
→ Retrieve only approved KB chunks
→ Redact sensitive data
→ Build versioned prompt
→ Call LLM
→ Validate JSON Schema
→ Run deterministic policy checks
→ Extract claims and citations
→ Save new immutable article version
→ Queue automated QA
```

---

## 13. Mô hình dữ liệu

### 13.1 Quy ước chung

- Primary key: UUID.
- Mọi bảng tenant-scoped có `organization_id`.
- Thời gian lưu UTC với `created_at`, `updated_at`.
- Soft delete chỉ dùng khi có yêu cầu khôi phục; dữ liệu compliance/audit không xóa tùy tiện.
- Dùng optimistic locking (`version` hoặc `updated_at`) cho editor.
- Secret lưu qua secret manager/encrypted field, không trả lại API.

### 13.2 Bảng chính

#### `organizations`

- `id`
- `name`
- `slug`
- `status`
- `settings_json`
- timestamps

#### `users`

- `id`
- `email`
- `display_name`
- `auth_provider_id`
- `status`
- timestamps

#### `organization_members`

- `organization_id`
- `user_id`
- `roles_json` hoặc relation `member_roles`
- `joined_at`
- unique `(organization_id, user_id)`

#### `clinics`

- `id`
- `organization_id`
- `legal_name`
- `brand_name`
- `address`
- `contact_json`
- `operating_hours_json`
- `verification_status`
- `last_verified_at`

#### `clinic_licenses`

- `id`
- `organization_id`
- `clinic_id`
- `license_number`
- `issuing_authority`
- `effective_from`
- `expires_at`
- `status`
- `document_object_key`
- `verified_by`
- `verified_at`

#### `professional_scopes`

- `id`
- `clinic_license_id`
- `code`
- `name`
- `description`
- `status`

#### `doctors`

- `id`
- `organization_id`
- `clinic_id`
- `full_name`
- `verified_profile_json`
- `professional_license_ref`
- `verification_status`

#### `services`

- `id`
- `organization_id`
- `clinic_id`
- `name`
- `slug`
- `risk_level`
- `status`
- `verified_facts_json`

#### `service_professional_scopes`

- `service_id`
- `professional_scope_id`
- `verified_by`
- `verified_at`

#### `websites`

- `id`
- `organization_id`
- `name`
- `base_url`
- `platform`
- `status`
- `settings_json`
- `credential_secret_ref`
- `last_health_check_at`

#### `keywords`

- `id`
- `organization_id`
- `website_id`
- `text`
- `normalized_text`
- `locale`
- `source`
- `intent`
- `funnel_stage`
- `service_id`
- `metrics_json`
- `priority_score`
- `status`
- unique theo site/locale/normalized text

#### `keyword_clusters`

- `id`
- `organization_id`
- `website_id`
- `name`
- `primary_keyword_id`
- `centroid_embedding`
- `status`

#### `keyword_cluster_members`

- `cluster_id`
- `keyword_id`
- `similarity_score`
- `source`

#### `content_plans`

- `id`
- `organization_id`
- `website_id`
- `service_id`
- `cluster_id`
- `content_type`
- `owner_user_id`
- `planned_date`
- `status`

#### `knowledge_sources`

- `id`
- `organization_id`
- `source_type`
- `title`
- `uri_or_object_key`
- `status`
- `effective_from`
- `expires_at`
- `approved_by`
- `approved_at`
- `metadata_json`

#### `knowledge_chunks`

- `id`
- `organization_id`
- `knowledge_source_id`
- `chunk_index`
- `content`
- `embedding`
- `content_hash`
- `metadata_json`

#### `articles`

- `id`
- `organization_id`
- `website_id`
- `content_plan_id`
- `primary_keyword_id`
- `service_id`
- `current_version_id`
- `status`
- `risk_level`
- `assigned_to`
- timestamps

#### `article_versions`

- `id`
- `organization_id`
- `article_id`
- `version_number`
- `title`
- `slug`
- `meta_description`
- `content_html`
- `structured_output_json`
- `content_hash`
- `created_by`
- `generation_run_id`
- immutable timestamp

#### `generation_runs`

- `id`
- `organization_id`
- `article_id`
- `prompt_template_version`
- `model`
- `input_source_ids_json`
- `parameters_json`
- `status`
- `usage_json`
- `error_code`
- timestamps

#### `medical_claims`

- `id`
- `organization_id`
- `article_version_id`
- `claim_text`
- `claim_type`
- `risk_level`
- `location_json`
- `review_required`
- `status`

#### `claim_sources`

- `medical_claim_id`
- `knowledge_source_id`
- `locator`
- `support_level`

#### `review_tasks`

- `id`
- `organization_id`
- `article_id`
- `article_version_id`
- `review_type`
- `assignee_id`
- `status`
- `decision`
- `comment`
- `decided_at`

#### `compliance_rules`

- `id`
- `rule_code`
- `version`
- `jurisdiction`
- `scope_json`
- `severity`
- `rule_type`
- `definition_json`
- `effective_from`
- `effective_to`
- `legal_approval_status`
- `source_reference`
- unique `(rule_code, version)`

#### `qa_runs`

- `id`
- `organization_id`
- `article_version_id`
- `rule_set_snapshot_json`
- `status`
- `score_json`
- timestamps

#### `qa_findings`

- `id`
- `qa_run_id`
- `category`
- `rule_code`
- `severity`
- `is_blocking`
- `location_json`
- `message`
- `remediation`
- `status`
- `resolved_by`
- `resolved_at`

#### `images`

- `id`
- `organization_id`
- `source_type`
- `object_key_original`
- `object_key_web`
- `checksum`
- `mime_type`
- `width`
- `height`
- `license_json`
- `service_tags_json`
- `contains_patient`
- `identity_protection_status`
- `status`

#### `image_consents`

- `id`
- `organization_id`
- `image_id`
- `subject_reference`
- `evidence_object_key`
- `allowed_channels_json`
- `allowed_purposes_json`
- `effective_from`
- `expires_at`
- `status`
- `verified_by`
- `verified_at`
- `revoked_at`
- `revocation_reason`

#### `article_images`

- `article_version_id`
- `image_id`
- `placement`
- `alt_text`
- `caption`
- `consent_validation_snapshot_json`

#### `publishing_jobs`

- `id`
- `organization_id`
- `article_id`
- `article_version_id`
- `website_id`
- `idempotency_key`
- `target_status`
- `status`
- `attempt_count`
- `wp_post_id`
- `response_summary_json`
- `last_error_code`
- timestamps

#### `seo_metrics`

- `id`
- `organization_id`
- `website_id`
- `article_id`
- `date`
- `query`
- `page`
- `device`
- `country`
- `clicks`
- `impressions`
- `ctr`
- `position`

#### `jobs`

- `id`
- `organization_id`
- `job_type`
- `resource_type`
- `resource_id`
- `status`
- `attempt`
- `max_attempts`
- `scheduled_at`
- `started_at`
- `finished_at`
- `error_code`
- `correlation_id`

#### `audit_logs`

- `id`
- `organization_id`
- `actor_type`
- `actor_id`
- `action`
- `resource_type`
- `resource_id`
- `before_summary_json`
- `after_summary_json`
- `reason`
- `correlation_id`
- `created_at`

### 13.3 Index quan trọng

- Tenant + status cho các bảng nghiệp vụ.
- `keywords(website_id, normalized_text, locale)`.
- Vector index cho `knowledge_chunks.embedding`.
- `articles(organization_id, website_id, status)`.
- `article_versions(article_id, version_number desc)`.
- `medical_claims(article_version_id, status)`.
- `review_tasks(assignee_id, status)`.
- `image_consents(image_id, status, expires_at)`.
- `publishing_jobs(idempotency_key)` unique.
- `seo_metrics(website_id, date, page, query)`.
- `audit_logs(organization_id, created_at desc)`.

---

## 14. API nội bộ

### 14.1 Quy ước

- Base path: `/api/v1`.
- JSON request/response.
- OpenAPI là contract chính.
- Pagination theo cursor cho danh sách lớn.
- Idempotency key cho generation và publishing.
- Error format thống nhất:

```json
{
  "error": {
    "code": "ARTICLE_NOT_APPROVED",
    "message": "Article must be approved before publishing",
    "details": {},
    "correlation_id": "uuid"
  }
}
```

### 14.2 Endpoint chính

#### Organizations và clinics

- `GET/POST /organizations`
- `GET/PATCH /organizations/{id}`
- `GET/POST /clinics`
- `GET/PATCH /clinics/{id}`
- `POST /clinics/{id}/licenses`
- `POST /licenses/{id}/verify`
- `GET/POST /services`

#### Websites và integrations

- `GET/POST /websites`
- `POST /websites/{id}/test-connection`
- `POST /websites/{id}/sync-taxonomies`
- `POST /integrations/search-console/connect`
- `POST /integrations/keyword-provider/test`

#### Keywords

- `POST /keywords/import`
- `POST /keywords/sync-search-console`
- `POST /keywords/classify`
- `POST /keywords/cluster`
- `GET /keywords`
- `PATCH /keywords/{id}`
- `POST /keyword-clusters/{id}/merge`
- `POST /keyword-clusters/{id}/split`

#### Content planning

- `GET/POST /content-plans`
- `POST /content-plans/{id}/generate-brief`
- `POST /content-plans/{id}/approve-keyword`

#### Knowledge Base

- `GET/POST /knowledge-sources`
- `POST /knowledge-sources/{id}/approve`
- `POST /knowledge-sources/{id}/revoke`
- `POST /knowledge-sources/{id}/reindex`

#### Articles

- `GET/POST /articles`
- `GET/PATCH /articles/{id}`
- `GET /articles/{id}/versions`
- `POST /articles/{id}/generate`
- `POST /articles/{id}/versions`
- `POST /articles/{id}/run-qa`
- `POST /articles/{id}/transition`
- `GET /articles/{id}/diff?from=&to=`

#### Review

- `GET /review-tasks`
- `POST /review-tasks/{id}/approve`
- `POST /review-tasks/{id}/reject`
- `POST /review-tasks/{id}/request-changes`
- `POST /medical-claims/{id}/decision`

#### Media và consent

- `POST /images/upload`
- `GET/PATCH /images/{id}`
- `POST /images/{id}/consents`
- `POST /consents/{id}/verify`
- `POST /consents/{id}/revoke`
- `POST /articles/{id}/images`
- `GET /images/{id}/usage`

#### Publishing

- `POST /articles/{id}/publish/wordpress-draft`
- `GET /publishing-jobs/{id}`
- `POST /publishing-jobs/{id}/retry`
- `POST /websites/{id}/sync-post-status`

#### Analytics

- `POST /analytics/search-console/sync`
- `GET /analytics/articles/{id}`
- `GET /analytics/opportunities`

#### Audit và jobs

- `GET /audit-logs`
- `GET /jobs/{id}`
- `POST /jobs/{id}/cancel` nếu job chưa bắt đầu và loại job cho phép

### 14.3 Webhooks

- `/webhooks/wordpress` nếu có plugin hỗ trợ.
- Webhook phải xác minh chữ ký, chống replay và idempotent.
- Không tin dữ liệu trạng thái từ webhook trước khi validate site/resource mapping.

---

## 15. Tích hợp bên ngoài

### 15.1 WordPress REST API

Chức năng:

- Health check.
- Đọc categories, tags, users/authors và bài hiện có.
- Upload media.
- Tạo/update post.
- Đọc trạng thái post.

Yêu cầu:

- Ưu tiên Application Password hoặc cơ chế token được quản trị phê duyệt.
- Quyền tài khoản tối thiểu.
- Chỉ `draft` trong MVP.
- Timeout, retry với exponential backoff và jitter.
- Redact credential và response nhạy cảm khỏi log.
- Idempotency dựa trên internal publishing job + post mapping.

### 15.2 Google Search Console

- OAuth với scope tối thiểu.
- Đồng bộ Search Analytics theo incremental window.
- Quản lý quota và backoff.
- Không giả định API trả toàn bộ dữ liệu chi tiết; hiển thị giới hạn dữ liệu.
- Lưu timestamp sync và khoảng dữ liệu.

### 15.3 Google Ads Keyword Planning

- Tích hợp tùy chọn.
- Cache kết quả theo keyword, locale và thời gian.
- Quản lý quota.
- Không phụ thuộc bắt buộc để chạy MVP; CSV/provider adapter là fallback.

### 15.4 SERP provider

- Dùng adapter interface để thay provider.
- Không scrape Google trực tiếp.
- Lưu terms/source/date của dữ liệu.
- Có circuit breaker và budget limit.

### 15.5 LLM provider

Interface tối thiểu:

```text
generate_structured(prompt, schema, safety_config)
embed(texts)
moderate(optional)
```

Yêu cầu:

- Provider/model cấu hình được.
- Timeout/retry chỉ cho lỗi an toàn để retry.
- Request ID và usage tracking.
- Structured output validation.
- Không log raw sensitive prompt mặc định.
- Có test double để test không gọi API thật.

### 15.6 Object storage

- Presigned upload/download.
- Private bucket mặc định.
- Antivirus/malware scan cho upload nếu hạ tầng hỗ trợ.
- Lifecycle policy.
- Không public ảnh gốc bệnh nhân.
- Phiên bản web chỉ được xuất sau khi consent check hợp lệ.

---

## 16. Hàng đợi tác vụ

### 16.1 Loại job

- `KEYWORD_IMPORT`
- `KEYWORD_METRICS_SYNC`
- `KEYWORD_CLASSIFICATION`
- `KEYWORD_CLUSTERING`
- `KB_INGESTION`
- `EMBEDDING_GENERATION`
- `ARTICLE_GENERATION`
- `AUTOMATED_QA`
- `IMAGE_PROCESSING`
- `WORDPRESS_MEDIA_UPLOAD`
- `WORDPRESS_DRAFT_PUBLISH`
- `SEARCH_CONSOLE_SYNC`
- `CONSENT_REVOCATION_SCAN`
- `CONTENT_FRESHNESS_SCAN`

### 16.2 Trạng thái job

```text
QUEUED → RUNNING → SUCCEEDED
                 ↘ RETRY_SCHEDULED → RUNNING
                 ↘ FAILED
QUEUED → CANCELLED
```

### 16.3 Yêu cầu

- At-least-once delivery; handler phải idempotent.
- Exponential backoff + jitter.
- Max attempts theo job type.
- Dead-letter queue.
- Correlation ID xuyên suốt.
- Heartbeat và timeout cho job dài.
- Progress percentage cho job có thể đo.
- Không retry lỗi validation hoặc permission.
- Dashboard xem job thất bại và retry có kiểm soát.

---

## 17. Yêu cầu phi chức năng

### NFR-01 — Bảo mật

- OWASP ASVS mức phù hợp cho SaaS xử lý dữ liệu nhạy cảm.
- TLS mọi kết nối.
- Mã hóa secret và object nhạy cảm khi lưu.
- CSRF protection cho session auth.
- Rate limiting theo user, tenant và endpoint.
- Input validation và output encoding.
- HTML sanitizer cho nội dung editor/AI.
- Dependency and container scanning trong CI.
- Không commit secret.

### NFR-02 — Tenant isolation

- Mọi repository query tenant-scoped.
- Test tự động cho cross-tenant access.
- Object storage path và authorization tenant-scoped.
- Queue payload luôn có organization context đã ký/validate.

### NFR-03 — Hiệu năng

- P95 API read thông thường dưới 500 ms, không tính external API.
- P95 write thông thường dưới 1 giây.
- Tác vụ trên 3 giây phải chuyển qua queue khi hợp lý.
- Danh sách lớn dùng pagination.
- Không load toàn bộ article versions/metrics vào một request.

### NFR-04 — Độ tin cậy

- Publishing idempotent.
- Không mất article version đã submit.
- Backup database và object metadata.
- RPO/RTO phải được xác định trước pilot; mục tiêu gợi ý RPO 24 giờ, RTO 8 giờ cho MVP.
- Graceful degradation khi AI/SEO provider không hoạt động.

### NFR-05 — Quan sát hệ thống

- Structured logs với correlation ID.
- Metrics: latency, error rate, queue depth, job duration, publish success, token/cost.
- Trace external integrations.
- Alert cho queue backlog, repeated publish failure và auth failure.
- Redaction PII/secrets.

### NFR-06 — Accessibility và UX

- Mục tiêu WCAG 2.1 AA cho luồng chính.
- Keyboard navigation.
- Error message rõ ràng, không chỉ dựa vào màu.
- Hiển thị lý do bài bị chặn và cách xử lý.
- Xác nhận rõ hành động revoke, reject và publish draft.

### NFR-07 — Maintainability

- Module boundaries rõ ràng.
- Migration có rollback strategy.
- API schema và domain enums dùng chung hoặc sinh tự động.
- Unit, integration và end-to-end tests.
- ADR cho quyết định kiến trúc quan trọng.

### NFR-08 — Privacy

- Data inventory.
- Retention schedule theo loại dữ liệu.
- Export/delete workflow theo chính sách đã phê duyệt.
- Không dùng dữ liệu khách hàng để train model nếu chưa có căn cứ và phê duyệt rõ ràng.

---

## 18. Repository structure đề xuất

```text
ai-seo-clinic/
├─ README.md
├─ AGENTS.md
├─ .env.example
├─ .gitignore
├─ docker-compose.yml
├─ Makefile
├─ docs/
│  ├─ product-spec.md
│  ├─ architecture.md
│  ├─ compliance/
│  │  ├─ README.md
│  │  ├─ rule-catalog.md
│  │  └─ legal-review-log.md
│  ├─ adr/
│  └─ api/
├─ apps/
│  ├─ web/
│  │  ├─ app/
│  │  ├─ components/
│  │  ├─ features/
│  │  ├─ lib/
│  │  └─ tests/
│  ├─ api/
│  │  ├─ src/
│  │  │  ├─ core/
│  │  │  ├─ identity/
│  │  │  ├─ organizations/
│  │  │  ├─ clinics/
│  │  │  ├─ keywords/
│  │  │  ├─ knowledge_base/
│  │  │  ├─ articles/
│  │  │  ├─ reviews/
│  │  │  ├─ compliance/
│  │  │  ├─ media/
│  │  │  ├─ publishing/
│  │  │  ├─ analytics/
│  │  │  └─ audit/
│  │  └─ tests/
│  └─ worker/
│     ├─ tasks/
│     └─ tests/
├─ packages/
│  ├─ contracts/
│  ├─ ui/
│  ├─ prompts/
│  │  ├─ templates/
│  │  ├─ schemas/
│  │  └─ evals/
│  └─ compliance-rules/
├─ migrations/
├─ scripts/
├─ infra/
│  ├─ docker/
│  └─ deployment/
└─ tests/
   ├─ e2e/
   ├─ fixtures/
   └─ security/
```

### 18.1 AGENTS.md nên quy định

- Lệnh setup, lint, test, migrate.
- Không thay đổi compliance rule mà thiếu test và source reference.
- Không log PII hoặc secret.
- Mọi endpoint mới phải có authorization và tenant test.
- Mọi migration phải có mô tả dữ liệu và rollback strategy.
- Không gọi API thật trong test mặc định.
- Không auto-publish WordPress.

---

## 19. Biến môi trường

File `.env.example` chỉ chứa tên và giá trị giả:

```dotenv
# Runtime
APP_ENV=development
APP_NAME=ai-seo-clinic
APP_BASE_URL=http://localhost:3000
API_BASE_URL=http://localhost:8000
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql+psycopg://app:app@postgres:5432/ai_seo_clinic

# Redis / Queue
REDIS_URL=redis://redis:6379/0
QUEUE_NAME_DEFAULT=default
QUEUE_MAX_RETRIES=5

# Auth
AUTH_PROVIDER_ISSUER=
AUTH_PROVIDER_CLIENT_ID=
AUTH_PROVIDER_CLIENT_SECRET=
SESSION_SECRET=

# Encryption
APP_ENCRYPTION_KEY=
SECRET_MANAGER_PROVIDER=local

# Object storage
S3_ENDPOINT_URL=http://minio:9000
S3_REGION=auto
S3_BUCKET_PRIVATE=ai-seo-private
S3_ACCESS_KEY_ID=
S3_SECRET_ACCESS_KEY=

# AI
LLM_PROVIDER=
LLM_API_KEY=
LLM_MODEL=
EMBEDDING_MODEL=
LLM_TIMEOUT_SECONDS=90
LLM_MAX_COST_PER_JOB=
LLM_STORE_RAW_PROMPTS=false

# Google Search Console / Ads
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REDIRECT_URI=
GOOGLE_ADS_DEVELOPER_TOKEN=
GOOGLE_ADS_CUSTOMER_ID=

# Keyword / SERP provider
KEYWORD_PROVIDER=
KEYWORD_PROVIDER_API_KEY=
SERP_PROVIDER=
SERP_PROVIDER_API_KEY=

# WordPress defaults
WORDPRESS_REQUEST_TIMEOUT_SECONDS=30
WORDPRESS_ALLOW_AUTO_PUBLISH=false

# Observability
OTEL_EXPORTER_OTLP_ENDPOINT=
ERROR_TRACKING_DSN=

# Feature flags
FEATURE_GOOGLE_ADS=false
FEATURE_SERP_PROVIDER=false
FEATURE_EMAIL_NOTIFICATIONS=false
FEATURE_AI_IMAGE_GENERATION=false
```

Quy tắc:

- Credential riêng từng website không lưu trực tiếp trong biến môi trường dùng chung; lưu bằng secret reference.
- Production secret đi qua secret manager.
- Startup phải fail rõ ràng khi thiếu biến bắt buộc.
- Không in giá trị secret khi validate config.

---

## 20. Phát triển theo giai đoạn

### Giai đoạn 0 — Discovery và compliance baseline

- Chốt dịch vụ pilot.
- Xác minh quy trình phòng khám.
- Legal review rule catalog.
- Data classification và threat model.
- Chốt stack và ADR.

**Exit criteria:** rule set v1 được chuyên môn/pháp chế ký duyệt; backlog MVP được ưu tiên.

### Giai đoạn 1 — Foundation

- Repository, CI, local Docker.
- Auth, RBAC, tenant isolation.
- Organization, clinic, license, service.
- Audit log.

**Exit criteria:** cross-tenant security tests pass.

### Giai đoạn 2 — SEO ingestion và planning

- CSV import.
- Search Console adapter.
- Keyword classification, clustering và scoring.
- Content planner và cannibalization.

**Exit criteria:** tạo được content plan từ bộ keyword pilot.

### Giai đoạn 3 — Knowledge Base và AI drafting

- KB ingestion, approval và retrieval.
- Brief generation.
- Structured draft generation.
- Versioning và editor.

**Exit criteria:** draft luôn trace được về nguồn và prompt/model version.

### Giai đoạn 4 — Safety, review và media

- Claim extraction.
- Compliance engine.
- QA findings.
- Review workflow.
- Image library, consent, EXIF removal.

**Exit criteria:** blocking rules thực sự ngăn approval/publishing.

### Giai đoạn 5 — WordPress và analytics

- WordPress connection.
- Media upload + draft publish.
- Idempotency/retry.
- Search Console metrics và update suggestions.

**Exit criteria:** chạy end-to-end trên WordPress staging.

### Giai đoạn 6 — Pilot hardening

- Security review.
- Performance test.
- Backup/restore drill.
- Operational dashboards.
- User training.
- Pilot với một phòng khám.

**Exit criteria:** đáp ứng toàn bộ acceptance criteria bắt buộc.

---

## 21. Kế hoạch kiểm thử

### 21.1 Unit tests

- Priority score.
- Intent/risk mapping.
- State transition guards.
- Approval invalidation.
- Consent validity.
- Compliance deterministic rules.
- WordPress payload mapping.
- Redaction và sanitization.

### 21.2 Integration tests

- PostgreSQL tenant isolation.
- Queue retry/idempotency.
- Object storage authorization.
- LLM structured-output adapter bằng fake provider.
- WordPress API bằng mock server.
- Search Console adapter bằng fixtures.

### 21.3 End-to-end tests

1. Admin tạo clinic/license/service.
2. SEO import keyword và tạo plan.
3. Editor tạo brief/draft.
4. QA phát hiện câu tuyệt đối.
5. Editor sửa.
6. Medical Reviewer duyệt claim.
7. Consent hợp lệ được gắn ảnh.
8. Marketing duyệt.
9. Publisher tạo WordPress draft.
10. Retry không tạo post trùng.

### 21.4 Security tests

- User tenant A không đọc/sửa tenant B.
- Editor không tự medical approve.
- Secret không xuất hiện trong API/log.
- HTML injection bị sanitize.
- Prompt injection trong KB không thay đổi system policy.
- Consent revoked chặn lần xuất bản tiếp theo.
- Publishing endpoint từ chối article chưa approved.

### 21.5 AI evaluations

Tạo bộ eval cố định bằng tiếng Việt:

- Hallucination clinic facts.
- Unsupported medical claims.
- Absolute promises.
- Missing risk disclosure.
- Citation fidelity.
- Intent match.
- Duplicate/generic content.
- Prompt injection resistance.

Mọi thay đổi prompt/model phải chạy eval và so sánh với baseline.

---

## 22. Tiêu chí nghiệm thu MVP

### AC-01 — Kết nối WordPress

**Given** website WordPress staging và credential hợp lệ  
**When** admin kiểm tra kết nối  
**Then** hệ thống xác nhận endpoint/quyền và không lộ credential.

### AC-02 — Hồ sơ cơ sở

Hệ thống lưu được clinic, giấy phép, phạm vi chuyên môn, bác sĩ và dịch vụ; dịch vụ không được xác minh phải sinh blocking finding khi dùng cho bài quảng bá.

### AC-03 — Keyword pipeline

Nhập được CSV tối thiểu 1.000 keyword, loại trùng, phân intent, cluster và chấm priority mà không chặn request giao diện.

### AC-04 — Content plan

Người dùng tạo được cluster/pillar/supporting plan và nhận cảnh báo cannibalization với bài hiện có.

### AC-05 — AI brief và draft

Draft trả về đúng JSON Schema, có metadata, outline, HTML, claims, source IDs, image requirements và compliance warnings.

### AC-06 — Không bịa thông tin cơ sở

Nếu không có tên bác sĩ, giá, giấy phép hoặc dữ liệu riêng trong nguồn đã duyệt, output phải để marker cần xác nhận hoặc bỏ qua, không tự tạo giá trị.

### AC-07 — Medical review

Mọi claim `HIGH` chưa được reviewer có quyền duyệt phải chặn trạng thái `APPROVED`.

### AC-08 — Compliance

Câu “cam kết không biến chứng” hoặc nội dung tương đương phải tạo blocking finding và ngăn xuất bản.

### AC-09 — Consent

Ảnh trước–sau không có consent `VALID` cho kênh website phải bị chặn. Thu hồi consent tạo danh sách đầy đủ bài đang sử dụng ảnh.

### AC-10 — Image processing

Ảnh xuất bản đã bị xóa GPS/EXIF nhạy cảm, có phiên bản web tối ưu và alt text có thể sửa.

### AC-11 — SEO QA

Hệ thống kiểm tra title, meta, slug, H1, headings, intent, duplicate target, internal links, alt text, canonical readiness và placeholder.

### AC-12 — Workflow

Không thể bỏ qua các bước review bắt buộc bằng cách gọi API trực tiếp; state guard nằm ở backend.

### AC-13 — Versioning

Mỗi lần submit review hoặc publish tạo immutable version; có thể xem diff và khôi phục thành version mới.

### AC-14 — WordPress draft

Article đã approved tạo được WordPress post với `status=draft`, upload featured image và lưu ID/preview URL.

### AC-15 — Idempotency

Gửi lại cùng idempotency key không tạo post hoặc media trùng.

### AC-16 — Analytics

Đồng bộ được click, impression, CTR và position từ Search Console cho site đã kết nối.

### AC-17 — Audit

Tạo, sửa, duyệt, reject, revoke consent và publish đều có audit record với actor, resource, timestamp và correlation ID.

### AC-18 — Tenant isolation

Automated tests chứng minh tenant A không truy cập dữ liệu tenant B qua API, object storage hoặc job.

### AC-19 — Failure handling

LLM hoặc WordPress timeout không làm mất dữ liệu; job retry theo policy và hiển thị lỗi có thể xử lý.

### AC-20 — MVP publishing policy

Không có đường dẫn UI, API hoặc worker nào có thể đặt WordPress post thành `publish` khi `WORDPRESS_ALLOW_AUTO_PUBLISH=false`.

---

## 23. Definition of Done

Một feature chỉ hoàn thành khi:

- Có acceptance criteria và được demo.
- Authorization và tenant boundary đã kiểm tra.
- Unit/integration test phù hợp pass.
- Migration đã review nếu thay schema.
- API/OpenAPI được cập nhật.
- Audit và observability phù hợp.
- Không log PII/secret.
- UI có empty/loading/error state.
- Documentation được cập nhật.
- Compliance/security review được thực hiện nếu feature chạm dữ liệu nhạy cảm, AI hoặc publishing.

---

## 24. Rủi ro và biện pháp

| Rủi ro | Biện pháp |
|---|---|
| AI bịa thông tin | Approved sources only, structured output, source IDs, blocking markers |
| Nội dung y khoa sai | Claim extraction, risk level, medical review |
| Quy định thay đổi | Versioned rule engine, legal approval, effective dates |
| Ảnh dùng sai consent | Consent ledger, publish-time validation, revocation scan |
| Tạo bài hàng loạt kém chất lượng | Human approval, uniqueness QA, rate/budget limits |
| WordPress tạo bài trùng | Idempotency key và post mapping |
| Lộ dữ liệu bệnh nhân | Minimization, pseudonymization, encryption, redaction |
| Cross-tenant leak | Repository scoping và automated security tests |
| Vendor outage | Queue, retry, circuit breaker, graceful degradation |
| Chi phí AI tăng | Usage tracking, per-job budget, caching, model routing |

---

## 25. Câu hỏi cần chốt trước production

- Văn bản pháp lý và rule catalog nào đã được pháp chế phê duyệt?
- Dữ liệu nào được phép gửi tới LLM provider?
- Vị trí lưu trữ dữ liệu và retention period?
- Ai có quyền duyệt y khoa/compliance cho từng dịch vụ?
- WordPress dùng plugin SEO nào?
- Phương thức xác thực WordPress được phê duyệt?
- Nguồn keyword/SERP chính thức?
- SLA, RPO, RTO thực tế?
- Có cần SSO?
- Có cho phép nhiều cơ sở chung một website?
- Quy trình gỡ ảnh trên WordPress sau khi consent bị thu hồi?

---

## 26. Prompt thực tế để giao cho Codex

Sao chép prompt dưới đây vào Codex cùng file đặc tả này:

```text
Bạn là kỹ sư trưởng chịu trách nhiệm triển khai MVP trong file
AI_SEO_THAM_MY_MVP_SPEC.md.

Mục tiêu:
Xây một modular monolith có frontend Next.js/TypeScript, backend FastAPI/Python,
PostgreSQL + pgvector, Redis task queue, S3-compatible storage và WordPress
REST integration. Sản phẩm tạo WordPress draft, tuyệt đối không auto-publish.

Nguyên tắc triển khai:
1. Đọc toàn bộ specification và kiểm tra repository hiện tại trước khi sửa.
2. Nếu repository trống, scaffold cấu trúc monorepo được đề xuất.
3. Tạo AGENTS.md với các lệnh setup/lint/test/migrate và guardrails bảo mật.
4. Viết một implementation plan theo vertical slices; triển khai từng slice có
   migration, API, UI tối thiểu và test.
5. Ưu tiên theo thứ tự:
   a) foundation + tenant isolation + RBAC + audit;
   b) clinic/license/service;
   c) keyword import/planning;
   d) Knowledge Base + AI structured draft;
   e) claims/compliance/reviews;
   f) image consent;
   g) WordPress draft publishing;
   h) analytics.
6. Không hard-code kết luận pháp lý. Tạo versioned compliance rule framework và
   seed một bộ rule mẫu được đánh dấu NEEDS_LEGAL_REVIEW.
7. Không gọi API thật trong test. Cung cấp provider interfaces, fake adapters và
   fixtures.
8. Mọi dữ liệu tenant-scoped phải có organization_id và automated cross-tenant
   tests.
9. Mọi state transition và permission check phải được enforce ở backend.
10. Mọi generation phải lưu model, prompt version, source IDs và validate JSON
    Schema.
11. Không để AI gọi trực tiếp WordPress. Publishing chỉ chạy qua approved,
    idempotent background job.
12. Ảnh bệnh nhân phải private; publish-time check phải xác minh consent VALID,
    đúng kênh website, đúng mục đích và chưa hết hạn.
13. Không log secret, raw credential, PII hoặc dữ liệu y tế nhạy cảm.
14. Không xóa hoặc ghi đè thay đổi có sẵn không liên quan trong repository.
15. Sau mỗi vertical slice, chạy formatter, lint, typecheck, unit/integration
    tests và báo cáo kết quả thật.

Yêu cầu đầu ra cho lần triển khai đầu tiên:
- Phân tích hiện trạng repository.
- Chốt các giả định kỹ thuật cần thiết.
- Tạo cấu trúc dự án chạy local bằng Docker Compose.
- Tạo database schema/migrations nền tảng.
- Triển khai auth abstraction, organizations, memberships/RBAC, clinics,
  licenses, professional scopes, services và audit logs.
- Tạo OpenAPI endpoints tương ứng.
- Tạo frontend tối thiểu cho đăng nhập giả lập local, chọn organization, danh
  sách clinic và form clinic/license/service.
- Thêm unit tests, integration tests và cross-tenant tests.
- Tạo .env.example không chứa secret.
- Cập nhật README với lệnh chạy và trạng thái tính năng.
- Không triển khai tính năng ngoài specification nếu chưa cần cho vertical slice.

Tiêu chí kết thúc lần đầu:
- Toàn bộ stack khởi động được bằng hướng dẫn trong README.
- Migration chạy sạch trên database mới.
- API health check thành công.
- Các test nền tảng pass.
- Tenant A không thể đọc hoặc sửa dữ liệu tenant B.
- Audit log được tạo cho thao tác create/update/verify.
- Không có endpoint auto-publish WordPress.

Trước khi code, hãy trình bày kế hoạch ngắn và những giả định có ảnh hưởng lớn.
Sau đó triển khai, kiểm thử và chỉ báo cáo những gì đã thực sự hoàn thành.
```

---

## 27. Prompt tiếp nối cho từng phase

Sau khi phase nền tảng hoàn thành, dùng mẫu sau:

```text
Tiếp tục triển khai phase [TÊN PHASE] theo AI_SEO_THAM_MY_MVP_SPEC.md.

Trước khi sửa:
- Kiểm tra code, migration và test hiện có.
- Liệt kê acceptance criteria liên quan.
- Nêu migration/API/UI/job sẽ thêm.

Trong khi triển khai:
- Giữ tenant isolation, RBAC, audit, idempotency và privacy guardrails.
- Dùng fake provider trong test.
- Không mở rộng scope sang phase khác trừ dependency nhỏ bắt buộc.

Khi hoàn tất:
- Chạy formatter, lint, typecheck và test liên quan.
- Cập nhật README/architecture/OpenAPI.
- Báo cáo file thay đổi, test đã chạy, giới hạn còn lại và bước tiếp theo.
```

---

## 28. Kết luận phạm vi phiên bản đầu

Phiên bản đầu tiên phải là:

> Một ứng dụng web kết nối WordPress, tập trung vào 4–6 dịch vụ phẫu thuật thẩm mỹ, hỗ trợ thu thập và phân nhóm từ khóa, lập kế hoạch nội dung, tạo bản nháp có nguồn, kiểm duyệt claim y khoa, quản lý ảnh/consent, kiểm tra compliance–SEO và đưa bài lên WordPress ở trạng thái chờ duyệt.

Ưu tiên số một của MVP là **khả năng truy vết, kiểm duyệt và kiểm soát rủi ro**, không phải số lượng bài tạo ra.
