# Trinh Bay Cong Thuc Full Standard

This is the mandatory formula, notation, unit, list, equation-alignment, and solution-presentation standard extracted from the user's `TrinhBayCongThuc.pdf`. The original PDF is stored next to this file as `TrinhBayCongThuc.pdf`; when extraction looks visually odd, obey the source PDF.

## Mandatory Use

Read and obey this reference whenever writing or reviewing math notation, formulas, units, intervals, systems, combinations/permutations/probability symbols, vectors, distances, planes/lines, integrals, variation tables, enumerated solution parts, or aligned solution chains. This standard overrides convenience habits and generic LaTeX style unless the user explicitly gives a local override.

## Full Extracted Text

```text
                          1. QUY ĐỊNH VỀ SOẠN THẢO VÀ KÝ HIỆU
            1 Các công thức, số đều phải đưa vào môi trường toán. Ví dụ: Với $m$ là tham số, tam giác
               $ABC$ đều có các cạnh bằng $3$.
            2 Dấuchấmcâukhôngđượcnằmtrongdấuđôla$a$.Màphảinằmngoài,trừmộtsốtrường
               hợp như $S.ABC$,$A(2; 3)$, \[abc.\]...
            3 Sau “là, bằng, thì ...” không có dấu hai chấm “:”
            4 Dấu “dấu nháy kép” dùng \lq\lq dấu nháy kép\rq\rq\
               Hoặc Dấu “dấu nháy kép” dùng ‘‘dấu nháy kép’’
            5 Gõ tập xác định theo $\mathscr{D}$: D.
            6 Hiệu tập hợp dùng $\Omega\setminus A$: Ω\A, không dùng $\backslash$.
            7 Gõ tập rỗng dùng $\varnothing$: ∅ (không dùng ký hiệu khác).
            8 Gõ dấu nhân dùng $\times$ × hoặc $\cdot$ · không dùng dấu chấm ., khuyến khích bỏ
               dấu nhân trong nhiều trường hợp không cần thiết có: như 2a ta không viết 2.a.
            9 Gõ $\ldots$ ... cho liệt kê phần tử như "tập hợp A = {1,2,...,9}" và gõ $\cdots$ ···
               cho các phép toán tương tự 1+2+···+9 hoặc 1·2···9.
            10 Gõ dấu phẩy thập phân ta dùng $1{,}234$ và được 1,234.
                       
                       x=a
                       
                       
            11 Gõhệvày=b dùnglệnh\heva{&x=a\\&y=b\\&z=c}, có dấu & để canh thẳng hàng hoặc
                       
                       
                       
                       z=c
               $\begin{cases}&x=a\\&y=b\\&z=c \end{cases}$ (có dấu & để canh thẳng hàng).
                     
                      x=a
                     
            12 Gõ hệ       dùng lệnh \hoac{&x=a\\&y=b\\&z=c}, có dấu & để canh thẳng hàng hoặc
                     
                      y = b
                     
                      z = c
               dùnglệnh$\left[\begin{aligned} &x=a\\&y=b\\&z=c \end{aligned}\right.$(códấu
               & để canh thẳng hàng).
                                          k                        k
            13 Gõ tổ hợp chỉnh hợp hoán vị C dùng $\mathrm{C}_n^k$, A dùng $\mathrm{A}_n^k$, Pn
                                          n                        n
               dùng $\mathrm{P}_n$, gõ xác suất dùng P(A) dùng $\mathrm{P}(A)$.
            14 Gõ phép tịnh tiến, quay, vị tự, ...T#» dùng $\mathrm{T}_{\vec{v}}$,
                                              v
               Q(O,α) dùng $\mathrm{Q}_{(O,\alpha)}$,
               V(I,k) dùng $\mathrm{V}_{(I,k)}$.
            15 Gõ dx, e, idùng $\mathrm{d}x$, $\mathrm{e}$, $i$.
                                                   1
            16 Gõ max, min dùng
               $\max\limits_{x\in\mathscr D} f(x)$, $\min\limits_{x\in\mathscr D} f(x)$maxf(x),
               minf(x).                                                                   x∈D
               x∈D
            17 Gõ điểm cực trị ta dùng $x_\text{CĐ}$ : xCĐ, $x_\text{CT}$ : xCT.
            18 Gõđơnvị:inđứngvàkhôngchovàongoặc,códấucáchgiữasốvàđơnvị,vídụnhư$3$ cm;
               $4$ m$^2$; $5$ m/s; ...
            19 Nguyên hàm, tích phân dùng: $\displaystyle\int\limits_a^b f(x)\mathrm{\,d}x$
            20 Songsongdùng$a\parallel b$a k b, không dùng // ; vuông góc dùng $a\perp b$: a ⊥ b.
            21 Ký hiệu độ 90◦ dùng: 90^\circ không dùng $90^0$ hay $90^o$.
                                                                     0           0
            22 Khoảng cách dùng: $\mathrm{d}[\Delta,\Delta’]$ : d[∆,∆] hoặc d(∆,∆);
            23 Góctrongcácgiátrịlượnggiáckhông dùng\widehat,tứclàchỉgõcosA,sin(AB,DC),...
                           [
               trừ khi gõ sinABC
            24 Gõmặtphẳnghoặcđườngthẳngdùng$(P)\colon ax+by+cz+d=0$:(P): ax+by+cz+d = 0
                                                                  #»      #»
            25 Véc-tơ của mặt phẳng dùng $\overrightarrow{n}_{P}$: nP hoặc n(P)
            26 Đưahìnhvào$\immini{câu dẫn}{code hình}$hoặc$\impicinpar{câu dẫn}{code hình}$
               (khuyến khích dùng $\immini{câu dẫn}{code hình}$).
            27 Bảngbiếnthiênkhôngphảikẻkhungngoài,khinằmriêngphảiđặttrongmôitrườngcenter.
            28 Bảng biến thiên dòng x, y0 và y khai báo như sau:
               \tkzTabInit[nocadre,lgt=1.2,espcl=2.5,deltacl=0.6]%phần bắt buộc.
               {$x$ /0.6,$y’$ /0.6,$y$ /2}%phần bắt buộc
               Trong đó kích thước của dòng x, y0 không được quá cao, từ 0.6 → 1.
            29 Sử dụng $\left(...\right) hay \left[ ...\right]$ cho các khoảng, đoạn.
                           A
            30 Sau lệnh của LT X phải có dấu cách ví dụ: \True $x=2$, $\triangle ABC$.
                             E
            31 Phân số đứng riêng xài \dfrac{A}{B}: A,
                                                 B                      p
                                                                        q
               phân số ở cơ số, số mũ, cận tích phân dùng \frac hoặc \tfrac: Z f(x)dx
                                                                       m
                                                                       n
            32 Gõ các chữ phiên âm: gõ đủ dấu, có gạch ngang ở giữa, ví dụ như mô-đun, véc-tơ, vi-rút,...
            33 Không được lệnh gõ tắt và định nghĩa thêm bất cứ môi trường nào khác ngoài quy định.
            34 Không dùng lệnh \hfill khi bắt đầu gõ bài tập, cứ để mặc định cho đồng nhất giữa các đề
               - Không dùng lệnh \\, \par, \hfill khi bắt đầu soạn lời giải
               - Sau các môi trường enummurate, các lệnh \immini, \impicinpar,...đã tự động xuống
               dòng, thầy cô không gõ thêm lệnh \\,\par,...
                                                   2
                     2. QUY ĐỊNH VỀ TRÌNH BÀY LỜI GIẢI
         1 Các ý nhỏ dùng môi trường liệt kê enumerate phải để mặc định, KHÔNG thêm tham số
           bổ sung \begin{enumerate}[a)]..., (trừ một số trường hợp đặc biệt).
         2 Các ví dụ hoặc bài tập có các ý liệt kê dài, không chia cột (số cột bằng 1) thì phải sử dụng
           môi trường liệt kê enumerate; nếu muốn chia cột (2 cột trở lên) khi sử dụng môi trường
           liệt kê thì soạn theo cấu trúc:
           \begin{listEX}[Số cột]
           \item Ý 1.
           \item Ý 2.
           \end{listEX}
           Các ví dụ:
           \begin{vd}
           Giải các phương trình sau
           \begin{listEX}[2]
           \item $x^2-x+1=0$.
           \item $2x^2-x-3=0$.
           \item $3x^2+5x-8=0$.
           \item $-x^2+x-3=0$.
           \item $-x^2-x+3=0$.
           \item $5x^2-6x+1=0$.
           \end{listEX}
           \end{vd}
           Giải các phương trình sau
             a) x2 −x+1=0.               b) 2x2 −x−3=0.
             c) 3x2 +5x−8=0.             d) −x2 +x−3=0.
             e) −x2 −x+3=0.              f) 5x2 −6x+1=0.
           Ta có $\triangle ABC$ cân tại $A$ \tagEX{1}
           Ta có 4ABC cân tại A                                   (1)
                                     3
            3 Gióng công thức trong môi trường {eqnarray*} và thêm lệnh \allowdisplaybreaks bắt
               buộc để tự động ngắt công thức toán khi sang trang
                                                  f(x) = g(x)
                                              ⇔ f (x)=g (x)
                                                   1     2
                                              ⇔ f (x)=0
                                                   3
               \allowdisplaybreaks
               \begin{eqnarray*}
               & & f(x)=g(x)\\
               &\Leftrightarrow & f_1(x)=g_2(x)\\
               &\Leftrightarrow & f_3(x)=0
               \end{eqnarray*}
                                          
            4 Dấu chấm của hệ phương trình ax+b = y. Đặt sau cùng của hệ nếu nằm trên cùng 1
                                          ay+b=x
               dòng với câu khác và đặt ở phương trình cuối nếu hệ đứng một mình.
                                                    
                                                    
                                         ax+b=y ⇔ ax−y=−b
                                                    
                                         ay +b = x     ay −x=−b.
                                                  4
```
