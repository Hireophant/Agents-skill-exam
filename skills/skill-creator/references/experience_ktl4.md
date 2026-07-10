# Kinh nghiệm từ các câu đợt kiểm tra lần 4 (KTL4.py)

Tài liệu này tổng hợp các bài học kinh nghiệm, lỗi thường gặp và cách xử lý đúng rút ra từ việc soạn thảo và tối ưu hóa 4 câu hỏi: **SP233TF016**, **GT223SA011**, **GT224SA005**, và **HH254SA014**.

---

## 1. Câu hỏi SP233TF016
- **Dạng bài**: SP/xác suất có điều kiện/TF.
- **Lỗi hoặc điểm khó**:
  - Gặp lỗi hiển thị hoặc lỗi cú pháp khi chèn trực tiếp các chuỗi ký tự phần trăm `%` hoặc dấu ngoặc nhọn lồng nhau trong f-string của Python.
  - Quên bọc các biến số/ký hiệu toán học trong dấu đô-la `$ ... $`, dẫn đến việc hiển thị lệch phông chữ Tiếng Việt trên bản in.
  - Lỗi dùng dấu nháy kép thẳng `"..."` trong văn bản LaTeX thay vì dùng cặp ký tự chuẩn `\lq\lq ... \rq\rq`.
- **Cách xử lý đúng**:
  - Tách biệt hoàn toàn phần tính toán số học với chuỗi hiển thị LaTeX.
  - Sử dụng các cặp lệnh `\lq\lq` và `\rq\rq` khi viết các mệnh đề hoặc cụm từ phát biểu trong lời giải.
- **Trình bày cần giữ**:
  - Luôn lược bỏ dấu hai chấm `:` sau các từ liên kết như "là" hoặc "bằng" khi phát biểu mệnh đề hoặc kết luận trong Tiếng Việt.
  - Đảm bảo bọc toàn bộ các tham số số học (kể cả số phần trăm) vào trong môi trường toán học dạng `$ {biến} $`.
- **Guardrail cần thêm**:
  - Kiểm tra tính khác biệt giữa phương án đúng và phương án nhiễu trước khi đóng gói đề bài.

---

## 2. Câu hỏi GT223SA011
- **Dạng bài**: GT/SA.
- **Lỗi hoặc điểm khó**:
  - Sử dụng hàm làm tròn `round()` mặc định của Python gây ra sai số ngẫu nhiên do thuật toán làm tròn chẵn (Banker's rounding).
  - Quên đóng khung kết quả cuối cùng trong phần kết luận của lời giải.
- **Cách xử lý đúng**:
  - Luôn sử dụng hàm `math_round` (đã được định nghĩa sẵn trong thư viện `thuvien.py`) thay thế hoàn toàn cho hàm `round()` mặc định của Python.
  - Kết quả cuối cùng tại Bước 4 (Kết luận) phải được bọc trong lệnh `\boxed{...}` (ví dụ: `\boxed{A_0}`).
- **Trình bày cần giữ**:
  - Trình bày lời giải đầy đủ theo cấu trúc 4 bước của giáo viên:
    1. Phân tích, định hướng tìm lời giải.
    2. Đặt ẩn và lập hàm số/công thức.
    3. Giải phương trình/tính toán.
    4. Kết luận (có đóng khung đáp án).
- **Guardrail cần thêm**:
  - Kiểm tra độ dài chuỗi đáp án cuối cùng sau khi làm tròn không vượt quá 4 ký tự (`len(str(A0)) <= 4`) để vừa với ô nhập liệu của Moodle.

---

## 3. Câu hỏi GT224SA005
- **Dạng bài**: GT/SA.
- **Lỗi hoặc điểm khó**:
  - Việc tính toán tích phân của hàm phân nhánh với số mũ lớn dễ gây ra hiện tượng tràn số (overflow) trên máy tính của học sinh hoặc hệ thống biên dịch.
  - Quên đóng khung kết quả cuối cùng.
  - Cần vẽ đồ thị phân nhánh bằng TikZ mô phỏng chính xác đường cong quang hợp và diện tích lá.
- **Cách xử lý đúng**:
  - Giới hạn miền giá trị random của các hệ số $a, b$, thời điểm $t_1, t_2, t_3$ và diện tích lá $S_0$ sao cho tích phân hàm mũ luôn nằm trong ngưỡng an toàn của kiểu dữ liệu float/double.
  - Dùng `math_round` cho các phép tính số thực để đồng bộ kết quả.
  - Vẽ đồ thị hàm số phân nhánh trực quan bằng TikZ (vẽ rõ các trục tọa độ, nét đứt gióng điểm gãy khúc, và đường cong tăng trưởng thực tế).
  - Kết quả cuối cùng tại Bước 4 (Kết luận) phải được bọc trong lệnh `\boxed{...}` (ví dụ: `\boxed{m}`).
- **Trình bày cần giữ**:
  - Bám sát cấu trúc lời giải 4 bước tự luận chuẩn.
  - Đặt hình vẽ minh họa TikZ căn giữa (`\begin{center}`) ngay phía trên đầu mục ① Phân tích, định hướng tìm lời giải.

---

## 4. Câu hỏi HH254SA014
- **Dạng bài**: HH/Oxyz/SA.
- **Lỗi hoặc điểm khó**:
  - Viết ký hiệu vectơ bằng lệnh ngắn `\vec{...}` thay vì lệnh chuẩn `\overrightarrow{...}` làm mũi tên hiển thị bị ngắn và lệch trên các chữ cái ghép (như $AB, CE$).
  - Random tọa độ các điểm ngẫu nhiên dẫn đến trường hợp 3 điểm $A, B, C$ thẳng hàng hoặc trùng nhau, làm bài toán trở nên vô lý.
  - TikZ minh họa vị trí đào hầm bị lệch hoặc chèn không đúng vị trí.
- **Cách xử lý đúng**:
  - Thay thế toàn bộ các ký hiệu vectơ trong tệp generator bằng `\overrightarrow` (ví dụ: `\overrightarrow{AB}`).
  - Kiểm tra tính phân biệt của các điểm và điều kiện không thẳng hàng của 3 điểm bằng cách tính tích có hướng (cross product):
    ```python
    cross_x = dy1 * dz2 - dz1 * dy2
    cross_y = dz1 * dx2 - dx1 * dz2
    cross_z = dx1 * dy2 - dy1 * dx2
    if cross_x == 0 and cross_y == 0 and cross_z == 0:
        continue  # Loại bỏ trường hợp thẳng hàng
    ```
  - Dựng hình núi và hai đường hầm cắt nhau bằng TikZ, đặt căn giữa (`\begin{center}`) ngay phía trên đề mục 1.
  - Kết quả cuối cùng tại Bước 4 (Kết luận) phải được bọc trong lệnh `\boxed{...}` (ví dụ: `\boxed{v_2}`).
