# Kinh nghiệm và Quy chuẩn Soạn đề từ KTL3.py, TrinhBayCongThuc.pdf và VeHinh.pdf

Tài liệu này đúc rút kinh nghiệm thực tiễn từ quá trình soạn thảo 4 mã câu hỏi (`HH194TF002`, `GT153SA021`, `GT153SA023`, `GT154SA034`) trong file `KTL3.py`, kết hợp các quy định bắt buộc về trình bày công thức toán học (`TrinhBayCongThuc.pdf`) và kỹ thuật vẽ hình TikZ (`VeHinh.pdf`).

---

## I. Cấu trúc & Logic Soạn đề từ KTL3.py

### 1. Quản lý Số liệu Ngẫu nhiên (Randomization Guardrails)
Để tránh sai số dấu phẩy động (float precision issues) và đảm bảo đề bài luôn có nghiệm đẹp:
* **Bộ số Pythagore mở rộng (Pythagorean quadruples):** Đối với hình Oxyz (`HH194TF002`), luôn khai báo danh mục các bộ số nguyên để độ dài vector luôn là số nguyên (ví dụ: `(2, 1, 2)`, `(2, 3, 6)`, `(4, 4, 2)`). Điều này giúp tránh việc dùng căn thức phức tạp trong tính toán độ dài đoạn thẳng.
* **Bộ tham số tối ưu (Predefined configuration loops):** 
  * Đối với bài toán cực trị thực tế như tính thời gian ngắn nhất (`GT153SA021`), cần thiết lập trước các "họ nghiệm" (families of integers) sao cho đạo hàm luôn cho nghiệm nguyên đẹp ($x = x_0$ hoặc phân số hữu hạn).
  * Đối với bài toán tối ưu hình học như tính diện tích lồng cá (`GT154SA034`), lập danh mục các từ điển (`config = random.choice([ ... ])`) chứa các tham số tương quan nguyên đẹp để đảm bảo điểm cực trị và kết quả tối ưu là các số nguyên hoặc số thập phân rất đẹp.
  * Đối với bài toán y học/vật lý như bán kính khí quản (`GT153SA023`), chọn đường kính $D$ là bội số của $0{,}3$ trong khoảng $[0{,}6; 2{,}7]$ để điểm tối ưu $r_{\text{opt}} = D/3$ luôn có phần thập phân hữu hạn (làm tròn đến hàng phần mười).
* **Vòng lặp Guardrail (`while True`):** Luôn kiểm tra các điều kiện suy biến trước khi sinh đề:
  * Hai vector chỉ phương không cùng phương (tích có hướng khác vector không).
  * Ba điểm không thẳng hàng.
  * Tránh tam giác cân/đều khi không cần thiết (tránh bẫy đáp án nhiễu bị triệt tiêu).
  * Điểm sinh ra không nằm trên các mặt phẳng tọa độ đặc biệt nếu đề bài không yêu cầu.
  * Các hoành độ/cao độ trong các trường hợp khác nhau của hình thang/hình chữ nhật phải phân biệt và không trùng lặp với các đỉnh đã cho.

### 2. Cấu trúc Lời giải Sư phạm 4 Bước
Lời giải tự luận ngắn (SA) luôn được trình bày theo cấu trúc chuẩn mực sử dụng ký hiệu vòng tròn đen của LaTeX (`\ding{172}` đến `\ding{175}`):
* **Bước 1:** `\textcolor{blue}{\textbf{\ding{172} Phân tích, định hướng tìm lời giải}}`
  * Giải thích trực giác vật lý/hình học của bài toán, định hướng phương pháp tối ưu hóa hoặc thiết lập mô hình toán.
* **Bước 2:** `\textcolor{blue}{\textbf{\ding{173} Đặt ẩn và lập hàm số}}`
  * Đặt biến số (ví dụ: $NE = x$ mét), nêu rõ điều kiện của ẩn dựa trên thực tế (ví dụ: $0 < x < AB$).
  * Biểu diễn các đại lượng khác theo biến đã đặt và lập hàm số mục tiêu (ví dụ: hàm thời gian $t(x)$, hàm tốc độ $V(r)$, hàm diện tích $S(x)$).
