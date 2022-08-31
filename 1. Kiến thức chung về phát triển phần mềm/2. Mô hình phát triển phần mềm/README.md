# Table of Content

- [Mô hình phát triển phần mềm](#mô-hình-phát-triển-phần-mềm)
  - [Mô hình thác nước (Waterfall model)](#mô-hình-thác-nước-waterfall-model)
  - [Mô hình tăng trưởng (Incremental Model)](#mô-hình-tăng-trưởng-incremental-model)
  - [Mô hình Agile](#mô-hình-agile)
  - [Mô hình tiếp cận lặp (Iterative Model)](#mô-hình-tiếp-cận-lặp-iterative-model)
  - [Mô hình chữ V (V model)](#mô-hình-chữ-v-v-model)
  - [Mô hình Scrum](#mô-hình-scrum)
  - [Mô hình RAD](#mô-hình-rad)
  - [So sánh Scrum và Waterfall](#so-sánh-scrum-và-waterfall)
  - [So sánh Scrum vs Agile](#so-sánh-scrum-vs-agile)

## Mô hình phát triển phần mềm

- Mô hình phát triển phần mềm hay quy trình phát triển phần mềm xác định các pha/ giai đoạn trong xây dựng phần mềm
  - Mô hình thác nước ( Waterfall model)
  - Mô hình xoắn ốc ( Spiral model)
  - Mô hình agile
  - Mô hình tiếp cận lặp ( Iterative model)
  - Mô hình tăng trưởng ( Incremental model)
  - Mô hình chữ V ( V model)
  - Mô hình Scrum
  - RAD model ( Rapid Application Development)

***

### Mô hình thác nước (Waterfall model)

![image](https://user-images.githubusercontent.com/43572616/187679119-8ac8ecbe-0b62-40cd-89aa-0d3d283a7265.png)

**Mô tả:**

- Đây được coi như là mô hình phát triển phần mềm đầu tiên được sử dụng.
- Mô hình này áp dụng tuần tự các giai đoạn của phát triển phần mềm.
- Đầu ra của giai đoạn trước là đầu vào của giai đoạn sau. Giai đoạn sau chỉ được thực hiện khi giai đoạn trước đã kết thúc. Đặc biệt không được quay lại giai đoạn trước để xử lý các yêu cầu khi muốn thay đổi.

**Phân tích mô hình:**

- **Requirement gathering**: Thu thập và phân tích yêu cầu được ghi lại vào tài liệu đặc tả yêu cầu trong giai đoạn này.
- **System Analysis**: Phân tích thiết kế hệ thống phần mềm, xác định kiến trúc hệ thống tổng thể của phần mềm.
- **Coding**: Hệ thống được phát triển theo từng unit và được tích hợp trong giai đoạn tiếp theo. Mỗi Unit được phát triển và kiểm thử bởi dev được gọi là Unit Test.
- **Testing**: Cài đặt và kiểm thử phần mềm. Công việc chính của giai đoạn này là kiểm tra và sửa tất cả những lỗi tìm được sao cho phần mềm hoạt động chính xác và đúng theo tài liệu đặc tả yêu cầu.
- **Implementation**: Triển khai hệ thống trong môi trường khách hàng và đưa ra thị trường.
- **Operations and Maintenance**: Bảo trì hệ thống khi có bất kỳ thay đổi nào từ phía khách hàng, người sử dụng.

**Ứng dụng:**

Mô hình thường được áp dụng cho các dự án phần mềm như sau:

- Các dự án nhỏ , ngắn hạn.
- Các dự án có ít thay đổi về yêu cầu và không có những yêu cầu không rõ ràng.

**Ưu điểm:**

- Dễ sử dụng, dễ tiếp cận, dễ quản lý.
- Sản phẩm phát triển theo các giai đoạn được xác định rõ ràng.
- Xác nhận ở từng giai đoạn, đảm bảo phát hiện sớm các lỗi.

**Nhược điểm:**

- Ít linh hoạt, phạm vi điều chỉnh hạn chế.
- Rất khó để đo lường sự phát triển trong từng giai đoạn.
- Mô hình không thích hợp với những dự án dài, đang diễn ra, hay những dự án phức tạp, có nhiều thay đổi về yêu cầu trong vòng đời phát triển.
- Khó quay lại khi giai đoạn nào đó đã kết thúc.

***

### Mô hình tăng trưởng (Incremental Model)

Mô hình gia tăng có tên tiếng anh là Incremental Model.

**1. Nguyên lý mô hình gia tăng.**

![image](https://user-images.githubusercontent.com/43572616/187679143-71f658f0-22d3-4952-88df-4ffb172f61c9.png)

- Với phương pháp chia nhỏ thành từng bản khác nhau, thì từ một chu kỳ lớn sẽ được phân chia thành nhiều chu kỳ nhỏ ứng với từng bản, và do đó có được một đa chu kỳ phát triển.
</br>

- Mỗi chu kỳ nhỏ ứng với một bản phân chia gọi là module đơn giản hơn và dễ dàng quản lý hơn, mỗi module cũng được xây dựng theo từng bước như là phân tích, đọc yêu cầu dự án, viết thiết kế, tiền hành coding và thực hiện test.
</br>

- Nguyên lý của mô hình gia tăng này giống như việc xếp một bức tranh từ các miếng ghép, miếng ghép nào được hoàn thành trước thì sẽ cho ta được một phần bức tranh được thể hiện trước, theo thời gian, số miếng ghép được hoàn thành sẽ gia tăng và sản phầm ngày càng đi vào hoàn thiện.

![image](https://user-images.githubusercontent.com/43572616/187679179-5ff82684-1431-4c8b-991c-e98cf7b09a03.png)

**2. Ưu điểm và nhược điểm.**

***\* Ưu điểm.***

– Có thể sớm tạo ra nguyên mẫu của sản phẩm trong vòng đời phát triển của nó.

– Độ linh hoạt cao hơn và khi thay đổi yêu cầu dự án thì chi phí sẽ ít hơn nhiều, vì những thay đổi thuộc về module nào thì module đó sẽ thay đổi mà các module khác không hề bị ảnh hưởng.

– Việc phân chia thành các module cũng sẽ làm cho việc test nhẹ nhàng hơn, những module đơn giản thì test cũng đơn giản, sớm kết thúc.

– Giảm chi phí cho lần đầu giao sản phẩm.

– Dễ dàng quản lý các rủi ro có thể phát sinh.

***\* Nhược điểm***.

– Cần phải có những khả năng thiết kế tốt và phương pháp tốt, để có thể hiểu rõ được yêu cầu và biết cách phân chi nó ra như thế nào cho hợp lý.

– Chi phí để phát triển theo phương pháp này là rất cao, cao hơn hẳn waterfall.***

**3. Khi nào thì áp dụng mô hình tăng trưởng.**

- Áp dụng mô hình này khi yêu cầu của dự án là rõ ràng, đầy đủ, và nắm rõ được các yêu cầu của dự án.
- Khi sớm cần có một nguyên mẫu phần mềm để quáng bá, giới thiệu hoặc thử nghiệm.
- Sử dụng mô hình này khi một công nghệ mới được áp dụng.
- Tài nguyên và kỹ năng chuyên môn luôn sẵn sàng.
- Khi có một tính năng hay các mục tiêu có nguy cơ lỗi cao.

***

### Mô hình Agile

Agile là một phương pháp phát triển phần mềm linh hoạt để làm sao đưa sản phẩm đến tay người dùng càng nhanh càng tốt và được xem như là sự cải tiến so với những mô hình cũ như mô hình “Thác nước (waterfall)” hay “CMMI”. Phương thức phát triển phần mềm Agile là một tập hợp các phương thức phát triển lặp và tăng dần trong đó các yêu cầu và giải pháp được phát triển thông qua sự liên kết cộng tác giữa các nhóm tự quản và liên chức năng.

![image](https://user-images.githubusercontent.com/43572616/187679216-e374fb98-7e8c-421d-a4ee-5d1c8b7b5183.png)

**Mô tả:**

- Dựa trên mô hình iterative and incremental.
- Các yêu cầu và giải pháp phát triển dựa trên sự kết hợp của các function.
- Trong Agile, các tác vụ được chia thành các khung thời gian nhỏ để cung cấp các tính năng cụ thể cho bản phát hành cuối.

**Ứng dụng:**

- Có thể được sử dụng với bất kỳ loại hình dự án nào, nhưng cần sự tham gia và tính tương tác của khách hàng.
- Sử dụng khi khách hàng yêu cầu chức năng sẵn sàng trong khoảng thời gian ngắn.

**Ưu điểm:**

- Tăng cường tinh thần làm việc nhóm và trao đổi công việc hiệu quả.
- Các chức năng được xây dựng nhanh chóng và rõ ràng, dế quản lý.
- Dễ dàng bổ sung, thay đổi yêu cầu.
- Quy tắc tối thiểu, tài liệu dễ hiểu, dễ sử dụng.

**Nhược điểm:**

Mô hình Agile được sử dụng rộng rãi trên thế giới nhưng cũng không đồng nghĩa với phù hợp với tất cả các dự án phần mềm.

- Không thích hợp để xử lý các phụ thuộc phức tạp.
- Có nhiều rủi ro về tính bền vững, khả năng bảo trì và khả năng mở rộng.
- Cần một team có kinh nghiệm.
- Phụ thuộc rất nhiều vào sự tương tác rõ ràng của khách hàng.
- Chuyển giao công nghệ cho các thành viên mới trong nhóm có thể khá khó khăn do thiếu tài liệu.

***

### Mô hình tiếp cận lặp (Iterative Model)

![image](https://user-images.githubusercontent.com/43572616/187679252-972d67d2-273d-4648-acd9-c3abb7a23596.png)

![image](https://user-images.githubusercontent.com/43572616/187679272-e84d9be5-5b87-482f-88b1-f1f973933366.png)

**Mô tả:**

- Một mô hình được lặp đi lặp lại từ khi start cho đến khi làm đầy đủ spec (chỉ dẫn kỹ thuật). Quá trình này sau đó được lặp lại, tạo ra một phiên bản mới của phần mềm vào cuối mỗi lần lặp của mô hình.

- Thay vì phát triển phần mềm từ spec đặc tả rồi mới bắt đầu thực thi thì mô hình này có thể review dần dần để đi đến yêu cầu cuối cùng.

**Ứng dụng:**

- Yêu cầu chính phải được xác định; tuy nhiên, một số chức năng hoặc yêu cầu cải tiến có thể phát triển theo thời gian.
- Một công nghệ mới đang được sử dụng và đang được học tập bởi nhóm phát triển trong khi làm việc trong dự án.
- Phù hợp cho các dự án lớn và nhiệm vụ quan trọng.

**Ưu điểm:**

- Xây dựng và hoàn thiện các bước sản phẩm theo từng bước.
- Thời gian làm tài liệu sẽ ít hơn so với thời gian thiết kế.
- Một số chức năng làm việc có thể được phát triển nhanh chóng và sớm trong vòng đời.
- Ít tốn kém hơn khi thay đổ phạm vi, yêu cầu.
- Dễ quản lý rủi ro.
- Trong suốt vòng đời, phần mềm được sản xuất sớm để tạo điều kiện cho khách hàng đánh giá và phản hồi.

**Nhược điểm:**

- Yêu cầu tài nguyên nhiều.
- Các vấn đề về thiết kế hoặc kiến trúc hệ thống có thể phát sinh bất cứ lúc nào.
- Yêu cầu quản lý phức tạp hơn.
- Tiến độ của dự án phụ thuộc nhiều vào giai đoạn phân tích rủi ro.

***

### Mô hình chữ V (V model)

![image](https://user-images.githubusercontent.com/43572616/187679297-f5de993f-89ec-44bb-86a4-5116f04f8b2f.png)

**Mô tả:**

- Mô hình chữ V là một phần mở rộng của mô hình thác nước và được dựa trên sự kết hợp của một giai đoạn thử nghiệm cho từng giai đoạn phát triển tương ứng. Đây là một mô hình có tính kỷ luật cao và giai đoạn tiếp theo chỉ bắt đầu sau khi hoàn thành giai đoạn trước.
</br>

- Với V model thì công việc test được tham gia ngay từ đầu.

**Ứng dụng:**

- Yêu cầu được xác định rõ ràng.
- Xác định sản phẩm ổn định.
- Công nghệ không thay đổi và được hiểu rõ bởi nhóm dự án.
- Không có yêu cầu không rõ ràng hoặc không xác định.
- Dự án ngắn.

**Ưu điểm:**

- Đây là một mô hình có tính kỷ luật cao và các giai đoạn được hoàn thành cùng một lúc.
- Hoạt động tốt cho các dự án nhỏ, khi các yêu cầu được hiểu rất rõ.
- Đơn giản và dễ hiểu và dễ sử dụng, dễ quản lý.

**Nhược điểm:**

- Khó quản lý kiểm soát rủi ro, rủi ro cao.
- Không phải là một mô hình tốt cho các dự án phức tạp và hướng đối tượng.
- Mô hình kém cho các dự án dài và đang diễn ra.
- Không thích hợp cho các dự án có nguy cơ thay đổi yêu cầu trung bình đến cao.

***

### Mô hình Scrum

(một quy trình phát triển phần mềm thuộc họ agile)

**1. Khái niệm Scrum.**

Là một quy trình phát triển phần mềm theo mô hình linh hoạt (agile). Với nguyên tắc chủ đạo là chia nhỏ phần mềm cần sản xuất ra thành các phần nhỏ để phát triển (các phần nhỏ này phải đọc lập và Release được), lấy ý kiến khách hàng và thay đổi cho phù hợp ngay trong quá trình phát triển để đảm bảo sản phẩm release đáp ứng những gì khách hàng mong muốn. Scrum chia dự án thành các vòng lặp phát triển gọi là các sprint. Mỗi sprint thường mất 2- 4 tuần (30 ngày) để hoàn thành. Nó rất phù hợp cho những dự án có nhiều sự thay đổi và yêu cầu tốc độ cao.

**2. Một số đặc điểm của Quy trình phát triển phần mềm SCRUM.**

- Scrum (hay agile nói chung) được xếp vào nhóm “Feature-driven development”. Sản phầm được phát triển theo tính năng, chứ không phát triển sản phẩm theo kiến trúc hệ thống.
</br>

- Scrum khác với các mô hình Agile ở chỗ nó là mô hình hướng khách hàng (Customer oriented), vai trò của khách hàng trong việc đánh giá sản phẩm rất quan trọng. Chỉ sau mỗi sprint (2-4 tuần) khách hàng sẽ thấy được sự thay đổi của sản phẩm của mình qua đó đưa ra phản hồi sớm để định hướng -> Thích ứng nhanh với sự thay đổi yêu cầu.
</br>

- Scrum giảm thiểu tài nguyên dành cho việc quản lý mà tập trung nhiều hơn cho những công việc liên quan trực tiếp đến việc làm ra sản phẩm. Bằng cách giảm vai trò quản lý (PM) bằng cách đẩy việc quản lý tới từng người.
</br>

- Giảm thời gian dành cho việc viết tài liệu bằng cách tăng thời gian trao đổi trực tiếp. Thông thường khi estimate công việc, thì team estimate cả thời gian dành cho communication để hoàn thành task đó nữa.
</br>

- Tập trung vào sản phẩm, sản phẩm mới là đích cuối cùng chứ không phải qui trình.

**3. Ưu điểm, nhược điểm của mô hình Scrum.**

***ƯU ĐIỂM:***

- Một người có thể làm nhiều việc ví dụ như dev có thể test
- Phát hiện lỗi sớm hơn rất nhiều so với các phương pháp truyền thống
- Khách hàng nhanh chóng thấy được sản phẩm qua đó đưa ra phản hồi sớm.
- Có khả năng áp dụng được cho những dự án mà yêu cầu khách hàng không rõ ràng ngay từ đầu.

***NHƯỢC ĐIỂM:***

- Trình độ của nhóm là có một kỹ năng nhất định
- Phải có sự hiểu biết về mô hình aglie .
- Khó khăn trong việc xác định ngân sách và thời gian.
- Luôn nghe ý kiến phản hồi từ khách hàng và thay đổi theo nên thời gian sẽ kéo dài khi có quá nhiều yêu cầu thay đổi từ khách hàng.
- Vai trò của PO (**Product Owner**) rất quan trọng, PO là người định hướng sản phẩm. Nếu PO làm không tốt sẽ ảnh hưởng đến kết quả chung.

**4. Các nhân tố cấu tạo lên 1 quy trình phát triển phần mềm trong Scrum:**

Một cách đơn giản có 03 thành tố quan trọng cấu thành nên SCRUM: Tổ chức (Organization), Qui trình (Process),  Tài liệu (Atifacts). Trong mỗi thành tố có 03 thành tố con. Như vậy, chúng ta chỉ cần hiểu và áp dụng được 9 thành tố này là có thể áp dụng SCRUM.

- Tổ chức (Organization): Tổ chức nhóm dự án và Roles (Vài trò)
  - Product Owner (Người sở hữu sản phẩm)
  - ScrumMaster (Người điều phối )
  - Development Team (Nhóm phát triển)
</br>

- Tài liệu (Atifacts):  các kết quả đầu ra
  - Product Backlog  (Danh sách các chức năng cần phát triển của sản phẩm)
  - Sprint Backlog (Danh sách các chức năng cần phát triển cho mỗi giai đoạn)
  - Estimation (Kết quả ước lượng của Team)
</br>

- Qui trình(Process):  Qui định cách thức vận hành của SCRUM
  - Sprint Planning meeting (Họp để hoạch định cho mỗi giai đoạn)
  - Sprint Review (Họp để tổng kết cho mỗi giai đoạn)
  - Daily Scrum Meeting (Họp review hàng ngày)

**Tổ chức của dự án (Organization):**

![image](https://user-images.githubusercontent.com/43572616/187679343-71bf4a53-2334-47a2-9130-d87d75b85408.png)

- **Product Owner**

Product Owner là người sở hữu sản phẩm, người quyết định sản phẩm có những chức năng nào và là người quyết định Product Backlog, họ sẽ tham gia 1 phần vào quy trình phát triển phần mềm. Thông thường Role này được khách hàng hoặc người đại diện cho khách hàng đảm nhận.

- **ScrumMaster**

Scrum Master là người đảm bảo các qui trình của Scrum được thực hiện đúng và thuận lợi, giúp đỡ cho Team thực hiện công việc phát triển sản phẩm một cách tốt nhất.

- **Development Team (Nhóm phát triển)**

Một nhóm từ 4-7 kỹ sư phần mềm chịu trách nhiệm phát triển sản phẩm. Nhóm dự án phải làm việc với Product Owner để quyết định những gì sẽ làm trong Sprint (giai đoạn )này và kết quả sẽ ra sao. Đồng thời nhóm cũng thảo luận để đưa ra các giải pháp, ước lượng thời gian thực hiện công việc, họp đánh giá kết quả công việc. Nếu dự án lớn chúng ta cần chia ra thành các dự án nhỏ.

**Tài liệu (Atifacts):**

- **Product Backlog**

Product Backlog là danh sách các chức năng cần được phát triển của sản phẩm trong quy trình phát triển phần mềm. Danh sách này do Product Owner quyết định. Nó thường xuyên được cập nhật để đáp ứng được nhu cầu thay đổi của khách hàng cũng như các điều kiện của dự án.

![image](https://user-images.githubusercontent.com/43572616/187679383-7896f9cc-cc4e-43a3-8bd5-237e49edf349.png)

- **Sprint Backlog**

Sprint là một giai đoạn phát triển trong quá trình phát triển sản phẩm, nó được khuyến khích có chiều dài từ 2 – 4 tuần. Mỗi Sprint được xác định bằng thời gian phát triển, danh sách các chức năng phát triển (Sprint Backlog).

*Mỗi sprint phải Release được sản phẩm để đảm bảo lấy được ý kiến khách hàng, qua được các qui trình phát triển của sản phẩm nhằm rút kinh nghiệm và tránh sự cố sau này.*

Sprint Backlog là danh sách chức năng phát triển trong Sprint, nó được quyết định bởi cuộc họp Sprint Planning. Sprint Backlog là các chức năng được chọn từ Product Backlog dựa trên mức độ ưu tiên và khả năng của team phát triển.

![image](https://user-images.githubusercontent.com/43572616/187679416-f301f646-07ef-40a8-890e-8ee18b85c53d.png)

- **Estimation (ước lượng)**

Trong SCRUM thì các thành viên của Team sẽ tự lựa chọn Task cho mình và ước lượng thời gian phát triển dự  kiến và chịu trách nhiệm với ước lượng này. Sau khi hoàn thành sẽ cập nhật vào bảng Sprint Backlog.

![image](https://user-images.githubusercontent.com/43572616/187679439-6d882fbf-131d-4937-a597-448bf7fa370b.png)

**Qui trình(Process):**

![image](https://user-images.githubusercontent.com/43572616/187679460-62ce7673-c67d-48ed-beb5-97e0b5223c6a.png)

- **Sprint Planning meeting  (Họp lập kế hoạch cho mỗi Sprint)**

Như  chúng ta đã biết ở trên Sprint là một giai đoạn phát triển có thời gian từ 2-4 tuần. Để chuẩn bị cho mỗi Sprint team cần phải họp để xác định những chức năng nào (story) sẽ phát triển trong giai đoạn này (sprint backlog), kết quả đầu ra dự kiến (Goal, kết quả Release), Estimate (ước lượng ai làm việc gì) và thảo luận các giải pháp. Tất cả được ghi thành biên bản để có cơ sở thực hiện và Review sau này.

- **Sprint Review**

Là cuộc họp để đánh giá lại kết quả thực hiện của Sprint vừa qua, xác định những chức năng được Release, những chức năng tiếp tục sửa hoặc phát triển thêm, xác định những vấn đề phát sinh và bàn phương án giải quyết, bổ sung Product Backlog v….

- **Daily Scrum Meeting (hay còn gọi là Standup Meeting)**
  - Daily Scrum Meeting là cuộc họp hàng ngày và được đề nghị không quá 15 phút và họp đứng để đảm bảo thời gian họp không bị kéo dài vào đầu mỗi ngày, mỗi thành viên chỉ trả lời 3 câu hỏi:
    - Phát sinh vấn đề gì trong quy trình phát triển phần mềm?
    - Hôm nay bạn sẽ làm gì
    - Hôm qua bạn làm được gì?
    - Nếu thành viên gặp vấn đề thì nên làm việc riêng để giải quyết để không mất nhiều thời gian của các thành viên.  Scrum Master phải đảm bảo cuộc họp này được thực hiện đúng qui định.
    - Các Sprint sẽ được lặp đi lặp lại cho tới khi nào các hạng mục trong Product Backlog đều được hoàn tất hoặc khi Product Owner quyết định có thể dừng dự án căn cứ tình hình thực tế. Do sử dụng chiến thuật “có giá trị hơn làm trước” nên các hạng mục mang lại nhiều giá trị hơn cho chủ dự án luôn được hoàn tất trước. Do đó Scrum luôn mang lại giá trị cao nhất cho người đầu tư cho dự án. Do quy trình luôn luôn được cải tiến, nhóm Scrum thường có năng suất lao động rất cao. Đây là hai lợi ích to lớn mà quy trình phát triển phần mềm Scrum mang lại cho tổ chức.

***

### Mô hình RAD

![image](https://user-images.githubusercontent.com/43572616/187679486-2eea13c3-85be-481e-a932-4b7a4f119fcc.png)

**Mô tả:**

- Mô hình RAD là một phương pháp phát triển phần mềm sử dụng quy hoạch tối thiểu có lợi cho việc tạo mẫu nhanh.
</br>

- Các mô-đun chức năng được phát triển song song như nguyên mẫu và được tích hợp để tạo ra sản phẩm hoàn chỉnh để phân phối sản phẩm nhanh hơn.
</br>

- Đảm bảo rằng các nguyên mẫu được phát triển có thể tái sử dụng được.

**Ứng dụng:**

Mô hình RAD có thể được áp dụng thành công cho các dự án:

- Module hóa rõ ràng. Nếu dự án không thể được chia thành các mô-đun, RAD có thể không thành công.
- RAD nên được sử dụng khi có nhu cầu để tạo ra một hệ thống có yêu cầu khách hàng thay đổi trong khoảng thời gian nhỏ 2-3 tháng.
- Nên được sử dụng khi đã có sẵn designer cho model và chi phí cao.

**Ưu điểm:**

- Giảm thời gian phát triển.
- Tăng khả năng tái sử dụng của các thành phần.
- Đưa ra đánh giá ban đầu nhanh chóng.
- Khuyến khích khách hàng đưa ra phản hồi.

**Nhược điểm:**

- Trình độ của nhóm cần có một kỹ năng nhất định.
- Chỉ những hệ thống có module mới sử dụng được mô hình này.

**2. Tổng kết vòng đời phát triển phần mềm.**

![image](https://user-images.githubusercontent.com/43572616/187679509-9369e9b8-cbf1-49c0-bb74-93a7017aad92.png)

- SDLC( Software Development Life Circicle) là một quá trình đi theo suốt trong một dự án phần mềm, trong một tổ chức phần mềm. Nó bao gồm một kế hoạch chi tiết mô tả cách phát triển, duy trì, thay thế và thay đổi hoặc nâng cao phần mềm cụ thể. Vòng đời xác định một phương pháp để cải thiện chất lượng phần mềm và quy trình phát triển tổng thể.
- Mỗi mô hình sẽ có sự khác nhau, tuy nhiên, mỗi mô hình bao gồm tất cả hoặc một số giai đoạn / hoạt động / nhiệm vụ sau.

**Planning - Lập kế hoạch:**

- Phân tích yêu cầu được thực hiện bởi các senior member của nhóm với đầu vào từ khách hàng, bộ phận bán hàng, khảo sát thị trường và các chuyên gia trong ngành.
- Lập kế hoạch cho các yêu cầu đảm bảo chất lượng và xác định các rủi ro liên quan đến dự án.

**Defining - Xác định yêu cầu:**

- Xác định rõ ràng và ghi lại các yêu cầu.
- Thực hiện xác định yêu cầu thông qua một tài liệu SRS (Software Requirement Specification) bao gồm tất cả các yêu cầu sản phẩm được thiết kế và phát triển trong suốt vòng đời của dự án.

**Designing - Phân tích thiết kế kiến trúc hệ thống:**

- Trong giai đoạn này, thiết kế hệ thống và phần mềm được chuẩn bị từ các đặc tả yêu cầu đã được nghiên cứu trong giai đoạn đầu tiên.
- Thiết kế hệ thống giúp xác định các yêu cầu phần cứng và kiến trúc hệ thống tổng thể.

**Building - Phát triển:**

- Khi nhận được tài liệu thiết kế hệ thống, công việc được chia thành các module nhỏ và coding được bắt đầu.
- Đây là giai đoạn trọng tâm và dài nhất của vòng đời phát triển phần mềm.

**Testing - Kiếm thử:**

- Sau khi coding được phát triển, nó được kiểm tra dựa trên các yêu cầu để đảm bảo rằng sản phẩm thực sự hoạt động đúng trong giai đoạn phân tích yêu cầu.
- Trong giai đoạn này tất cả các loại kiểm thử chức năng như kiểm thử đơn vị, kiểm thử tích hợp, kiểm thử hệ thống, kiểm thử chấp nhận được thực hiện cũng như test phi chức năng cũng được thực hiện.

**Deployment - Phát hành/triển khai:**

- Sau khi thử nghiệm thành công, sản phẩm được phân phối / triển khai cho khách hàng để họ sử dụng.
- Khách hàng sẽ thực hiện test beta. Nếu có bất kỳ vấn đề nào xảy ra, thì họ sẽ báo cáo cho nhóm kỹ thuật để được hỗ trợ.

**Maintenance - Bảo trì:**

- Trong quá trình bảo trì của SDLC, hệ thống được đánh giá để đảm bảo nó không trở nên lỗi thời.
- Một khi khách hàng bắt đầu sử dụng hệ thống đã phát triển thì những vấn đề thực sự xuất hiện và cần được giải quyết theo thời gian.
  Như vậy trong bài chia sẻ này, mình đã giới thiệu ngắn gọn một số mô hình phát triển phần mềm phổ biến hiện nay. Hy vọng rằng kiến thức mình tổng hợp sẽ giúp ích cho các bạn trong quá trình học tập cũng như làm việc.

***

### So sánh Scrum và Waterfall

|**Đặc điểm**|**Waterfall**|**Spiral**|**Scrum**|
| :- | :- | :- | :- |
|**Xác định các giai đoạn phát triển**|Bắt buộc|Bắt buộc|Chỉ có giai đoạn lập kế hoạch và kết thúc|
|**Sản phẩm cuối cùng**|Được xác định trong quá trình lập kế hoạch|Được xác định trong quá trình lập kế hoạch|Xác định trong suốt quá trình dự án|
|**Chi phí sản xuất**|Được xác định trong quá trình lập kế hoạch|Thay đổi cục bộ|Xác định trong quá trình xây dựng dự án|
|**Ngày hoàn thành sản phẫm**|Được xác định trong quá trình lập kế hoạch|Thay đổi cục bộ|Xác định trong quá trình xây dựng dự án|

***

### So sánh Scrum vs Agile

**Giống nhau:**

Điểm tương đồng đầu tiên là Agile và Scrum đều áp dụng cơ chế lặp lại và sự tăng trưởng. Do đó,cả hai đều nhấn mạnh việc vừa phát triển phần mềm và vừa điều chỉnh theo phản hồi. Vì Scrum được xây dựng dựa trên Agile nên hai phương pháp Agile và Scrum sẽ có chung mục tiêu. Đó là tối đa hóa các giá trị mà mỗi phương pháp sẽ tạo ra cho khách hàng doanh nghiệp.

*Agile và Scrum đều áp dụng cơ chế lặp lại và sự tăng trưởng.*

Tóm lại, cả hai phương pháp đều cố gắng chuyển giao sản phẩm dự án trong thời gian nhanh nhất có thể. Ngoài ra, Agile và Scrum còn nhấn mạnh việc quản lý hiệu quả và hợp tác, giao tiếp cởi mở.

**Khác nhau:**

*Mặc dù có nhiều thứ tương đồng nhưng Agile và Scrum cũng có khá nhiều điểm khác biệt rõ ràng.*

|**Agile**|**Scrum**|
| :-: | :-: |
|Là phương pháp luận gồm nhiều nguyên tắc.|Là một trong những mô hình làm việc áp dụng và triển khai các nguyên tắc của Agile.|
|Phạm vi áp dụng rộng vì là phương pháp luận.|Phạm vi áp dụng bị hạn chế vì chỉ là một trong những mô hình triển khai phương pháp Agile.|
|Chú trọng việc giao tiếp trực tiếp và tương tác tương quan giữa tất cả thành viên trong team.|Việc trao đổi, thảo luận được thực hiện hàng ngày (hoặc hàng tuần) theo một lịch trình cụ thể.|
|Có thể cần thay đổi quy trình, cách tổ chức khi bắt đầu hoặc trước khi bắt đầu dự án.|Không cần tiến hành thay đổi quá nhiều về quy trình hay cách tổ chức khi thực hiện dự án.|
|Thường có xu hướng chuyển giao sản phẩm khi chuẩn bị sắp kết thúc dự án phát triển phần mềm.|Cung cấp bản tổng hợp increment về các hạng mục của sản phẩm cho khách hàng sau mỗi vòng sprint.|
|Leader (nhóm trưởng) có vai trò cực kỳ quan trọng, chịu trách nhiệm về công việc của toàn bộ team.|Scrum team là một team đa chức năng, có khả năng tự quản, tự tổ chức và tự định hướng.|
|Liên tục giám sát các giai đoạn của một vòng đời phát triển phần mềm như phân tích, thiết kế,…|Việc giám sát diễn ra sau khi tổng hợp các tính năng nhất định thay vì sau mỗi vòng sprint.|
