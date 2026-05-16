# Agent Exam Skills

Bộ skill này giúp agent soạn đề, giải đề, sửa đề, review logic và chuyển bài toán thành generator Python-LaTeX theo đúng phong cách đề đã có sẵn.

Điểm quan trọng nhất: nếu muốn lời giải đúng ý, hãy gửi **ảnh đề** và nếu có thì gửi thêm **ảnh lời giải mẫu**. Ảnh lời giải mẫu có thể là viết tay, đánh máy, ảnh chụp PDF, ảnh chụp vở, hoặc đoạn LaTeX/Python cũ. Agent sẽ dùng ảnh lời giải mẫu để bắt đúng nhịp trình bày, độ chi tiết, cách đặt biến, cách xuống dòng và kiểu giải thích.

## Mục Tiêu

Bộ skill giúp agent:

- Nhận dạng dạng bài từ ảnh đề, mã câu, tên file, folder hoặc nội dung câu hỏi.
- Chọn đúng skill chuyên môn của dạng bài, không đọc lan sang folder khác.
- Luôn đọc skill chung về LaTeX, trình bày lời giải, random, consistency, TikZ và house style.
- Tạo hoặc sửa Python generator sao cho đề bài, đáp án, lời giải và hình vẽ thống nhất.
- Viết lời giải giống người làm thật: có ý tưởng, có lý do, không nhảy cóc phép tính.
- Bám theo lời giải mẫu nếu người dùng gửi ảnh lời giải hoặc bài đã làm trước đó.

## Cấu Trúc Skill

```text
skills/
  python-latex-exam-master/
  python-latex-exam-ds-solver/
  python-latex-exam-gt-solver/
  python-latex-exam-hh-co-dien-solver/
  python-latex-exam-hh-gan-truc-solver/
  python-latex-exam-sp-xac-suat-co-dien-solver/
  python-latex-exam-sp-xac-suat-co-dieu-kien-solver/
```

## Vai Trò Từng Skill

`python-latex-exam-master` là skill chung. Skill này chứa các quy tắc về:

- LaTeX và TikZ.
- Trình bày lời giải.
- Random tham số.
- Kiểm tra tính nhất quán giữa đề, đáp án, lời giải và hình vẽ.
- Cách dùng helper như `tinh_latex`, `lam_tron`, `kiem_tra_lam_tron`.
- Xử lý feedback, ảnh lời giải mẫu và giữ đúng house style.

`python-latex-exam-ds-solver` dùng cho DS/đại số:

- Bất phương trình logarit.
- Điều kiện xác định.
- Dãy số.
- Miền nghiệm, quy hoạch tuyến tính.
- Bài toán tài chính, lãi suất, đầu tư.

`python-latex-exam-gt-solver` dùng cho GT/giải tích:

- Hàm số, đạo hàm, cực trị, đơn điệu.
- Bảng biến thiên.
- Tích phân.
- Logarit, mũ, tăng trưởng/suy giảm.
- Tối ưu hóa, kinh tế, chuyển động, diện tích/thể tích.

`python-latex-exam-hh-co-dien-solver` dùng cho hình học cổ điển:

- Hình chóp, lăng trụ, tứ diện.
- Hình chiếu, điểm phụ, tỉ số đoạn.
- Cấu trúc hình học tổng hợp không gắn trục tọa độ.

`python-latex-exam-hh-gan-truc-solver` dùng cho hình học gắn trục/Oxyz:

- Hệ trục tọa độ.
- Vector, điểm, đường thẳng, mặt phẳng, mặt cầu.
- Khoảng cách, góc, mô hình 3D thực tế.
- Tối ưu hóa hoặc bài toán có ràng buộc trong Oxyz.

`python-latex-exam-sp-xac-suat-co-dien-solver` dùng cho xác suất cổ điển:

- Không gian mẫu hữu hạn.
- Đếm số trường hợp.
- Biến cố đối, giao, hợp, bổ sung.
- Độc lập, phép thử lặp, phân số rút gọn.

`python-latex-exam-sp-xac-suat-co-dieu-kien-solver` dùng cho xác suất có điều kiện:

- `P(A|B)`.
- Công thức xác suất toàn phần.
- Bayes.
- Cây xác suất.
- Xét nghiệm, chẩn đoán, độ nhạy, độ đặc hiệu, dương tính giả.
- Rút không hoàn lại và đếm có điều kiện.