* **Bước 3:** `\textcolor{blue}{\textbf{\ding{174} Giải phương trình đạo hàm tìm cực trị}}`
  * Tính đạo hàm của hàm mục tiêu trên khoảng xác định.
  * Giải phương trình đạo hàm bằng 0, chỉ rõ nghiệm thỏa mãn điều kiện.
  * Lập bảng biến thiên (BBT) bằng lệnh helper (`bbtb2TCT` hoặc `bbtb2CTC`).
* **Bước 4:** `\textcolor{blue}{\textbf{\ding{175} Kết luận, so sánh với điều kiện}}`
  * Kết luận giá trị lớn nhất/nhỏ nhất từ bảng biến thiên.
  * Thực hiện phép làm tròn cuối cùng (như `math.ceil` đối với bài toán thực tế cần làm tròn lên hoặc làm tròn thập phân theo yêu cầu đề bài).
  * Đưa ra đáp án cuối cùng nằm trong hộp `\boxed{}`.

### 3. Bố cục Đề bài & Hình vẽ (Minipage Layout)
Để đề bài cân đối và trực quan:
* Sử dụng môi trường `minipage` để chia đôi màn hình: phần câu hỏi nằm bên trái (`0.65\textwidth` hoặc `0.75\textwidth`) và hình vẽ TikZ nằm bên phải (`0.32\textwidth` hoặc `0.2\textwidth`).
* Dùng `\hfill` giữa hai `minipage` và đặt `\vspace{0pt}` đầu minipage hình vẽ để căn đỉnh văn bản và đỉnh hình vẽ thẳng hàng.

---

## II. Quy định Trình bày Công thức Toán học (TrinhBayCongThuc.pdf)

Quy định soạn thảo LaTeX bắt buộc phải tuân thủ để đảm bảo đồng bộ và thẩm mỹ:
1. **Môi trường toán:** Tất cả các công thức và con số (kể cả số đếm đơn lẻ) bắt buộc phải đặt trong cặp dấu đô la (ví dụ: `$m$`, `$3$`).
2. **Dấu chấm câu:** Dấu chấm, dấu phẩy câu không được nằm trong dấu đô la (ví dụ: `tam giác $ABC$,` chứ không viết `tam giác $ABC,$`). Ngoại trừ các ký hiệu điểm cụ thể như `$S.ABC$`, tọa độ điểm `$A(2; 3)$`, hoặc viết tắt tên file.
3. **Dấu hai chấm:** Không dùng dấu hai chấm `:` sau các từ liên kết như "là", "bằng", "thì".
4. **Dấu nháy kép:** Sử dụng `\lq\lq` và `\rq\rq` hoặc `''` trong mã nguồn để hiển thị dấu nháy kép đẹp mắt.
5. **Tập xác định:** Viết hoa tập xác định bằng lệnh `$\mathscr{D}$`.
6. **Hiệu tập hợp:** Dùng dấu `\setminus` (ví dụ: $\Omega \setminus A$), không dùng dấu gạch chéo ngược `\backslash`.
7. **Tập rỗng:** Chỉ dùng duy nhất ký hiệu `$\varnothing$`, không dùng `\emptyset`.
8. **Dấu nhân:** Dùng `\times` hoặc `\cdot`, không dùng dấu chấm thường. Khuyến khích viết liền không dấu nhân khi nhân số với biến (ví dụ: `$2a$`).
9. **Dấu ba chấm:**
   * Liệt kê phần tử: dùng `\ldots` (ví dụ: `$A = \{1, 2, \ldots, 9\}$`).
   * Phép toán nối tiếp: dùng `\cdots` (ví dụ: `$1 + 2 + \cdots + 9$`).
