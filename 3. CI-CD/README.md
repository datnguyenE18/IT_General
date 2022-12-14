# CI/CD

- Là một mô hình mới có những lợi ích về tốc độ, tự động hóa trong công việc

## Quy trình phát triển cũ

- Developer sau khi code xong thì sẽ build trực tiếp trên máy tính/laptop cá nhân, sau đó chờ code được build hoàn tất

- Upload thủ công file lên repo, trải qua 3,4 bước thao tác, rồi tiếp tục chờ cho đến khi kết thúc (vì code khá to)

- File được upload xong hết, Developer thông báo đến team Tester/QA QC và lúc này mới bắt đầu thực hiện công tác kiểm thử cho toàn bộ sản phẩm.

- Nếu xảy ra sai sót thì quy trình gần như sẽ quay lại từ đầu, thời gian chờ giữa 2 bên Developer và Tester/QA QC tương đối dài, khiến cho dự án cũng bị trì hoãn

- Developer có thể khi phát triển một tính năng mới có thể làm hỏng tính năng cũ đang chạy trên ứng dụng, mà chỉ khi deploy mới phát hiện ra.
</br>

***

## Khi áp dụng CI/CD

- Triệt tiêu hiệu quả các bước thủ công trong quy trình phát triển phần mềm/ứng dụng
- Việc của Developer chỉ là commit code, còn lại tất cả quy trình bao gồm chạy build, test, deploy sẽ được tự động thực hiện hoàn toàn bởi công cụ (tool) CI/CD
- Nếu có thể kết hợp thêm với automation test thì quy trình sẽ chặt chẽ và hạn chế được tối đa các lỗi phát sinh (ví dụ: lỗi phát triển tính năng mới làm hỏng tính năng cũ)
</br>

***

## CI - Continuous Integration (tích hợp liên tục)

- Là một phương pháp phát triển phần mềm theo hướng tự động hóa. CI đảm nhận nhiệm vụ xây dựng và kiểm tra một cách tự động
- Các thành viên trong đội cần phải tích hợp công việc với nhau một cách thường xuyên, mỗi ngày cần ít nhất một lần tích hợp.
- Mỗi lần tích hợp sẽ được xây dựng một cách tự động nhằm mục đích phát hiện ra những lỗi phát sinh một cách nhanh nhất có thể.
- Sử dụng CI sẽ giúp làm giảm những vấn đề về tích hợp và cho phép các dev phát triển phần mềm nhanh hơn và đúng tiến độ hơn
- Quy trình làm việc của CI:
  - Các developer sẽ commit code lên repo (repository - kho).
  - CI server sẽ thực hiện giám sát trên repo và kiểm tra xem có bất kỳ sự thay đổi nào trên repo hay không.
  - Khi xảy ra những thay đổi, CI server sẽ phải hiện ra code mới nhất từ repo và sau đó sẽ build, chạy các unit test và integration test
  - sau đó, CI server sẽ tạo ra những phản hồi và gửi đến cho các thành viên trong dự án. Và CI server lại tiếp tục chờ đợi những thay đổi từ repo

- Mỗi lần Dev làm xong các task của mình, họ sẽ run code trên local trước để kiểm tra trước khi commit code lên repo.