## Workflow Làm Việc

Khi nhận một yêu cầu, agent nên làm theo thứ tự:

1. Trước khi dùng skill, `cd` vào đúng folder tên/project đang chứa `.agents`, ví dụ folder `ThanhDanh`; nếu mở agent ở thư mục khác thì agent có thể không thấy skill.
2. Đọc `python-latex-exam-master`.
3. Nhận dạng dạng bài từ ảnh đề, mã câu, tên file, folder hoặc từ khóa trong đề.
4. Chọn đúng một skill solver tương ứng.
5. Đọc reference trong folder solver đó, chỉ đọc đúng file MC/TF/SA cần thiết.
6. Nếu có ảnh lời giải mẫu, phân tích cách trình bày trước khi viết lời giải mới.
7. Khóa model toán học, đơn vị, miền giá trị, cách làm tròn và format output.
8. Viết hoặc sửa code Python generator.
9. Sinh đề, đáp án, lời giải từ cùng một bộ biến.
10. Kiểm tra logic, random guardrails, LaTeX, TikZ, đáp án và lời giải.
11. Nếu có thể, chạy generator và inspect file `.tex` sinh ra.

## Cập Nhật Skill Sau Mỗi Lần Sửa Câu Hoặc Phản Biện

Sau mỗi lần sửa một câu, phản biện lời giải, sửa generator, hoặc xử lý một lỗi mới, nên cập nhật lại bộ skill để lần sau agent không lặp lại lỗi cũ.

Quy trình chuẩn:

1. Sau khi sửa xong câu hiện tại, yêu cầu agent đang dùng rút kinh nghiệm thành một file `.md`.
2. File kinh nghiệm nên ghi rõ dạng bài, mã câu, lỗi ban đầu, cách phát hiện lỗi, cách sửa đúng, guardrail cần thêm, và kiểu trình bày nên giữ.
3. Đặt file `.md` tạm ở nơi dễ tìm, ví dụ `tmp-experience/`, `kinh-nghiem-moi/`, hoặc gửi trực tiếp nội dung file đó cho agent cập nhật skill.
4. Mở agent ở đúng project, `cd` vào folder tên/project đang chứa `.agents`, ví dụ folder `ThanhDanh`.
5. Trong ô prompt của agent, gõ `/` để mở danh sách skill rồi chọn `skill-creator`.
6. Gửi kèm file `kinhnghiem.md` hoặc dán nội dung file kinh nghiệm vào prompt.
7. Yêu cầu `skill-creator` kết hợp kinh nghiệm mới với skill liên quan tới bài hiện tại.
8. Nếu kinh nghiệm là thuật toán, công thức, lỗi tư duy, dạng distractor, hoặc cách giải riêng của một dạng bài, cập nhật reference trong folder skill solver đúng dạng.
9. Nếu kinh nghiệm là quy tắc chung về trình bày, LaTeX/TikZ, format, random, helper, house style, cách đọc ảnh lời giải mẫu, hoặc guardrail dùng được cho nhiều dạng bài, có thể cập nhật `python-latex-exam-master`.
10. Nếu chưa có skill nào liên quan, tạo skill mới đúng chỗ theo dạng bài; chỉ cập nhật master khi kinh nghiệm đó thật sự là mặc định chung, không chỉ riêng một bài.
11. Sau khi agent cập nhật xong, phải tự đọc review lại các file đã sửa để kiểm tra cập nhật có đúng chỗ và viết hợp lí không.
12. Nếu agent cập nhật sai folder, nhét kinh nghiệm chuyên môn quá riêng vào master, viết quá chung chung, trùng lặp, hoặc làm mất rule cũ, phải yêu cầu sửa lại ngay.
13. Sau khi review ổn, chạy validator cho skill vừa sửa hoặc skill vừa tạo.
14. Nếu skill dùng chung trong nhiều project, đồng bộ lại vào repo `.agents/skills` và push lên GitHub.

File kinh nghiệm `.md` nên có cấu trúc ngắn gọn:

```text
# Kinh nghiệm từ câu <mã câu>

## Dạng bài
Ví dụ: GT/SA, HH/Oxyz/TF, SP/xác suất có điều kiện/SA.

## Lỗi hoặc điểm khó
Mô tả lỗi logic, lỗi trình bày, lỗi random, lỗi LaTeX, hoặc điểm dễ nhầm.

## Cách xử lý đúng
Ghi thuật toán giải, công thức chính, điều kiện cần kiểm tra, và cách sửa generator.

## Trình bày cần giữ
Ghi cách đặt biến, thứ tự dòng, cách xuống dòng, cách kết luận, hoặc style từ ảnh lời giải mẫu.

## Guardrail cần thêm
Ghi các điều kiện random hoặc kiểm tra để lỗi không lặp lại.
```

Nguyên tắc chọn nơi cập nhật:

- Kinh nghiệm về LaTeX, TikZ, format, random, helper, house style chung: cập nhật `python-latex-exam-master`.
- Kinh nghiệm DS: cập nhật `python-latex-exam-ds-solver/references`.
- Kinh nghiệm GT: cập nhật `python-latex-exam-gt-solver/references`.
- Kinh nghiệm HH cổ điển: cập nhật `python-latex-exam-hh-co-dien-solver/references`.
- Kinh nghiệm HH gắn trục/Oxyz: cập nhật `python-latex-exam-hh-gan-truc-solver/references`.
- Kinh nghiệm xác suất cổ điển: cập nhật `python-latex-exam-sp-xac-suat-co-dien-solver/references`.
- Kinh nghiệm xác suất có điều kiện: cập nhật `python-latex-exam-sp-xac-suat-co-dieu-kien-solver/references`.

Có thể cập nhật `python-latex-exam-master` khi kinh nghiệm là mặc định chung áp dụng cho nhiều dạng, ví dụ trình bày lời giải, cách bám ảnh lời giải mẫu, random, LaTeX/TikZ, helper, format đáp án, validate hoặc guardrail chung. Không đưa kinh nghiệm chuyên môn của một dạng bài vào master nếu nó chỉ áp dụng cho một dạng cụ thể. Master giữ luật chung; solver giữ kinh nghiệm giải bài.

Prompt mẫu để cập nhật skill sau khi sửa câu:

```text
Trước tiên cd vào folder project/tên mình, ví dụ:
cd <duong-dan-project>\ThanhDanh

Sau đó trong prompt gõ "/" và chọn skill-creator.

Gửi kèm file kinh nghiệm: kinhnghiem.md

Hãy đọc file kinh nghiệm mới này và cập nhật skill liên quan.
Bài hiện tại thuộc dạng: <DS/GT/HH/SP>/<MC/TF/SA>.
Nếu kinh nghiệm là chuyên môn của dạng bài thì cập nhật reference trong folder skill solver đúng dạng.
Nếu kinh nghiệm là rule chung về LaTeX, trình bày, random, helper, house style, ảnh lời giải mẫu hoặc guardrail dùng cho nhiều dạng thì có thể cập nhật python-latex-exam-master.
Nếu chưa có skill liên quan thì tạo skill mới đúng chỗ theo dạng bài; không tạo hoặc sửa master chỉ vì một kinh nghiệm quá riêng của một bài.
Sau khi cập nhật hãy validate lại skill.

Sau khi cập nhật xong, hãy liệt kê rõ:
- Đã sửa file nào.
- Vì sao sửa đúng skill đó.
- Có đụng tới master không, nếu có thì vì sao.
- Validator đã chạy cho skill nào.

Mình sẽ tự đọc review lại nội dung skill sau đó, nên đừng chỉ báo "xong"; hãy cho đường dẫn file đã sửa để kiểm tra.
```

## Input Nên Gửi

Input tốt nhất nên có:

- Ảnh đề bài.
- Ảnh lời giải mẫu hoặc lời giải mong muốn, nếu có.
- Mã câu, ví dụ `DS...MC`, `GT...TF`, `HH...SA`, `SP...TF`.
- Folder dạng bài, ví dụ `old_file_new/GT/MC`.
- File Python cần sửa, nếu đang sửa code.
- Dạng output: MC, TF, SA.
- Quy tắc làm tròn, đơn vị, số mẫu cần random.
- Yêu cầu random cụ thể, ví dụ số nào trên đề được random, số nào phải giữ cố định, random trong khoảng nào, cần số nguyên hay phân số, cần đáp án đẹp hay có làm tròn.
- Yêu cầu riêng khác, ví dụ giữ nguyên cách đặt biến, bắt buộc dùng một công thức, không đổi hình, không thêm bước giải, hoặc phải bám đúng ảnh lời giải mẫu.
- Feedback của giáo viên hoặc lỗi cần phản biện.