10. **Phẩy thập phân:** Đối với số thập phân kiểu Việt Nam, bắt buộc đặt dấu phẩy trong ngoặc nhọn `{,}` để tránh khoảng trắng LaTeX (ví dụ: `$1{,}234$`).
11. **Hệ phương trình (Môi trường Và):** 
    * Dùng lệnh `\heva{&x=a\\&y=b\\&z=c}` hoặc `\begin{cases} &x=a\\&y=b\\&z=c \end{cases}`. Luôn có dấu `&` để căn thẳng hàng các phương trình.
12. **Hệ tuyển (Môi trường Hoặc):**
    * Dùng lệnh `\hoac{&x=a\\&y=b\\&z=c}` hoặc `\left[\begin{aligned} &x=a\\&y=b\\&z=c \end{aligned}\right.` với dấu `&` để căn thẳng hàng.
13. **Tổ hợp, chỉnh hợp, hoán vị, xác suất:**
    * Tổ hợp: `\mathrm{C}_n^k`
    * Chỉnh hợp: `\mathrm{A}_n^k`
    * Hoán vị: `\mathrm{P}_n`
    * Xác suất của biến cố: `\mathrm{P}(A)` (chữ P đứng thẳng).
14. **Phép biến hình:** Dùng chữ cái in thẳng đứng: `\mathrm{T}_{\vec{v}}`, `\mathrm{Q}_{(O,\alpha)}`, `\mathrm{V}_{(I,k)}`.
15. **Ký hiệu vi phân, hằng số:** Dùng chữ đứng cho vi phân `\mathrm{d}x`, cơ số log tự nhiên `\mathrm{e}`, đơn vị ảo $i$ (ví dụ: `\mathrm{d}x`, `\mathrm{e}`).
16. **Max/Min:** Luôn chỉ rõ biến số chạy bên dưới: `\max\limits_{x\in\mathscr{D}} f(x)`, `\min\limits_{x\in\mathscr{D}} f(x)`.
17. **Cực trị:** Gõ điểm cực đại là `$x_\text{CĐ}$`, điểm cực tiểu là `$x_\text{CT}$`.
18. **Đơn vị đo lường:** Đơn vị phải viết đứng, có khoảng trắng ngăn cách với con số và **không** đặt đơn vị trong dấu ngoặc đơn (ví dụ: `$3$ cm`, `$4$ m$^2$`, `$5$ m/s`).
19. **Tích phân:** Viết cận đầy đủ ở trên và dưới dấu tích phân: `\displaystyle\int\limits_a^b f(x)\mathrm{\,d}x`.
20. **Quan hệ hình học:** Song song dùng `\parallel` (ví dụ: `$a\parallel b$`), vuông góc dùng `\perp` (ví dụ: `$a\perp b$`).
21. **Ký hiệu độ:** Dùng `^\circ` (ví dụ: `90^\circ`), không dùng `^0` hay `^o`.
22. **Khoảng cách:** Gõ khoảng cách bằng chữ đứng `\mathrm{d}` (ví dụ: `\mathrm{d}[\Delta, \Delta']` hoặc `\mathrm{d}(\Delta, \Delta')`).
23. **Ký hiệu góc:** Khi tính lượng giác, không dùng ký hiệu mũ góc `\widehat` (chỉ gõ `\cos A`, `\sin(AB, CD)`). Chỉ gõ `\widehat{ABC}` khi biểu diễn góc hình học thuần túy.
24. **Phương trình đường thẳng/mặt phẳng:** Gõ theo định dạng: `(P)\colon ax+by+cz+d=0` (sử dụng dấu hai chấm định nghĩa `\colon`).
25. **Vector pháp tuyến:** Gõ `\overrightarrow{n}_{P}` hoặc `\vec{n}_{(P)}`.
26. **Đưa hình vào văn bản:** Khuyến khích dùng lệnh `\immini{câu dẫn}{code hình}`.
27. **Bảng biến thiên (BBT):**
    * Không kẻ khung ngoài bảng biến thiên.
    * Khi BBT nằm riêng biệt, bắt buộc đặt trong môi trường `\begin{center} ... \end{center}`.
    * Khai báo chiều cao dòng hợp lý từ `0.6` đến `1.0` (dòng $x$ và $y'$ là `0.6` hoặc `0.7`, dòng $y$ là `2`).
      `\tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]{$x$ /0.6, $y'$ /0.6, $y$ /2}{...}`
28. **Ký hiệu khoảng, đoạn:** Sử dụng các lệnh giãn cách tự động `\left(...\right)` hoặc `\left[...\right]`.
29. **Dấu cách sau lệnh:** Sau các lệnh macro của LaTeX như `\True` hay `\triangle`, bắt buộc phải có khoảng trắng (ví dụ: `\True $x=2$`, `\triangle ABC`).
30. **Phân số:**
    * Phân số đứng riêng biệt dùng `\dfrac{A}{B}`.
    * Phân số nằm ở số mũ, cơ số, hoặc cận tích phân dùng `\frac` hoặc `\tfrac`.
31. **Từ phiên âm tiếng nước ngoài:** Viết đủ dấu tiếng Việt và có gạch nối ở giữa (ví dụ: mô-đun, véc-tơ, phế-nang, vi-rút).
32. **Từ viết tắt và lệnh tùy biến:** Tuyệt đối không tự định nghĩa lệnh viết tắt hoặc môi trường mới ngoài quy định chung để tránh lỗi biên dịch hệ thống.
33. **Khoảng cách lời giải:** Không dùng lệnh `\hfill` khi bắt đầu câu hỏi hay bài tập. Không dùng các lệnh nhảy dòng thủ công `\\`, `\par` ở đầu lời giải. Sau các môi trường như `listEX` hay `enumerate`, hệ thống đã tự động xuống dòng nên không chèn thêm lệnh `\\` hay `\par`.
34. **Cú pháp căn dòng công thức dài:** Sử dụng môi trường `eqnarray*` kết hợp bắt buộc với lệnh `\allowdisplaybreaks` để tự động ngắt trang khi công thức tràn trang.
    ```latex
    \allowdisplaybreaks
    \begin{eqnarray*}
    & & f(x) = g(x) \\
    &\Leftrightarrow & f_1(x) = g_2(x) \\
    &\Leftrightarrow & f_3(x) = 0
    \end{eqnarray*}`
    ```
35. **Dấu chấm cuối phương trình:** Luôn đặt dấu chấm câu ở cuối phương trình hoặc hệ phương trình khi kết thúc một câu/vế toán học.

---

## III. Quy chuẩn Vẽ hình TikZ (VeHinh.pdf)

Để tạo ra các hình vẽ trực quan, chuyên nghiệp và có độ chính xác hình học cao:

### 1. Khai báo Điểm & Điểm Đặc biệt
* **Khai báo tọa độ gốc:** Sử dụng lệnh `\coordinate` để định vị toàn bộ các điểm cốt lõi trước khi vẽ (ví dụ: `\coordinate (A) at (0,0);`).
* **Trung điểm và Vị tự (Lệnh Calc):** 
  * Sử dụng thư viện `calc` để tính toán tọa độ điểm mà không cần tính thủ công tọa độ số.
  * Trung điểm $M$ của $AB$: `\coordinate (M) at ($(A)!0.5!(B)$);`.
  * Phép vị tự tỉ lệ $k$ từ $A$ đến $B$: `\coordinate (P) at ($(A)!k!(B)$);`.
* **Phép tịnh tiến vector:** 
  * Xác định điểm mới bằng cách cộng vector: `\coordinate (E) at ($(A)+(1,-2)$);`.
* **Chân đường vuông góc (Perpendicular projection):**
  * Tìm chân đường cao $H$ hạ từ $A$ xuống $BC$: `\coordinate (H) at ($(B)!(A)!(C)$);`.
* **Phép quay (Rotation):**
  * Tìm ảnh $C$ của điểm $B$ qua phép quay tâm $A$ góc $60^\circ$: `\coordinate (c) at ($(a)!1!60:(b)$);`.

### 2. Giao điểm của các Đường (Intersections)
* Khi cần lấy giao điểm giữa hai đường thẳng hoặc đường cong, gán tên cho các đường bằng tham số `name path`:
  `\draw[name path=line1] (A)--(B);`
  `\draw[name path=line2] (C)--(D);`
* Lấy giao điểm bằng lệnh `path intersections`:
  `\path [name intersections={of=line1 and line2, by=H}];`
* Trường hợp có từ 2 giao điểm trở lên (như đường tròn cắt đường thẳng), lấy danh sách giao điểm tự động:
  `\path [name intersections={of=circle_path and line_path}];`
  `\coordinate (A) at (intersection-1);`
  `\coordinate (B) at (intersection-2);`

### 3. Vẽ Ký hiệu Vuông góc (`\khvuong`)
Để vẽ ký hiệu góc vuông chuẩn xác tại điểm $B$ của góc $\widehat{ABC}$, bắt buộc chèn macro tùy biến ở đầu file TikZ:
```latex
\def\khvuong[size=#1](#2,#3,#4){%
\draw ($(#3)!#1!(#2)$) -- ($($(#3)!#1!(#2)$)+($(#3)!#1!(#4)$)-(#3)$)-- ($(#3)!#1!(#4)$);
}
```
* **Cú pháp sử dụng:** `\khvuong[size=6pt](a,b,c);` (vẽ ký hiệu vuông góc tại đỉnh $B$, kích cỡ cạnh là $6$pt).

### 4. Vẽ Đồ thị Hàm số & Tô màu Miền Giới hạn
* **Lệnh vẽ đồ thị:** Luôn sử dụng tùy chọn `smooth` để đường cong mềm mại và xác định rõ miền `domain`:
  `\draw[domain=-2:2, smooth, blue] plot (\x, {(\x)^2});`
* **Công thức toán trong TikZ:** TikZ sử dụng ký hiệu toán học máy tính (dùng `*` cho phép nhân, `/` cho phép chia, `^` cho phép lũy thừa và đặt các biến trong ngoặc đơn, ví dụ: `(2/3)*(\x)^(3)-3*\x+1`).
* **Tô sọc kẻ miền đồ thị:** Sử dụng thư viện `patterns` bằng cách gọi `\usetikzlibrary{patterns}` ở đầu văn bản.
  * Các kiểu sọc phổ biến: `north east lines`, `north west lines`, `horizontal lines`, `vertical lines`, `crosshatch`, `dots`, `bricks`, `checkerboard`.
  * Để tô sọc mà không vẽ đường viền ngoài: thêm tham số `draw=none`.
    `\draw[pattern=north east lines, draw=none] (0,0) circle (1.5);`
  * Để tô màu giới hạn chính xác giữa các đường cong: sử dụng môi trường `\begin{scope} \clip ... \end{scope}` để cắt miền giới hạn rồi tô màu.

### 5. Hình vẽ Không gian 3D (Nét khuất & Nét nhìn thấy)
* **Hình trụ:** Đáy trên là ellipse hoàn chỉnh nét liền. Đáy dưới gồm nửa ellipse phía trước nét liền (`start angle=180, end angle=360`), nửa ellipse phía sau nét đứt (`start angle=0, end angle=180` kết hợp `[dashed]`). Trục hình trụ và các đường bán kính đáy khuất vẽ nét đứt `[dashed]`.
* **Hình nón:** Tương tự hình trụ, đỉnh nối với hai biên đáy bằng nét liền, đường cao và bán kính đáy vẽ nét đứt.
* **Mặt cầu:** Vẽ đường tròn bao ngoài bằng nét liền, vẽ đường vĩ tuyến/kinh tuyến bằng các cung ellipse nét liền phía trước và nét đứt `[dashed]` phía sau.
* **Hình lăng trụ:** Xác định tọa độ các đỉnh đáy dưới. Các đỉnh đáy trên được xác định bằng phép tịnh tiến vector tịnh tiến thẳng đứng. Vẽ các cạnh bên và cạnh đáy khuất bằng nét đứt `[dashed]`, các cạnh nhìn thấy vẽ nét liền.