![image](https://user-images.githubusercontent.com/43572616/187832190-39d1ce43-41ba-4a62-be0e-f8c8c3af17d7.png)

***

## CD - Continuous Delivery (chuyển giao liên tục)

- Là quá trình nâng cao hơn đó là kiểm tra tất cả những thay đổi về code đã được build và code trong môi trường kiểm thử. CD cho phép các lập trình viên tự động hóa phần mềm testing, kiểm tra phần mềm qua nhiều thước đo trước khi triển khai.

- Những bài test này có thể bao gồm UI testing, integration testing, API testing,... CD sử dụng Deployment Pipeline giúp chia quy trình chuyển giao thành các giai đoạn. Mỗi giai đoạn có những mục tiêu riêng để xác minh chất lượng của các tính năng từ một góc độ vô cùng khác để có thể kiểm định được chức năng và tránh những lỗi phát sinh ảnh hưởng đến người dùng.
</br>

- CI/CD là quá trình làm việc liên tục và tự động hóa của phần mềm. Để quá trình kiểm thử được diễn ra liên tục thì CI/CD phải được tích hợp vào trong vòng đời phát triển phần mềm. Là chìa khóa kết hợp các khâu kiểm thử và phát triển phần mềm lại với nhau.

***

## Quy trình CI/CD hoàn chỉnh

- Developer commit code (đẩy code lên server).
  - Khi Developer phát triển một tính năng nào đó thì họ sẽ tạo một branch
  - Sau khi làm xong thì sẽ tạo pull request để merge branch này vào development branch tổng.
  - Trong trường hợp pull request được khởi tạo, quy trình CI/CD được thiết lập sẵn sẽ chạy build, chạy test, chạy lint check và report

- Quy trình CI/CD sẽ tự động chạy build, chạy test và deploy sản phẩm
- Tiếp tục chuyển giao sản phẩm đến người dùng
</br>

***

## Quy trình làm việc điển hình

![image](https://user-images.githubusercontent.com/43572616/187832210-3f5afccc-c4dc-4ccf-ae51-90e18dec415b.png)

![1](https://user-images.githubusercontent.com/43572616/207554476-5d726066-bdd0-4e2f-9a49-61b808d00287.png)


- **Bước 1:** Tạo mới Repository. Nhất định phải có branch default là master và dev.
- **Bước 2:** Các thành viên tham gia sẽ thêm tính năng lên branch dev. Ngoại trừ người sở hữu.
- **Bước 3**: Chương trình CI/CD bắt đầu tiến hành chu trình kiểm tra code một cách tự động. Nếu vượt qua quá trình kiểm tra thành công sẽ triển khai trên server beta.
- **Bước 4:** Người có nhiệm vụ giám sát sẽ kiểm tra dữ liệu cuối cùng đã được check xong và đưa lên server beta lần nữa. Để chắc chắn rằng không còn lỗi sai nào.
- **Bước 5:** Leader của nhóm có trách nhiệm tích hợp code từ nhánh phụ sang nhánh chính.
- **Bước 6:** CI/CD tiếp tục test mã nguồn, nếu hoàn tất sẽ cho phép triển khai trên production server.
- **Bước 7:** Cuối cùng Leader thông báo cho người kiểm tra vào production để kiểm tra lần cuối. Nếu xác nhận OK sẽ cho triển khai rộng rãi. Ngược lại, ấn nút triển khai để hệ thống chủ động trở về trạng thái trước đó và thao tác lại từ đầu.
</br>

***

## Cách hoạt động

- Trong quy trình CI/CD sẽ có sự phối hợp của (1) là Git repository và (2) là CI/CD tool

- Developer tạo ra bất kỳ sự thay đổi trên Git repository (ví dụ: tạo pull request) thì Git repository sẽ phát đi thông báo đến CI/CD tool là có thay đổi như thế

- Phản hồi với thông báo, phía CI/CD sẽ tự động thực hiện các thao tác đã được cài đặt trước đó cho hành động pull request

- Sau khi thực hiện tất cả các lệnh đã được cài đặt kể trên thì CI/CD sẽ cập nhật kết quả ngược lại cho Git repository biết là pull request được tạo có vượt qua (pass) hết các quy trình (bao gồm testing) phía CI/CD hay không

- Khi review code, Reviewer chỉ cần nhìn vào trạng thái cuối cùng của pull request (passed hoặc failed) để biết pull request đã đáp ứng được chất lượng, đã tối ưu hay chưa

- Quy trình CI/CD chỉ có thể cover một phần logic, Developer vẫn phải dành thời gian để review code thủ công nhằm đảm bảo sự phù hợp với tiêu chuẩn của cả team, và vì thực tế vẫn có một số lỗi mà quá trình tự động (automation) vẫn chưa cover hết được

***

## Lợi ích

- Giảm thiểu rủi ro, nhờ việc phát hiện và sửa lỗi sớm, tăng chất lượng sản phẩm nhờ khả năng tự động kiểm tra và quan sát
- Những quy trình thủ công lặp đi lặp lại hằng ngày  được giảm tải, thay vào đó là xây dựng và kiểm thử tự động mà không cần đến sự giúp đỡ của con người.
- CI/CD có thể deploy, triển khai phần mềm ở bất cứ địa điểm và thời gian nào.
- Cho phép chúng ta tích hợp nhiều loại mã nhỏ cùng một lúc, những thay đổi mã này được thực hiện đơn giản và nhanh hơn so với những đoạn mã khổng lồ, từ đó làm giảm đi khả năng sinh ra những vấn đề liên quan đến việc thay đổi sau này
- Hệ thống CI/CD, có thể đảm bảo cho việc cách ly lỗi sẽ được phát hiện một cách nhanh chóng và dễ dàng thực hiện hơn

***

## Agile, DevOps và CI/CD

![image](https://user-images.githubusercontent.com/43572616/187832245-3c976b7e-fae8-463e-9a50-8a1653ca5aa7.png)

- CI/CD là quá trình làm việc liên tục và tự động hóa. Để quá trình kiểm thử được diễn ra liên tục cần tích hợp CI/CD trong vòng đời phát triển của phần mềm. CI/CD có mối quan hệ cực kỳ mật thiết với DevOps và Agile nhằm tạo ra một quy trình hoàn chỉnh trong phát triển và sản xuất phần mềm

- Các đội kỹ thuật sẽ bắt đầu công việc với CI
- DevOps giúp các thành viên hiểu được cấu hình và các phối hợp ra sao để xác định phần mềm nhằm tạo ra CD có giá trị hơn
- Việc thực hành CI/CD trong DevOps vào Agile sẽ thúc đẩy toàn bộ quá trình phát triển này
- CI/CD giống như một quy trình bổ sung, giúp cho việc thực hiện Agile tốt hơn. Nếu như Agile thiên về quy trình quản lý công việc thì CI/CD lại thiên về technical (kỹ thuật), giúp cho việc phát triển sản phẩm nhanh chóng hơn

- **Agile –** Công nghệ vận hành dựa trên tiến trình lặp lại theo chu kỳ. Mỗi vòng quay lặp lại có thể giải quyết tốt các tồn đọng trong chương trình, từ đó loại bỏ các rào cản, kích thích tăng trưởng nhanh, và bảo mật khá tốt

- **CI/CD –** Công nghệ hỗ trợ kiểm tra thường xuyên và liên hoàn. Quy trình hoạt động của CI/CD khá tốn kém, bù lại hiệu suất hoạt động rất tốt, đảm bảo đáp ứng công việc của doanh nghiệp một cách tự động hóa theo vòng tuần hoàn. Bên cạnh đó, CI/CD cũng có tính năng chia sẻ đến các thành viên, giúp mọi người luôn cập nhật công việc nhanh chóng

- **DevOps –** Công nghệ tập trung giải quyết các hạn chế của tài nguyên. Trách nhiệm chính của DevOps là giảm thiểu nhiều nhất tác động tiêu cực trong quá trình sản xuất, đồng thời mang lại hiệu năng và chất lượng công việc

***

## Công cụ CI/CD

- **Jenkin:**
  - công cụ CI mã nguồn mở được viết bằng Java
  - công cụ CI platform và nó cung cấp cấu hình thông qua cả giao diện GUI và các câu lệnh điều khiển.
  - Jenkin sẽ phù hợp với dự án:
    - Code lưu ở 1 server riêng
    - Muốn toàn quyền kiểm soát CI/CD
    - Yêu cầu 1 máy chủ tại chỗ
    - Yêu cầu quy trình công việc có thể tuỳ biến cao.
    - Có thể chỉ định 1 hay nhóm người quản lí và duy trì Jenkin.
    - Tiết kiệm tiền.

- **Gitlab CI/CD**
  - Một phần của dự án mã nguồn mở GitLab

  - **Đặc điểm:**
    - Công cụ có sẵn và tích hợp trên giblab mà mọi người dùng gitlab có thể sử dụng
    - Cho phép mở rộng dễ dàng vì hệ thống máy chủ nhiều
    - Cho phép lưu trữ một số tính năng Gitlab trên máy chủ và phân bố nhãn cho chúng.

  - **Phù hợp:**
    - Code lưu trên git lab
    - Bỏ qua config lằng nhằng của các công cụ khác.
    - Không cần plugin.
    - Khi cần đăng kí tích hợp docker
    - Liên tục phát hành tính năng ổn định và mình hưởng lợi từ đó
