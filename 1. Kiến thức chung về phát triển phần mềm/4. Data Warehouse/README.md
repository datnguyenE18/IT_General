# Kho dữ liệu

- Data warehouse hay Kho dữ liệu là một loại hệ thống quản lý dữ liệu được thiết kế để kích hoạt và hỗ trợ các hoạt động kinh doanh thông minh (BI), Kho dữ liệu lưu trữ dữ liệu lưu trữ bằng thiết bị điện tử của một tổ chức. Các kho dữ liệu được thiết kế để hỗ trợ việc phân tích dữ liệu và lập báo cáo.
</br>

- Khả năng phân tích của nó cho phép các tổ chức thu được những hiểu biết kinh doanh có giá trị từ dữ liệu của họ để cải thiện việc ra quyết định.
</br>

- Data warehouse tập trung và tổng hợp một lượng lớn dữ liệu từ nhiều nguồn như tiếp thị, bán hàng, tài chính, ứng dụng hướng tới khách hàng, và các hệ thống đối tác bên ngoài…
</br>

- Ở cấp độ kỹ thuật, kho dữ liệu định kỳ lấy dữ liệu từ các ứng dụng và hệ thống đó; sau đó, dữ liệu trải qua quá trình định dạng và nhập để khớp với dữ liệu đã có trong kho. Data warehouse lưu trữ dữ liệu đã xử lý này để sẵn sàng cho những người ra quyết định truy cập. Tần suất kéo dữ liệu xảy ra hoặc cách dữ liệu được định dạng, v.v., sẽ khác nhau tùy thuộc vào nhu cầu của tổ chức
</br>

***

## Đặc điểm chính của Data warehouse

- **Hướng chủ đề (Subject-Oriented)**

    Data warehouse cung cấp thông tin phục vụ cho một chủ thể cụ thể thay vì các hoạt động liên tục của toàn tổ chức. Các chủ đề đó có thể là bán hàng, khuyến mãi, hàng tồn kho,… Ví dụ, nếu muốn phân tích dữ liệu bán hàng của công ty, cần xây dựng một kho dữ liệu tập trung vào việc bán hàng. Một nhà kho như vậy sẽ cung cấp những thông tin có giá trị như “ai là khách hàng tốt nhất của bạn năm ngoái?” hoặc “ai có khả năng trở thành khách hàng tốt nhất của bạn trong năm tới?”
</br>

- **Được tích hợp (Integrated)**

    Data warehouse được phát triển bằng cách tích hợp dữ liệu từ nhiều nguồn khác nhau thành một định dạng nhất quán. Dữ liệu phải được lưu trữ trong kho một cách nhất quán và được mọi người chấp nhận về cách đặt tên, định dạng và mã hóa. Điều này tạo điều kiện cho việc phân tích dữ liệu hiệu quả. 
</br>

- **Bất biến (Non-volatile)**

    Dữ liệu một khi được nhập vào kho dữ liệu phải không thay đổi. Tất cả dữ liệu ở chế độ chỉ đọc (read-only). Dữ liệu trước đó không bị xóa khi nhập dữ liệu hiện tại. Điều này giúp bạn phân tích những gì đã xảy ra và khi nào. Data warehouse tách biệt với cơ sở dữ liệu hoạt động, có nghĩa là bất kỳ thay đổi thường xuyên nào trong cơ sở dữ liệu hoạt động sẽ không được nhìn thấy trong kho dữ liệu.
</br>

- **Có gán nhãn thời gian (Time-Variant)**

    Dữ liệu được lưu trữ trong Data warehouse cung cấp thông tin từ một thời điểm lịch sử cụ thể; do đó, dữ liệu được phân loại với một khung thời gian cụ thể. Ví dụ về Time-Variant trong Data warehouse được hiển thị trong Primary Key có yếu tố thời gian như ngày, tuần hoặc tháng.

***

## 3 loại Data warehouse

- ***3.1. Kho dữ liệu doanh nghiệp (EDW - Enterprise Data Warehouse)***

    Kho dữ liệu doanh nghiệp đóng vai trò là cơ sở dữ liệu chính hoặc trung tâm tạo điều kiện thuận lợi cho việc ra quyết định trong toàn doanh nghiệp. Các lợi ích chính của việc có EDW bao gồm quyền truy cập vào thông tin liên tổ chức, khả năng chạy các truy vấn phức tạp và hỗ trợ các thông tin chi tiết phong phú, có tầm nhìn xa để đưa ra các quyết định dựa trên dữ liệu và đánh giá rủi ro sớm.
</br>

- ***3.2. Kho dữ liệu hoạt động (ODS - Operational Data Store)***

    Trong ODS, Data Warehouse làm mới theo thời gian thực. Do đó, các tổ chức thường sử dụng nó cho các hoạt động doanh nghiệp thông thường, chẳng hạn như lưu trữ hồ sơ của nhân viên. Các quy trình nghiệp vụ cũng sử dụng ODS làm nguồn cung cấp dữ liệu cho EDW.
</br>

- ***3.3. Data Mart***

    Data mart là một tập hợp con của Data Warehouse được xây dựng để duy trì một bộ phận, khu vực hoặc đơn vị kinh doanh cụ thể. Mỗi bộ phận của doanh nghiệp đều có một kho lưu trữ trung tâm hoặc trung tâm dữ liệu để lưu trữ dữ liệu. Dữ liệu từ data mart được lưu trữ định kỳ trong ODS. Sau đó, ODS sẽ gửi dữ liệu đến EDW, nơi nó được lưu trữ và sử dụng. 
