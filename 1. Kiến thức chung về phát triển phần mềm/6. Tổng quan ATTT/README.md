# Tổng quan ATTT

- [Tổng quan ATTT](#tổng-quan-attt)
  - [Các yêu cầu đảm bảo ATTT và an toàn HTTT](#các-yêu-cầu-đảm-bảo-attt-và-an-toàn-httt)
  - [Các dạng lỗ hổng bảo mật](#các-dạng-lỗ-hổng-bảo-mật)
  - [Các dạng tấn công](#các-dạng-tấn-công)

## Các yêu cầu đảm bảo ATTT và an toàn HTTT

- **Tính bí mật (Confidentiality):** chỉ người dùng có thẩm quyền mới được truy nhập thông tin.
</br>

- **Tính toàn vẹn (Integrity):** thông tin chỉ có thể được sửa đổi bởi những người dùng có thẩm quyền.
  - Kẻ tấn công có thể lợi dụng điểm yếu an ninh để lặng lẽ sửa đổi thông tin/hệ thống --> phá vỡ tính toàn vẹn;

  - Một điểm yếu trong hệ thống có thể cho phép một người dùng bình thường thay đổi quyền truy nhập đến mọi file tương tự người quản trị.
</br>

- **Tính sẵn dùng (Availability):** thông tin có thể truy nhập bởi người dùng hợp pháp bất cứ khi nào họ có yêu cầu.

***

## Các dạng lỗ hổng bảo mật

- **Lỗi tràn bộ đệm (buffer overflows)**
  - Khi một ứng dụng cố gắng ghi dữ liệu vượt khỏi phạm vi bộ đệm (giới hạn cuối hoặc cả giới hạn đầu của bộ đệm);

  - Lỗi tràn bộ đệm có thể khiến ứng dụng ngừng hoạt động, gây mất dữ liệu hoặc thậm chí giúp kẻ tấn công kiểm soát hệ thống;

  - Lỗi tràn bộ đệm là lỗi trong khâu lập trình phần mềm 
</br>

- **Không kiểm tra đầu vào (unvalidated input)**
  - Các dữ liệu đầu vào (input data) cần được kiểm tra để đảm bảo đạt các yêu cầu về định dạng và kích thước;
    </br>

  - Các dạng dữ liệu nhập điển hình cần kiểm tra:
    - Các trường dữ liệu text
    - Các lệnh được truyền qua URL để kích hoạt chương trình
    - Các file âm thanh, hình ảnh, hoặc đồ họa do người dùng hoặc các tiến trình khác cung cấp
    - Các đối số đầu vào trong dòng lệnh
    - Các dữ liệu từ mạng hoặc các nguồn không tin cậy
    </br>
  - Kẻ tấn công có thể kiểm tra các dữ liệu đầu vào và thử tất cả các khả năng có thể để khai thác.

- **Các vấn đề với điều khiển truy cập (access control problems)**
  - Điều khiển truy nhập có thể được thiết lập bởi hệ điều hành hoặc mỗi ứng dụng, thường gồm 2 bước:
    - Xác thực (Authentication): xác thực thông tin nhận dạng của chủ thể;
    - Trao quyền (Authorization): cấp quyền truy nhập cho chủ thể sau khi thông tin nhận dạng được xác thực.
    </br>

  - Nếu kiểm soát truy nhập bị lỗi, một người dùng bình thường có thể đoạt quyền của người quản trị và toàn quyền truy nhập vào hệ thống;
    </br>

  - Một kẻ tấn công có thể lợi dụng lỗ hổng bảo mật của hệ thống kiểm soát truy nhập để truy nhập vào các file trong hệ thống.

- **Các điểm yếu trong xác thực, trao quyền hoặc các hệ mật mã (weaknesses in authentication, authorization, or cryptographic practices)**
  - Xác thực:
    - Mật khẩu được lưu dưới dạng rõ (plain text) à nguy cơ bị lộ mật khẩu rất cao trong quá truyền thông tin xác thực;
    - Sử dụng mật khẩu đơn giản, dễ đoán, hoặc dùng mật khẩu trong thời gian dài;
    - Sử dụng cơ chế xác thực không đủ mạnh: ví dụ các cơ chế xác thực của giao thức HTTP.
</br>

  - Trao quyền:
    - Cơ chế thực hiện trao quyền không đủ mạnh, dễ bị vượt qua;
    - Ví dụ: một trang web chỉ thực hiện ẩn các links đến các trang web mà người dùng không được truy nhập mà không thực sự kiểm tra quyền truy nhập trên từng trang. Nếu người dùng tự gõ URL của trang thì vẫn có thể truy nhập.
</br>

- **Các lỗ hổng bảo mật khác.**

***

## Các dạng tấn công

- **Tấn công mật khẩu:**
  - Tên người dùng và mật khẩu có thể bị đánh cắp thông qua các dạng tấn công XSS hoặc Social Engineering (lừa đảo, bẫy người dùng cung cấp thông tin):
    </br>

    - Cross Site Scripting (XSS) là một trong những tấn công phổ biến và dễ bị tấn công nhất mà tất cả các Tester có kinh nghiệm đều biết đến. Tấn công Cross Site Scripting nghĩa là gửi và chèn lệnh và script độc hại, những mã độc này thường được viết với ngôn ngữ lập trình phía client như Javascript, HTML, VBScript, Flash… Tuy nhiên, cách tấn công này thông thường sử dụng Javascript và HTML
    </br>

    - Những hình thức tấn công chính của Cross Site Scripting:
      - Cross Site Scripting có thể xảy ra trên tập lệnh độc hại được thực hiện ở phía client.
      - Trang web hoặc form giả mạo được hiển thị cho người dùng (nơi nạn nhân nhập thông tin đăng nhập hoặc nhấp vào liên kết độc hại).
      - Trên các trang web có quảng cáo được hiển thị.
      - Email độc hại được gửi đến nạn nhân. Tấn công xảy ra khi tin tặc tìm kiếm những lỗ hổng trên website và gửi nó làm đầu vào độc hại. Tập lệnh độc hại được tiêm vào mã lệnh và sau đó được gửi dưới dạng đầu ra cho người dùng cuối cùng.
    </br>

  - Các dạng tấn công mật khẩu:

    ![image](https://user-images.githubusercontent.com/43572616/187743752-11e74643-3f93-48ae-bbb4-4dcf9715fbf7.png)

***

- **Tấn công bằng mã độc:**
  - Lợi dụng lỗi không kiểm tra đầu vào SQL Injection:
    - SQL Injection (chèn mã độc SQL) là một kỹ thuật cho phép kẻ tấn công chèn mã SQL vào dữ liệu gửi đến máy chủ và được thực hiện trên máy chủ CSDL;
    </br>

  - **Một số cách thức SQL injection khác:**

    Ngoài ví dụ về vượt qua xác thực người dùng thì kẻ tấn công cũng còn có thể đánh cắp dữ liệu trong cơ sở dữ liệu thông qua một số bước như sau:

    - **1. Tìm lỗ hổng chèn mã SQL và thăm dò các thông tin về hệ quản trị cơ sở dữ liệu:**
      - Nhập một số dữ liệu mẫu (như dấu --) hoặc dùng các tool hỗ trợ quét để kiểm tra một trang web có chứa lỗ hổng chèn mã SQL

      - Tìm phiên bản máy chủ cơ sở dữ liệu: nhập các câu lệnh lỗi và kiểm tra thông báo lỗi, hoặc sử dụng @@version (với MS-SQL Server), hoặc version() (với MySQL) trong câu lệnh ghép với UNION SELECT.
    </br>

    - **2. Tìm thông tin về số lượng và kiểu dữ liệu các trường của câu truy vấn hiện tại của trang web.**
      - Sử dụng mệnh đề ORDER BY <số thứ tự của trường>
      - Sử dụng UNION SELECT 1, 2, 3, …
    </br>

    - **3. Trích xuất thông tin về các bảng, các trường của cơ sở dữ liệu thông qua các bảng hệ thống (metadata).**
    </br>

    - **4. Sử dụng lệnh UNION SELECT để ghép các thông tin định trích xuất vào câu truy vấn hiện tại của ứng dụng.**
    </br>

  - **Phòng chống**

    Do tính chất nguy hiểm của tấn công chèn mã SQL, nhiều giải pháp đã được đề xuất nhằm hạn chế tác hại và ngăn chặn triệt để dạng tấn công này. Nhìn chung, cần áp dụng kết hợp các biện pháp phòng chống tấn công chèn mã SQL để đảm bảo an toàn cho hệ thống. Các biện pháp, kỹ thuật cụ thể có thể áp dụng gồm:

    - **1. Các biện pháp phòng chống dựa trên kiểm tra và lọc dữ liệu đầu vào:**
      - Kiểm tra tất cả các dữ liệu đầu vào, đặc biệt dữ liệu nhập từ người dùng và từ các nguồn không tin cậy;
      - Kiểm tra kích thước và định dạng dữ liệu đầu vào;
      - Tạo các bộ lọc để lọc bỏ các ký tự đặc biệt (như \*, ‘, =, --) và các từ khóa của ngôn ngữ SQL (SELECT, INSERT, UPDATE, DELETE, DROP,....) mà kẻ tấn công có thể sử dụng;
    </br>

    - **2. Sử dụng thủ tục cơ sở dữ liệu (stored procedures) và cơ chế tham số hóa dữ liệu:**
      - Đưa tất cả các câu truy vấn (SELECT) và cập nhật, sửa, xóa dữ liệu (INSERT, UPDATE, DELETE) vào các thủ tục. Dữ liệu truyền vào thủ tục thông qua các tham số, giúp tách dữ liệu khỏi mã lệnh SQL, nhờ đó hạn ngăn chặn hiệu quả tấn công chèn mã SQL;
      - Hạn chế thực hiện các câu lệnh SQL động trong thủ tục;
      - Sử dụng cơ chế tham số hóa dữ liệu hỗ trợ bởi nhiều ngôn ngữ lập trình web như ASP.NET, PHP và JSP.
    </br>

    - **3. Các biện pháp phòng chống dựa trên thiết lập quyền truy nhập người dùng cơ sở dữ liệu:**
      - Không sử dụng người dùng có quyền quản trị hệ thống hoặc quản trị cơ sở dữ liệu làm người dùng truy cập dữ liệu. Ví dụ: không dùng người dùng sa (Microsoft SQL) hoặc root (MySQL) làm người dùng truy cập dữ liệu. Chỉ dùng các người dùng này cho mục đích quản trị.
      - Chia nhóm người dùng, chỉ cấp quyền vừa đủ để truy cập các bảng biểu, thực hiện câu truy vấn và chạy các thủ tục.
      - Tốt nhất, không cấp quyền thực hiện các câu truy vấn, cập nhật, sửa, xóa trực tiếp trên các bảng dữ liệu. Thủ tục hóa tất cả các câu lệnh và chỉ cấp quyền thực hiện thủ tục.
      - Cấm hoặc vô hiệu hóa (disable) việc thực hiện các thủ tục hệ thống (các thủ tục cơ sở dữ liệu có sẵn) cho phép can thiệp vào hệ quản trị cơ sở dữ liệu và hệ điều hành nền.
      - Sử dụng các công cụ rà quét lỗ hổng chèn mã SQL, như SQLMap, hoặc Acunetix Vulnerability Scanner để chủ động rà quét, tìm các lỗ hổng chèn mã SQL và có biện pháp khắc phục phù hợp.
