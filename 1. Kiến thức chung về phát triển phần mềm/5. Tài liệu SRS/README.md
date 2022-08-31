# Tài liệu SRS

- Tài liệu SRS là viết tắt của từ Software Requirement Specification, có nghĩa là tài liệu đặc tả yêu cầu.
</br>

- Chức năng mô tả các yêu cầu về cả chức năng và phi chức năng của hệ thống một cách chi tiết. Tài liệu này sẽ giúp đưa ra các chức năng của hệ thống hay dùng cho việc đọc hiểu hệ thống của bên thứ ba có liên quan đến công ty.

***

## Các thành phần của tài liệu SRS

Tài liệu SRS bao gồm 7 thành phần chính sau đây:

**Introduction (Phần giới thiệu): Đây là phần đầu tiên của tài liệu, bao gồm những nội dung sau:**

- **Purpose:** Mô tả mục đích và ý nghĩa của tài liệu đặc tả yêu cầu một cách chi tiết, giúp người đọc nắm được khái niệm sự quan trọng của nó.
- **Application Overview:** Mô tả tổng quan hệ thống. Hệ thống phải đảm bảo các yếu tố như: quyền sử dụng, tính năng, khái quát, mục đích của hệ thống.
- **Intended Audience and Reading Suggestions:** Mô tả mục đích sử dụng và các đối tượng chứa tài liệu SRS.
- **Abbreviations:** Là một danh sách bao gồm các từ viết tắt và ý nghĩa giúp người đọc hiểu rõ hơn.
- **References:** Mô tả các tài liệu liên quan và mục đích sử dụng chúng.

**High Level Requirement (Yêu cầu mức độ tổng thể), bao gồm những nội dung sau:**

- **Object Relationship Diagram:** Mô hình mô tả mối quan hệ tĩnh giữa các đối tượng của hệ thống.
- **Workflow Diagram:** Có chức năng hiển thị chuỗi công việc hay các bước mà người dùng thực hiện. Mỗi hành động của người dùng sẽ được hiển thị ở từng giai đoạn trên hệ thống.
- **State Transition Diagram:** Mô tả từng bước trạng thái của workflow giúp người đọc biết được người thực hiện và tác động đến trạng thái của hệ thống như thế nào.
- **Use Case Diagram:** Mô tả cách người dùng sử dụng tính năng của hệ thống.

**Security Requirement (Yêu cầu bảo mật):**

Ở phần này, nhiệm vụ chính là mô tả nhiệm vụ của người dùng hệ thống, chức năng của người dùng và cho người dùng thấy quyền của họ trong hệ thống. Bảng ma trận nhiệm vụ đối với từng người sử dụng hệ thống sẽ được hiển thị ngay trong phần này.

**Use Case Specification (Đặc tả Use Case):**

Tất cả các chức năng của hệ thống, mô tả nhiệm vụ phải thực hiện về hành vi đầu ra, đầu vào một cách chi tiết. Thêm vào đó, Những tương tác từ tác nhân bên ngoài vào hệ thống và kết quả của việc tương tác đó cũng sẽ được hiển thị ở phần này.

**Other Requirement (Những yêu cầu khác):**

Ở phần này, các yêu cầu bổ sung đối với hệ thống sẽ được hiển thị chi tiết, sau đó được chuyển đến các yêu cầu phi hệ thống.

**Integration (Yêu cầu tích hợp):**

Hỗ trợ việc đính kèm các tài liệu hoặc những nội dung liên quan đến hệ thống từ bên ngoài vào phần này.

**Appendices (Phụ lục):**

Cho phép người dùng xác định được các lỗi tin nhắn ở hệ thống hoặc những email mẫu trên hệ thống.

***

## Vai trò và cách viết tài liệu SRS

Tài liệu SRS là một tài liệu quan trọng trong công việc phát triển phần mềm, bởi nó bao gồm những vai trò sau:

- Giúp các đội phát triển xây dựng hệ thống chính xác, mô tả được hết chức năng, tránh đi lạc hướng với yêu cầu của khách hàng.
- Tránh gặp phải các trường hợp có quá nhiều ý kiến và giúp cho các bên liên quan hiểu về hệ thống một cách rõ ràng.
- Giúp cho việc bảo trì và nâng cao các chức năng của hệ thống một cách dễ dàng và nhanh chóng.
- Giúp các chuyên viên kiểm thử hệ thống hiểu được dễ dàng từ đó có thể xây dựng chi tiết các kịch bản kiểm thử.



**Để viết một tài liệu chính xác nên tuân thủ các điều kiện sau:**

- **Tài liệu có tính chính xác:** Điều này vô cùng quan trọng để đảm bảo SRS luôn thể hiện được đặc điểm kỹ thuật và chức năng của sản phẩm.
- **Tài liệu có tính rõ ràng:** Đây là một điều cơ bản không thể bỏ qua. Nội dung trong tài liệu phải có tính rõ ràng giúp người đọc dễ đọc hơn cũng như nắm bắt được hết nội dung.
- **Tài liệu phải hoàn tất:** Đây là những nhu cầu thiết yếu của người mua mà bạn không thể bỏ qua.
- **Nội dung phù hợp:** Các từ viết tắt hay các định nghĩa trong tài liệu SRS phải được sử dụng nhất quán.
- **Xếp hạng mức độ quan trọng:** Việc xếp hạng mức độ quan trọng sẽ giúp cho các yêu cầu được xác minh.
- **Tài liệu phải được kiểm chứng:** Cần sử dụng nhiều phương pháp trong việc xác định và kiểm chứng nội dung trong tài liệu.
- **Cho phép sửa đổi:** Những thay đổi và yêu cầu cần phải thực hiện một cách có hệ thống và việc tác động đến các yêu cầu khác phải cần được xem xét.
- **Tài liệu có tính truy nguyên:** Hỗ trợ truy nguồn được nguồn gốc từ đầu.

***

## Phân biệt tài liệu SRS với BRD, FRS

  - **BRD (Business Requirement Document)** là tài liệu yêu cầu nghiệp vụ ghi lại yêu cầu nghiệp vụ và các bên liên quan. Đây là tài liệu đầu tiên trong quá trình phát triển của tổ chức.


    Các chiến lược của công ty mà họ cố gắng đạt được trong tương lai sẽ được mô tả trong tài liệu này. Để dễ hiểu hơn thì nó trả lời tất cả các câu hỏi tại sao có những yêu cầu trên, sự thay đổi của hệ thống và một kết quả như mong đợi. Các nhà tài trợ, quản lý chung, quản lý cao cấp và BA chính là đối tượng sử dụng của BRD.
</br>

- **FRS là viết tắt của từ Functional Requirement Specifications**- tài liệu mô tả thông số kỹ thuật yêu cầu của chức năng. Đây là tài liệu chi tiết nhất trong 3 tài liệu được liệt kê, nó sẽ hệ thống cách dự kiến hoạt động để đáp ứng yêu cầu được nêu trong các tài liệu SRS và BRS. Mỗi yêu cầu, chức năng trong từng trường và sự tương tác của người dùng với mỗi trang trong hệ thống sẽ được FRS xây dựng mô tả một cách chi tiết và rõ ràng.
</br>

    FRS được tạo ra từ cách mà hệ thống tương tác với người dùng và quan điểm của họ. Khi hoàn thành xong, tài liệu FRS sẽ được đưa đến cho quản lý dự án kiểm tra, sau đó mới đưa cho khách hàng và được xác nhận lại lần nữa. Tài liệu này sẽ là bản chuẩn về cách thức phần mềm hoạt động, sau khi được xác nhận lại lần cuối.
