# IT_General

- **5 mảng nội dung:**
  - 1. Kiến thức chung về phát triển phần mềm
  - 2. Kiến thức lập trình cơ bản
  - 3. CI/CD
  - 4. Hệ điều hành
  - 5. An toàn thông tin

- **Interviews:**

  - Git, SQL, Data Struct
  - Database: Cách tạo bảng, Oracle, MongoDB, các cách đánh index mongoDB, truy vấn, so sánh Truncate và delete, ALERT có ý nghĩa gì…
  - Quản lý mã nguồn: Hỏi về mã nguồn phân tán git, các câu lệnh git, git add m, git reset -- hard, ... một chút về các công cụ vận hành Jenkins, DI/OS, docker, đệ quy, thuật toán sắp xếp…
  - Cấu trúc dữ liệu: Cây nhị phân, thêm sửa xóa node, cách duyệt, dựng cây,
  - Front – end (web): Html, css, js, jquery
  - Địa chỉ IP, hệ điều hành linux, trình duyệt web...

***

**1. Kiến thức chung về phát triển phần mềm:**

\-        Kiến thức về unit test/acceptance test, test hồi quy/ Mô hình phát triển tăng trưởng (Incremental Development Model)/ Quản lý rủi ro trong phát triển phần mềm/ Đặc trưng của kho dữ liệu.

\-        Quy trình phát triển phần mềm Agile/Waterfall/ Agile – Scrum.

\-        Quy trình phát triển phần mềm - mô hình - Kiểm thử/ Tài liệu SRS/ mô hình waterfall/ unit test/ Water fall/ Iteration Model.

\-        Hệ điều hành - Windows – Network

\-        ATTT - Lỗi SQL Injection, XSS…

***

**2. Kiến thức lập trình cơ bản.**

\-        Cơ sở dữ liệu: WHERE, SUM/ SQL (Oracle) - DECODE- ROLLBACK - SQL – DDL - DCL, - DML - AVG - COUNT - ROWNUM - CONNECT BY PRIOR - SUM, GROUP BY - PROCEDURE - LPAD, CONNECT BY PRIOR - FOREIGN KEY - COUNT – JOIN - NVL, DECODE - GROUP BY / Index - Oracle – Procedure - Function - Connection Pool - Tối ưu - Insert table - Update, nested select - Session management - Group by, having /AS - PRIMARY KEY – ROWNUM/ Kiểu dữ liệu/ Thao tác dữ liệu lớn - Tối ưu - kiến trúc/ Khóa ngoài/ Function/ NoSQL/ Index/ Trigger/ Kiến trúc/ Constraint/ ALTER/ TRUNCATE/ ALTER TABLE/ Khóa/ HAVING/ WHERE/ MySQL -  USE/ Linear Search/ Bubble Sort/ Selection Sort/ List/ Array/ LinkedList/ Stack/ Doubly Linked List/ Binary Search/ Linear Search/ AJAX/ JS/ HTML/ HP – state/ PHP – function/ DELETE/ DROP/ INSERT/ IN,OR/ LIKE + regex/ Subquery/ SELECT/ JOIN/ BETWEEN/ ALL, subquery/ CREATE/ PRIMARY KEY/ MySQl – backup/ sum, having, order/ count, group by AVG/ JOIN/ LEFT JOIN/ OR, AND, NOT/ DISTINCT, UNIQUE/ Phép chiếu/ ORDER BY, HAVING.

\-        Hệ quản trị cơ sở dữ liệu/ Kiểu dữ liệu/ Cấu trúc dữ liệu danh sách tuyến tính/ Các kiểu dữ liệu cơ bản/ Khái niệm cấu trúc dữ liệu và giải thuật/ Sơ đồ Collaboration Diagram, State Diagram...Số lượng mã màu trong HTML/ Các thẻ và mệnh đề thực thi trong HTML/ Cấu trúc của HTML, DOM/ Cấu trúc bộ nhớ ứng dụng java trên JVM/ Mảng 2 chiều/ Khai báo mảng/ Danh sách liên kết/ Giải thuật Algorithm Complexity (độ phức tạp của giải thuật)/ Mảng 1 chiều/

\-        Kiến thức về khóa chính, khóa ngoại trong CSDL quan hệ/ Các loại câu lệnh join trong ngôn ngữ SQL/ Biểu thức union, union all trong SQL/ Mệnh đề distinct trong SQL/ Order by xắp xếp theo thứ tự tăng dần, giảm dần trong SQL.

\-        Viết tắt của một số thuật ngữ: SQL, DML, DDL…/ Từ khóa Like trong SQL/ Khái niệm index trong SQL/ Hàm tổng hợp trong SQL như Count, Sum, ABS…/ Hàm decode, translate trong SQL/ Hàm làm tròn trong SQL (Round, floor...)/ Thao tác với sequence trong sql (.nextval, .currval...)

\-        Các lệnh cơ bản SQL: cú pháp của câu lệnh như select, insert,  delete, update/ insert into ; truy vấn có sử dụng hàm tính toán, tổng hợp như: AVG, COUNT, SUM, DISTINCT…/ Lệnh query thao tác (format,  lấy ngày giờ phút giây...) với datatime

**Ví dụ:**

