# Data Analyst Personal Portfolio Project

## Tổng quan dự án (Project Overview)
Dự án này bao gồm hai phân tích dữ liệu chính nhằm chứng minh kỹ năng xử lý dữ liệu đa dạng:
1.  **Phân tích hành vi ẩm thực mùa đông:** Sử dụng **Python (Pandas, Matplotlib, Seaborn)** để khám phá xu hướng ăn uống qua các năm.
2.  **Dashboard Quản trị Logistics:** Sử dụng **Power BI** để tối ưu hóa theo dõi vận hành, doanh thu và vận chuyển.

---

## Công cụ sử dụng (Tech Stack)
* **Ngôn ngữ:** Python (Phân tích & Trực quan hóa)
* **Công cụ BI:** Power BI
* **Thư viện Python:** Pandas, Matplotlib, Seaborn
* **Kỹ năng:** Đọc hiểu biểu đồ, Xử lý dữ liệu (Cleaning), Phân tích tương quan.

---

## Phần 1: Phân tích Ẩm thực Mùa đông (Python Analysis)

Phần này tập trung vào việc tìm hiểu thói quen ăn uống của người dùng trong giai đoạn mùa đông từ năm 2023 đến 2025.

### 1. Cơ cấu món ăn theo mùa
Biểu đồ tròn cho thấy sự tăng trưởng dần đều về sự quan tâm của người dùng đối với các món ăn mùa đông qua từng năm, đạt đỉnh vào năm 2025 với **36.7%**.

![Cơ cấu món ăn theo mùa](./Bieu_do_the_hien_co_cau_giua_mon_an_va_mua.jpg) 

### 2. Phân loại thực phẩm (Food Categories)
Qua biểu đồ cột, chúng ta thấy **Đồ uống (Drink)** chiếm số lượng áp đảo (hơn 60 món), theo sau là Soup và Snack. Điều này cho thấy nhu cầu giữ ấm cơ thể bằng đồ uống nóng trong mùa đông là rất lớn.

![Số lượng món ăn theo kiểu](./Bieu_do_the_hien_so_luong_mon_an_theo_kieu_an.jpg)

### 3. Tương quan giữa Calo và Độ phổ biến
Biểu đồ phân tán (Scatter Plot) cho thấy sự phân bổ đa dạng. Đặc biệt, có một cụm dữ liệu tập trung mạnh ở mức **240 Calories**, nơi mà cả Drink, Snack và Soup đều có điểm Popularity trải dài từ thấp đến cao.

![Tương quan Calo và Popularity](./Bieu_do_phan_tan_the_hien_giua_luong_Calories_va_chi_so_Popularity.jpg)


---

## Phần 2: Dashboard Vận hành Logistics (Power BI)

Dashboard cung cấp cái nhìn toàn diện về tình hình kinh doanh tính đến ngày 25/12/2025.

* **File gốc:** [Tải file .pbix tại đây](./DATA_ANALYST_PERSONAL_PORTFOLIO_PROJECT.pbix)

![Logistics Dashboard](DATA_ANALYST_PERSONAL_PORTFOLIO_LOGISTIC_PROJECT.jpg)

### Các chỉ số chính (KPIs):
* **Tổng doanh thu:** 77.65 triệu VNĐ.
* **Chi phí vận chuyển:** 51.32 triệu VNĐ (Chiếm tỷ trọng lớn trong tổng chi phí).
* **Trạng thái đơn hàng:** Tỷ lệ đơn hàng **Delivered (35.02%)** và **Shipped (30.24%)** chiếm ưu thế, cho thấy luồng vận hành khá ổn định.
* **Phương tiện vận chuyển:** **Van (41.02%)** là phương tiện chủ lực trong việc giao nhận.

### Phân tích vùng miền:
* Khu vực **Hà Nội (HN)** có lượng mưa trung bình cao nhất nhưng nhiệt độ trung bình thấp nhất, ảnh hưởng trực tiếp đến thời gian giao hàng.
* Khách hàng **Retail (Bán lẻ)** chiếm số lượng đơn hàng vượt trội so với khách hàng B2B ở tất cả các khu vực (CT, DN, HCM, HN, HP).

---

## Kết luận & Đề xuất (Insights & Recommendations)
* **Ẩm thực:** Các doanh nghiệp F&B nên tập trung đẩy mạnh menu đồ uống vào mùa đông năm 2025 vì đây là phân khúc có số lượng và sự quan tâm cao nhất.
* **Logistics:** Cần tối ưu hóa chi phí vận chuyển vì nó đang chiếm gần bằng tổng chi phí phải trả. Cần xem xét lại hiệu suất đội xe Motorbike để giảm tải cho xe Van.

---

## Liên hệ
* **Email:** nguyenhachien070104@gmail.com
