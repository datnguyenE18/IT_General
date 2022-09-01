- **Secure coding for developers: <https://viblo.asia/s/secure-coding-for-developers-dbZN76EalYM>**
</br>

- Phải luôn luôn kiểm tra quyền của người dùng mỗi khi người dùng thực hiện 1 chức năng và tương tác với dữ liệu trên hệ thống
</br>

- Đảm bảo mọi thông tin nhạy cảm của người dùng phải được mã hóa bằng các thuật toán mã hóa mạnh như SHA256, SHA512,… các thông tin nhạy cảm như tài khoản, mật khẩu, stk ngân hàng  
</br>

- Luôn tuân thủ quy tắc không bao giờ truyền thông tin hệ thống trên URL
</br>

- Luôn sử dụng phương pháp tạo white list các ký tự đầu vào, xử lý mã hóa các ký tự đặc biệt nếu cần thiết
</br>

- Luôn sử dụng phương pháp tạo white list các ký tự đầu vào
</br>

- Lập trình viên cần xử lý phiên session của người dùng theo session lưu trong cookie, giá trị người dùng gửi lên thông qua session, lập trình viên đối chiếu phiên của người dùng với thông tin trên server để xác định người dùng đã đăng nhập chưa? Người dùng là ai? Có quyền gì
</br>

- Không trust dữ liệu người dùng nhập vào
</br>

- Luôn kiểm tra định dạng file, cấu trúc, mime type, Nội dung file khi thực hiện thao tác với file
</br>

- Với phân quyền, phải kiểm tra đủ phân quyền theo chức năng và phân quyền theo dữ liệu. Kiểm tra phần quyền giữa ngừoi dùng cùng cấp quyền và người dùng cấp trên- cấp dưới
</br>

- Javascript chỉ thực thi dưới trình duyệt ngừoi dùng, người dùng có thể by pass được nên phải kiểm tra input người dùng ở cả 2 phía để tránh các lỗi ATTT
</br>

- Việc kiểm tra dữ liệu đầu vào ngừoi dùng phải được thực hiện ở cả 2 phía server và client, luôn sử dụng white list vì blacklist không thể xử lý được tất cả các trường hợp