Cho bảng khach\_hang có dữ liệu như sau:

ID |ten\_khach\_hang |tuoi| dia\_chi

1 |Nguyễn Thị Ngoan |20|Ha Dong

2 |Hoàng Văn Sơn |21|Hoàng Mai

3 |Phạm Thị Hương |20|Ha Dong

Tính tuổi trung bình của các khách hàng có địa chỉ ở Ha Dong

**Ví dụ 2:**

Cho thuật toán tìm nhị phân không đệ quy sau

```sh
int NRecBinarySearch (int M[], int N, int X)
{ int First = 0;
int Last = N – 1;
while (First <= Last)
{
int Mid = (First + Last)/2;
if (X == M[Mid])
return(Mid);
if (X < M[Mid])
Last = Mid – 1;
else
First = Mid + 1;
}
return(-1);
}
```

Chọn câu đúng nhất trong trường hợp tốt nhất khi phần tử ở giữa của mảng có giá trị bằng X

***

**3. CI/CD.**

\-        Quy trình Agile - CI/CD

\-        CI/CD - mục đích - công cụ - quy trình/ pipeline/ auto test/ quản lý mã nguồn/ deploy/ DevOps -  Docker – Git/ cloud service.

**Ví dụ:** nói về CI trong Agile

- ưu điểm của DevOps

- Trong CICD, Git được sử dụng làm gì?

***

**4. Hệ điều hành.**

\-        Hệ điều hành – Process Linux

**Ví dụ:** Trạng thái BLOCKED của một process?

- HĐH sẽ thực thi một process mới sinh ra?

- Hệ thống Linux có mấy Run Level chính?

***

**5. An toàn thông tin.**

\-        Đọc các nguyên tắc mã hóa mật khẩu người dùng/ Các nguyên tắc kiểm tra đuôi file, mime type khi người dùng upload file/ Phương án xử lý ngắt phiên làm việc hiện tại của người dùng hiện tại/ Các nguyên tắc sử dụng internet an toàn ngoài công cộng/ Tài liệu liên quan xử lý XML/ Tài liệu xử lý an toàn cho session ID/ Tiêu chuẩn về các thông tin được ghi trong log hệ thống phần mềm/ Tài liệu Phân tích thiết kế hệ thống, module phân quyền và quản trị người dùng/ Cách phòng chống SQL Injection/ Cách kiểm tra, lọc dữ liệu đầu vào người dùng trong hệ thống, chú ý phải kiểm tra đầy đủ 2 phía tránh kẻ tấn công có thể sử dụng các kiểu mã hóa, ký tự đặc biệt để bypass / Đọc các tài liệu liên quan đến phân quyền người dùng/ Tài liệu tham khảo chống CSRF/ Các tài liệu về tương tác với file trong lập trình an toàn. Luôn luôn kiểm tra các thuộc tính của file

\-        Phải luôn luôn kiểm tra quyền của người dùng mỗi khi người dùng thực hiện 1 chức năng và tương tác với dữ liệu trên hệ thống/ Đảm bảo mọi thông tin nhạy cảm của ngừoi dùng phải được mã hóa bằng các thuật toán mã hóa mạnh như SHA256, SHA512,… các thông tin nhạy cảm như tài khoản, mật khẩu, stk ngân hàng / Luôn tuân thủ quy tắc không bao giờ truyền thông tin hệ thống trên URL/ Tìm hiểu các quy tắc sinh token người dùng/

\-        Luôn sử dụng phương pháp tạo white list các ký tự đầu vào, xử lý mã hóa các ký tự đặc biệt nếu cần thiết/ Luôn sử dụng phương pháp tạo white list các ký tự đầu vào/ Lập trình viên cần xử lý phiên session của người dùng theo session lưu trong cookie, giá trị người dùng gửi lên thông qua session, lập trình viên đối chiếu phiên của người dùng với thông tin trên server để xác định người dùng đã đăng nhập chưa? Người dùng là ai? Có quyền gì…/ Không trust dữ liệu người dùng nhập vào/ Luôn kiểm tra định dạng file, cấu trúc, mime type, Nội dung file khi thực hiện thao tác với file/ Với phân quyền, phải kiểm tra đủ phân quyền theo chức năng và phân quyền theo dữ liệu. Kiểm tra phần quyền giữa ngừoi dùng cùng cấp quyền và người dùng cấp trên- cấp dưới/ Javascript chỉ thực thi dưới trình duyệt ngừoi dùng, người dùng có thể by pass được nên phải kiểm tra input người dùng ở cả 2 phía để tránh các lỗi ATTT/ Việc kiểm tra dữ liệu đầu vào ngừoi dùng phải được thực hiện ở cả 2 phía server và client, luôn sử dụng white list vì blacklist không thể xử lý được tất cả các trường hợp

\-        Tham khảo các cách phòng chống SQL Injection/ Tham khảo các cơ chế về việc chống bruteforce tài khoản/mật khẩu người dùng/ <https://mailtrap.io/blog/reset-password-email/> Các tham số trong request có thể bị ghi đè nếu được truyền nhiều lần. Ví dụ <https://site?x=abc&y=def&x=kh> thì param x sẽ bị ghi đè thành x=kh/ Tham khảo các thêm salt vào trước khi mã hóa