Nếu chỉ có ảnh đề, agent vẫn có thể tự nhận dạng dạng bài. Nhưng nếu cần lời giải đúng phong cách của bạn, nên gửi thêm ảnh lời giải mẫu.

Nếu người dùng không nói rõ random số nào hoặc yêu cầu riêng nào, agent sẽ tự chọn cách random theo skill, dùng guardrail hiện có để giữ đề hợp lí, đáp án đúng, phương án không trùng và lời giải dễ đọc.

## Cách Prompt Nên Dùng

Ví dụ tạo generator từ ảnh đề và ảnh lời giải:

```text
Trước khi prompt, cd vào folder project/tên mình đang chứa .agents, ví dụ:
cd <duong-dan-project>\ThanhDanh

Hãy tạo generator Python-LaTeX cho câu này.
Dạng: GT/MC.
Mã câu: GT254MC012.
Input gồm ảnh đề và ảnh lời giải mẫu.
Yêu cầu: bám cách trình bày trong ảnh lời giải, random hợp lí, đáp án không trùng.
```

Ví dụ có yêu cầu random cụ thể:

```text
Hãy tạo generator Python-LaTeX cho câu này.
Dạng: HH/Oxyz/SA.
Mã câu: HH254SA012.
Random các tọa độ điểm A, B, C nhưng giữ chiều cao là số nguyên từ 3 đến 8.
Khoảng cách cuối cùng làm tròn đến 1 chữ số thập phân.
Không đổi cách trình bày lời giải trong ảnh mẫu.
Nếu yêu cầu nào chưa nói rõ thì tự xử lí theo skill.
```

Ví dụ sửa một file có lỗi logic:

```text
Hãy sửa file SP234TF040.py.
Dạng: SP/xác suất có điều kiện/TF.
Lỗi hiện tại: câu d nhầm P(A|B) với P(B|A).
Hãy sửa logic, đáp án và lời giải cho đúng.
```

Ví dụ chỉ gửi ảnh:

```text
Gửi kèm ảnh đề.
Hãy giải câu trong ảnh và tạo generator Python-LaTeX theo đúng style skill.
Nếu chưa rõ dạng bài, hãy tự nhận dạng từ nội dung đề.
```

Ví dụ phản biện lời giải:

```text
Gửi kèm ảnh đề và ảnh lời giải học sinh/AI.
Hãy phản biện lời giải này: kiểm tra logic, phép tính, cách trình bày, LaTeX và kết luận cuối.
Nếu sai, hãy chỉ ra lỗi và viết lại lời giải đúng theo style đề.
```

## Output Mong Đợi

Tùy yêu cầu, agent có thể trả ra:

- File Python generator đã tạo/sửa.
- Lời giải LaTeX theo đúng style mẫu.
- Đáp án và giải thích vì sao đúng.
- Các guardrail random đã thêm.
- Các lỗi logic/LaTeX đã sửa.
- Nhận xét phản biện nếu lời giải chưa chuẩn.
- Kết quả validate/chạy test nếu có.

Output tốt cần đảm bảo:

- Đề bài, đáp án, lời giải và hình vẽ dùng cùng một bộ biến.
- Không lệch đơn vị, miền xác định, điều kiện hoặc giả thiết.
- Các phương án sai trong MC không trùng đáp án sau khi format.
- Các mệnh đề TF có độ khó tương đương, không sai quá lộ.
- SA có đáp án cuối đúng format và đúng quy tắc làm tròn.
- Lời giải đọc được, có ý tưởng và có lý do, không chỉ là tính nháp.
- Nếu có ảnh lời giải mẫu, lời giải mới phải bám phong cách đó trừ khi mẫu sai.

## Nguyên Tắc Quan Trọng

- Master là mặc định chung, solver là chuyên môn từng dạng.
- Mỗi lần làm bài nên dùng đúng một solver chính, tránh đọc nhiều folder không liên quan.
- Nếu dạng bài chưa có reference mẫu, không tự giả vờ như đã có kinh nghiệm cũ.
- Nếu đề bài thực tế cho ra giá trị phi thực tế, phải thêm guardrail random hoặc sửa mô hình.
- Nếu sửa layout, phải inspect `.tex` sinh ra, không chỉ nhìn code Python.
- Nếu ảnh lời giải mẫu có lỗi, phải nói rõ lỗi trước rồi mới viết lại lời giải đúng.
