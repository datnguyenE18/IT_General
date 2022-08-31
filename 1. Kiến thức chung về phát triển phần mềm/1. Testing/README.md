# Table of Content

- [Testing](#testing)
  - [Một số khái niệm](#một-số-khái-niệm)
  - [Unit test](#unit-test)
  - [Acceptance Testing](#acceptance-testing)
  - [Test hồi quy (Regression Testing)](#test-hồi-quy-regression-testing)
  - [Một số câu hỏi tuyển dụng](#một-số-câu-hỏi-tuyển-dụng)

## Testing

### Một số khái niệm

**1. Kiểm thử phần mềm (Software Testing):**

- Kiểm thử phần mềm là quá trình thực thi 1 chương trình với mục đích tìm ra lỗi.
- Kiểm thử phần mềm đảm bảo sản phẩm phần mềm đáp ứng chính xác, đầy đủ và đúng theo yêu cầu của khách hàng, yêu cầu của sản phẩm đề đã đặt ra.
- Kiểm thử phần mềm cũng cung cấp mục tiêu, cái nhìn độc lập về phần mềm, điều này cho phép việc đánh giá và hiểu rõ các rủi ro khi thực thi phần mềm.
- Kiểm thử phần mềm tạo điều kiện cho bạn tận dụng tối đa tư duy đánh giá và sáng tạo để bạn có thể phát hiện ra những điểm mà người khác chưa nhìn thấy.

**2. Kiểm thử hộp đen (Black box testing):**

- Kiểm thử hộp đen là 1 phương pháp kiểm thử mà tester sẽ chỉ xem xét đến đầu vào và đầu ra của chương trình mà không quan tâm code bên trong được viết ra sao. Tester thực hiện kiểm thử dựa hoàn toàn vào đặc tả yêu cầu . Mục đích của kiểm thử hộp đen là tìm ra các lỗi ở giao diện , chức năng của phần mềm. Các trường hợp kiểm thử sẽ được xây dựng xung quanh đó.

**3. Kiểm thử hộp trắng( White box testing):**

- Kiểm thử hộp trắng là phương pháp kiểm thử mà cấu trúc thuật toán của chương trình được đưa vào xem xét. Các trường hợp kiểm thử được thiết kế dựa vào cấu trúc mã hoặc cách làm việc của chương trình. Người kiểm thử truy cập vào mã nguồn của chương trình để kiểm tra nó.

**4. Kiểm thử đơn vị (Unit test):**

- Kiểm thử đơn vị là hoạt động kiểm thử nhỏ nhất. Kiểm thử thực hiện trên các hàm hay thành phần riêng lẻ.
- Đây là 1 công việc mà để thực hiện được nó thì người kiểm thử sẽ phải hiểu biết về code, về chương trình, các hàm, ...
- Mục đích của việc thực hiện kiểm thử đơn vị là cô lập từng thành phần của chương trình và chứng minh các bộ phận riêng lẻ chính xác về các yêu cầu chức năng.

**5. Kiểm thử tích hợp(Intergration test):**

- Như chúng ta đã biết, một phần mềm được tạo ra sẽ bao gồm rất nhiều module trong đó, để chắc chắn rằng phần mềm hoạt động tốt thì chúng ta cần phải gom các module lại với nhau để kiểm tra sự giao tiếp giữa các module cũng như bản thân từng thành phần từng module.. Kiểm thử tích hợp bao gồm 2 mục tiêu chính là :
  - Phát hiện lỗi giao tiếp xảy ra giữa các Unit
  - Tích hợp các Unit đơn lẻ thành các hệ thống nhỏ và cuối cùng là 1 hệ thống hoàn chỉnh để chuẩn bị cho bước kiểm thử hệ thống.

**6. Kiểm thử hệ thống( System test):**

- Kiểm thử 1 hệ thống đã được tích hợp hoàn chỉnh để xác minh rằng nó đáp ứng được yêu cầu Kiểm thử hệ thống thuộc loại kiểm thử hộp đen . Kiểm thử hệ thống tập trung nhiều hơn vào các chức năng của hệ thống . Kiểm tra cả chức năng và giao diện , các hành vi của hệ thống 1 cách hoàn chỉnh, đáp ứng với yêu cầu.

**7. Kiểm thử chấp nhận( Acceptance test):**

- Trong kiểu kiểm thử này, phần mềm sẽ được thực hiện kiểm tra từ người dùng để tìm ra nếu phần mềm phù hợp với sự mong đợi của người dùng và thực hiện đúng như mong đợi. Trong giai đoạn test này, tester có thể cũng thực hiện hoặc khách hàng có các tester của riêng họ để thực hiện.
</br>

- Có 2 loại kiểm thử chấp nhận đó là kiểm thử Alpha và kiểm thử Beta:
  - **Kiểm thử Alpha:** là loại kiểm thử nội bộ . Tức là phần mềm sẽ được 1 đội kiểm thử độc lập hoặc do khách hàng thực hiện tại nơi sản xuất phần mềm.
  - **Kiểm thử Beta:** là loại kiểm thử mà khách hàng thực hiện kiểm thử ở chính môi trường của họ. Loại kiểm thử này được thực hiện sau kiểm thử Alpha.

**8. Kiểm thử chức năng ( Functional testing):**

- Kiểm thử chức năng là một loại kiểm thử hộp đen (black box) và các trường hợp kiểm thử của nó được dựa trên đặc tả của ứng dụng phần mềm/thành phần đang test. Các chức năng được test bằng cách nhập vào các giá trị nhập và kiểm tra kết quả đầu ra, và ít quan tâm đến cấu trúc bên trong của ứng dụng (không giống như kiểm thử hộp trắng - white-box testing).
</br>

- Có thể hiểu 1 cách đơn giản, kiểm thử chức năng là xác nhận tất cả các chức năng của hệ thống. Nó đánh giá ứng dụng và xác nhận liệu ứng dụng có đang hoạt động theo yêu cầu hay không.

**9. Kiểm thử phi chức năng( Non Functional testing):**

- Loại kiểm thử này tập trung vào các khía cạnh phi chức năng của ứng dụng. Vậy những khía cạnh phi chức năng là những gì? Hay tôi nên nói những tính năng mà không liên quan đến các chức năng của ứng dụng là gì? Tôi nghĩ nó sẽ bao gồm:
  - Kiểm thử chịu tải
  - Kiểm thử bảo mật
  - Kiểm tra tính tương thích trên từng môi trường,...

**10. Test cấu hình (Shakeout testing):**

- Kiểu kiểm thử này cơ bản là kiểu kiểm thử về khả năng của hệ thống mạng, kết nối dữ liệu và sự tương tác của các module. Thông thường thì kiểu test này là do nhóm quản lý cấu hình chuẩn bị thiết lập các môi trường test thực sự. Họ cũng kiểm tra xem liệu các thành phần chính của phần mềm có hoạt động bất thường không. Kiểu kiểm thử này thực hiện trước khi tiến hành thực hiện trong môi trường test. Sau khi test shakeout, bước kế tiếp là test smoke (kiểu test được thực hiện bởi tester sau khi biên dịch, được tiến hành trong môi trường test).

**11. Smoke testing:**

- Smoke Testing là 1 quá trình để kiểm tra liệu bản build có ổn định hay không? Để xem bản build có đủ ổn định để thực hiện test chi tiết hay không (trong trường hợp bản build ko ổn định, lỗi luôn chức năng chính hoặc build bị lỗi thì trả lại Dev, yêu cầu sửa luôn). Hay kiểm tra các tính năng quan trọng có đang hoạt động hay không . Nó là 1 bài test hồi quy nhỏ đơn giản và nhanh của các chức năng chính, cho thấy sản phẩm đã sẵn sàng cho việc test hay chưa.

**12. Ad hoc testing:**

- Thuật ngữ Adhoc testing là phương pháp kiểm thử dạng Black box test mà không theo cách thông thường. Với quy trình test thông thường là phải có tài liệu yêu cầu, kế hoạch test ( test plan), kịch bản kiểm thử. Kiểu test này không theo bất cứ loại kỹ thuật test nào để tạo testcase.

**13. Monkey testing:**

- Monkey testing được định nghĩa rất ngắn gọn: là một phương pháp kiểm thử với đầu vào ngẫu nhiên, không theo testcase hay một chiến lược test nào.
</br>

- Trong Monkey testing thì các tester ( đôi khi cả developer nữa ) được coi như là 1 con khỉ vậy  Bạn thử nghĩ mà xem, nếu 1 con khỉ mà sử dụng máy tính thì nó sẽ làm những gì nhỉ? Tuy loài khỉ rất thông minh nhưng khi cho nó sử dụng máy tính, nó sẽ thực hiện những hành động bất kỳ trên hệ thống , điều mà chính nó cũng không thể hiểu được. Nó cũng giống như khi tester thực hiện monkey testing, họ sẽ áp dụng các kịch bản kiểm thử ngẫu nhiên trên hệ thống để tìm ra lỗi mà không cần xác định trước. Trong 1 số trường hợp, Monkey testing chỉ dành cho Unit Testing hoặc GUI Testing( Kiểm thử giao diện người dùng)

**14. Kiểm thử hiệu suất (Performance testing):**

- Trong loại test này, ứng dụng được test dựa vào sức nặng như sự phức tạp của giá trị, độ dài của đầu vào, độ dài của các câu truy vấn…Loại test này kiểm tra bớt phần tải (stress/load) của ứng dụng có thể được chắc chắn hơn.

**15. Kiểm thử hồi quy (Regression testing):**

- Test hồi quy là test lại 1 chức năng đã được làm xong, đã được test xong rồi, đã hết lỗi nhưng do có sự sửa đổi 1 chức năng khác mà lại có ảnh hưởng đến nó, thì phải test 1 chức năng đã xong rồi thì gọi là test hồi quy.
</br>

- Ví dụ có 3 chức năng A B C đã hoàn thành, 3 chức năng này đều có mối quan hệ với nhau và chức năng A cần phải sửa đổi thêm về nghiệp vụ, việc sửa chức năng A này sẽ làm ảnh hưởng đến chức năng B, C và việc phải test lại chức năng B và C thì gọi là test hồi quy . Hoặc khi Dev sửa 1 chức năng mà chức năng này có làm ảnh hưởng đến chức năng đã xong rồi thì cũng phải thực hiện test lại chức năng đã xong rồi kia thì gọi là test hồi quy
</br>

- Hoặc ngay cả khi re- test để đóng bug, mà thấy chức năng Developer sửa có thể làm ảnh hưởng đến 1 chức năng khác đã xong rồi thì tester cũng nên test hồi quy lại chức năng đó để tránh có lỗi tiềm ẩn mà ko biết.

**16. Re-test:**

- Re-test là thực hiện test để đóng bug/ defect / lỗi sau khi lập trình viên đã được sửa hoặc sửa 1 chức năng nào đó rồi test lại chức năng sửa đó thì gọi là test lại hoặc 1 chức năng cần re -test vài lần cho hết bug

**17. Bug:**

- Là một khiếm khuyết trong một thành phần hoặc hệ thống mà nó có thể làm cho thành phần hoặc hệ thống này không thực hiện đúng chức năng yêu cầu của nó, ví dụ như thông báo sai hoặc định nghĩa dữ liệu không đúng. Một bug, nếu gặp phải trong quá trình hệ thống hoạt động, có thể gây ra failure trong thành phần hoặc hệ thống đó.

**18. Testcase:**

- Test case là mô tả một dữ liệu đầu vào, hành động và một kết quả mong đợi (expected result) để xác định một chức năng của ứng dụng phần mềm hoạt động đúng hay không.
</br>

- Test case thường được viết trên excel. Một file Testcase cơ bản cần có các trường sau: TestcaseID, mục tiêu test, các bước thực hiện test, và kết quả trả về (expected result) có đúng với yêu cầu test không.Ngoài ra còn có thể có thêm điều kiện tiên quyết và dữ liệu test.
</br>

- Để viết được testcases có hiệu quả bao phủ hết các trường hợp cần test thì testcases phải có đầy đủ hết các Nghiệp vụ mà hệ thống yêu cầu (các yêu cầu trong tài liệu Đặc tả ko được bỏ sót, sử dụng các kỹ thuật thiết kế test case (các kỹ thuật test hộp đen) để viết được test case có độ bao phủ tối đa.

**19. Testplan:**

- Test plan chính là tài liệu tổng quan về việc kiểm thử 1 project: phạm vi kiểm thử, hướng tiếp cận, quy trình kiểm thử, tài nguyên và nhân lực test cần có, các chức năng/ module cần được test, các công cụ và môi trường test cần có.
</br>

- Bao gồm cả kế hoạch ai test chức năng nào, khi nào bắt đầu thực hiện viết và hoàn thành testcases, khi nào bắt đầu thực hiện test và kế hoạch hoàn thành test
</br>

- Dựa vào kế hoạch chung của dự án để lên kế hoạch cho bên kiểm thử. Trong trường hợp khi làm thực tế thấy có khả năng không đúng như kế hoạch đã lên thì phải báo cáo lại test leader hoặc Quản trị dự án sớm.

***

### Unit test

- Unit Test hay Kiểm thử đơn vị là một loại kiểm thử phần mềm mà trong đó, các đơn vị hoặc thành phần riêng lẻ của phần mềm sẽ được kiểm tra nhằm xác định sự phù hợp của chúng với các thông số kỹ thuật được thiết kế, dữ liệu liên quan và quy trình sử dụng. Quá trình kiểm thử đơn vị là bắt buộc phải có trong mọi quá trình phát triển của ứng dụng.
</br>

- Kiểm thử phần mềm chia làm 4 mức độ khác nhau theo thứ tự gồm: SDLC, STLC, V Model và Unit Test. Trong đó, Unit Test nằm ở mức độ thấp nhất và được thực hiện trước khi kiểm tra tích hợp
</br>

- Unit Test được thực hiện trong quá trình phát triển hay giai đoạn lập trình của một ứng dụng bởi các nhà phát triển. Quy trình kiểm thử này sẽ tách một phần code và xác minh tính đúng đắn của nó.
</br>

- Bản chất của Unit Test là tập trung vào một đơn vị nên không thể áp dụng để tìm kiếm các lỗi tích hợp hoặc lỗi cấp hệ thống.
</br>

- Các nhà phát triển phần mềm luôn cố gắng tiết kiệm thời gian nhất có thể bằng cách thực hiện ít các kiểm thử nhất có thể. Nhưng đây cũng chính là nguyên nhân dẫn đến chi phí sửa lỗi cao trong quá trình kiểm tra hệ thống, kiểm tra tích hợp và thậm chí thử nghiệm. Vì vậy, nếu Unit Test được thực hiện sớm trong quá trình phát triển phần mềm sẽ giúp tiết kiệm thời gian và tiền bạc
</br>

- Unit Test được tạo có 3 trạng thái cơ bản gồm:
  - **Trạng thái lỗi:** Fail
  - **Trạng thái tạm dừng thực hiện:** Ignore
  - **Trạng thái làm việc:** Pass

</br>

- **Để Unit Test có thể hoạt động và mang lại hiệu quả:**
  - Unit Test cần được vận hành lặp lại nhiều lần.
  - Unit Test cần được thiết lập chế độ tự động
  - Unit Test này phải hoạt động độc lập với những Unit Test khác.
</br>

- **Trình tự thiết kế:**
  - Thực hiện thiết lập những điều kiện cần thiết: khởi tạo các đối tượng, xây dựng dữ liệu giả, xác định tài nguyên cần thiết,…
  - Gọi các phương thức cần kiểm tra.
  - Kiểm tra các phương thức xem có hoạt động chính xác hay không
  - Dọn dẹp tài nguyên ngay sau khi quá trình kiểm tra kết thúc.
</br>

- Unit Test cần phải nhanh, vì Unit Test sẽ được chạy để kiểm định lỗi mỗi lần build. Do đó, trong Unit Test phải hạn chế các nhiệm vụ tốn thời gian như gọi I/O, database, network,…
</br>

- Luôn đảm bảo lỗi phải được xác định trong quá trình Unit Test được sửa trước khi chuyển sang giai đoạn tiếp theo.
</br>

- Nếu không thực hiện Unit Test, các lỗi được tìm thấy ở các giai đoạn sau sẽ càng nhiều và lỗi ngày càng phức tạp, tốn rất nhiều thời gian và chi phí để sửa chữa. Vì vậy, hãy thực hiện Unit Test ngay từ đầu
</br>

- Unit Test thường được thực hiện bởi lập trình viên. Công đoạn này cần được thực hiện càng sớm càng tốt trong giai đoạn viết code và phải xuyên suốt chu kỳ phát triển phần mềm. Mặc khác, Unit Test đòi hỏi các kiểm tra viên phải có kiến thức về thiết kế và code của chương trình.
</br>

- **Một số thuật ngữ:**
  - **Assertion**: Là các công việc kiểm tra cần tiến hành, thí dụ: AreEqual(), IsTrue(), IsNotNull()… Mỗi một UT gồm nhiều assertion để kiểm tra dữ liệu đầu ra, tính chính xác của các lỗi ngoại lệ ra và các vấn đề phức tạp khác.
  - **Test Point**: Là một đơn vị kiểm tra nhỏ nhất, chỉ chứa một assertion . Mọi thành viên dự án đều có thể viết một test point.
  - **Test Case:** Là một tập hợp các test point nhằm kiểm tra một đặc điểm chức năng cụ thể. Trong nhiều trường hợp kiểm tra đặc biệt và khẩn cấp có thể không cần đến test case.
  - **Test Suite**: Là một tập hợp các test case định nghĩa cho từng module hoặc hệ thống con.
  - **Regression Testing (hoặc Automated Testing)**: Là phương pháp kiểm nghiệm tự động sử dụng một phần mềm đặc biệt. Cùng một loại dữ liệu kiểm tra giống nhau nhưng được tiến hành nhiều lần lặp lại tự động nhằm ngăn chặn các lỗi cũ phát sinh trở lại. Kết hợp Regression Testing với Unit Testing sẽ đảm bảo các đoạn mã mới vẫn đáp ứng yêu cầu thay đổi và các đoạn mã cũ sẽ không bị ảnh hưởng bởi các hoạt động bảo trì.
  - **Production Code**: Phần mã chính của ứng dụng được chuyển giao cho khách hàng.
  - **Unit Testing Code**: Phần mã phụ để kiểm tra mã ứng dụng chính, không được chuyển giao cho khách hàng.

![image](https://user-images.githubusercontent.com/43572616/187674926-ed8a730e-8318-48c3-b2b4-63ec1e963ede.png)

**Test case:**

là các trường hợp cần kiểm thử với đầu vào và đầu ra được xác định cụ thể. Một test case thường có hai thành phần:

- Expected value: Giá trị mong đợi khối lệnh trả về
- Actual value: Giá trị thực tế mà khối lệnh trả về. Sau khi thực hiện khối lệnh cần kiểm thử, sẽ nhận được actual value. Lấy giá trị đó so sánh với expected value. Nếu hai giá trị này trùng khớp nhau thì kết quả của test case là PASS. Ngược lại, kết quả là FAIL.

**Phân loại test case:**

- Positive test case: Là những trường hợp kiểm thử đảm bảo người dùng có thể thực hiện được thao tác với dữ liệu hợp lệ.
- Negative test case: Là những trường hợp kiểm thử tìm cách gây lỗi cho ứng dụng bằng cách sử dụng các dữ liệu không hợp lệ.

**Cấu trúc một test case:**

Các trúc mã cần tuân thủ trong một test case là cấu trúc AAA. Cấu trúc này gồm 3 thành phần:

- Arrange – Chuẩn bị dữ liệu đầu vào và các điều kiện khác để thực thi test case.
- Act – Thực hiện việc gọi phương thức/hàm với đầu vào đã được chuẩn bị ở Arrange và nhận về kết quả thực tế.
- Assert – So sánh giá trị mong đợi và giá trị thực tế nhận được ở bước Act.

Kết quả của test case sẽ là một trong hai trạng thái sau:

- PASS: nếu kết quả mong đợi và kết quả thực tế khớp nhau
- FAIL: nếu kết quả mong đợi khác với kết quả thực tế

Đôi khi bắt gặp một số bài viết dùng từ cấu trúc Given-When-Then. Về bản chất, cũng chính là cấu trúc AAA như trên.

***

### Acceptance Testing

- Acceptance Testing là một trong 4 mức độ kiểm thử và cũng là bước cuối cùng trước khi sản phẩm được đưa ra hoạt động hoặc trước khi phân phối sản phẩm phải được chấp nhận.

- Là một kiểm thử nhằm xác định hệ thống phần mềm có đạt yêu cầu kỹ thuật hay không. Bằng việc kiểm tra các hành vi của hệ thống qua dữ liệu thực tế, kiểm thử chấp nhận sẽ xác định có hay không việc hệ thống đáp ứng được các tiêu chí lẫn yêu cầu của khách hàng

- **User Acceptance Testing (UAT)** – Kiểm thử chấp nhận của người dùng có nghĩa là kiểm thử xem phần mềm đã thỏa mãn tất cả yêu cầu của khách hàng và khách hàng chấp nhận sản phẩm (và trả tiền thanh toán hợp đồng)

![image](https://user-images.githubusercontent.com/43572616/187674980-10a1873e-c0e4-43e8-9de8-45d9c2c50e19.png)

- **Điều kiện tiên quyết của Acceptance Testing**
  - Phải đảm bảo các yêu cầu nghiệp vụ chính của ứng dụng hoạt động
  - Phần mềm đã được hoàn thiện nhất
  - Các khâu kiểm thử Unit testing, integration testing, system testing đã được hoàn thành
  - Không có lỗi quan trọng còn tồn tại trong hệ thống
  - Lỗi về thẩm mỹ được chấp nhận trước UAT
  - Regression testing phải được hoàn thành và không có lỗi lớn
  - Tất cả các lỗi đã phát hiện phải được sửa và kiểm tra trước khi UAT
  - Môi trường Acceptance Testing phải được chuẩn bị sẵn sàng
  - Nhà phát triển phải chắc chắn rằng hệ thống đã sẵn sàng thực hiện Acceptance Testing

</br>

- **Các bước thực hiện Acceptance Testing**
  - Phân tích các yêu cầu nghiệp vụ của phần mềm
  - Tạo kế hoạch kiểm tra Acceptance Testing
  - Xác định các kịch bản kiểm thử
  - Tạo các trường hợp kiểm tra Acceptance Testing
  - Chuẩn bị data test (giống với data thật nhất)
  - Thực hiện kiểm thử
  - Ghi nhận kết quả
  - Xác nhận các chức năng của sản phẩm

![image](https://user-images.githubusercontent.com/43572616/187675022-39993cf1-a0c3-4c75-a47a-d07b28724b4f.png)

- Kiểm thử chấp nhận xác định xem tất cả những chức năng chính đều hoạt động tốt. Nếu người dùng tìm thấy bug ở những chức năng chính thì tester sẽ phải xem xét lại test case, tìm hiểu nguyên nhân tại sao xảy ra bug đó.
</br>

- Đây cũng là cơ hội để tìm thấy lỗi còn tồn tại trong hệ thống
</br>

- Kiểm thử chấp nhận được chia làm hai loại: thử nghiệm Alpha và Beta
</br>

- Hầu hết trong một dự án phát triển phần mềm thường thì UAT được thực hiện trong môi trường đảm bảo chất lượng nếu không có môi trường dàn dựng hoặc môi trường Acceptance Testing

***

### Test hồi quy (Regression Testing)

- Kiểm thử hồi quy là một hình thức kiểm thử phần mềm để xem các chức năng cũ và mới của nó có còn hoạt động đúng sau khi thay đổi hệ thống hay không
</br>

- **Khi nào thì cần kiểm thử hồi quy**
  - Chẳng hạn, một ứng dụng phần mềm có thể cho phép giáo viên thêm, lưu, xóa và làm mới trong một công cụ học tập trực tuyến. Sau đó, các Developer deploy 1 version mới với chức năng bổ sung để cập nhật. Chức năng mới được kiểm tra để xác nhận rằng bản cập nhật hoạt động như mong đợi. Trong trường hợp này, kiểm tra hồi quy có thể cải thiện chất lượng tổng thể của sản phẩm.

</br>

- Sau khi phần mềm thay đổi, điều quan trọng là đảm bảo không làm hỏng bất cứ thứ gì. Ngay cả sau khi phát hiện và sửa lỗi hồi quy, vẫn cần phải thử nghiệm thêm. Cần xác nhận rằng việc xử lý một lỗi không gây ra các vấn đề khác.
</br>

- Thử nghiệm hồi quy là cần thiết, ngay cả khi thực hiện các thay đổi rất nhỏ đối với code.
</br>

- Kiểm tra hồi quy cũng thường được thực hiện bất cứ khi nào một vấn đề được phát hiện trước đó đã được khắc phục. Sau tất cả, có nhiều người phụ thuộc kiểm tra khi nào hoặc không mã mới tuân thủ mã cũ và mã không được sửa đổi đó không bị ảnh hưởng.
</br>

- Sau mỗi ngày, hàng tuần, hai tuần một lần, v.v ... Nói chung, thực hiện kiểm tra hồi quy, nên có một lịch trình. Kiểm tra thường xuyên có nghĩa là ứng dụng sẽ trở nên ổn định hơn và sẵn sàng sản xuất., Kiểm tra hồi quy càng thường xuyên xảy ra, càng có nhiều vấn đề có thể được phát hiện và giải quyết.
</br>

- Các thử nghiệm được tiến hành trước đây nên chạy lại và kết quả của chúng có thể được so sánh với các kết quả thử nghiệm hiện tại.
</br>

- **Các phương pháp thử nghiệm hồi quy thích hợp**

    Thông thường có 3 phương pháp để kiểm tra hồi quy:

![image](https://user-images.githubusercontent.com/43572616/187675056-f00bd087-859a-4499-b20e-2b63f87233f2.png)

- Kiểm tra lại tất cả: Điều này giúp kiểm tra lại tính toàn vẹn của phần mềm từ trên xuống dưới.
</br>

- Lựa chọn kiểm tra hồi quy: Phương pháp này cho phép chọn một lựa chọn đại diện cho các thử nghiệm sẽ xấp xỉ một thử nghiệm đầy đủ. Điều này đòi hỏi ít thời gian hoặc chi phí hơn nhiều so với bộ thử nghiệm đầy đủ
</br>

- Ưu tiên cho trường hợp thử nghiệm: Với các trường hợp thử nghiệm hạn chế, hãy thử ưu tiên các thử nghiệm có thể ảnh hưởng đến cả bản dựng hiện tại và tương lai của phần mềm.

***

### Một số câu hỏi tuyển dụng

**Ví dụ:** Các lập trình viên thường viết và thực hiện unit test đối với những dòng code mà họ đã viết. Trong hoạt động tự testing này thì lập trình viên có thể áp dụng tư duy của kiểm thử nào để có hiệu quả?

**Ví dụ 2:** "Lỗi tiềm ẩn chức năng" được thực hiện đánh giá trong giai đoạn nào của quy trình phát triển phần mềm?

**Bạn biết bao nhiêu phương pháp kiểm thử phần mềm?**

Kiểm thử hộp đen: Dùng khi test theo yêu cầu, tiêu chí của khách hàng, đưa ra các chức năng hệ thống.

Kiểm tra hộp trắng: Kiểm tra về các thuật toán, mã code, cấu trúc của chương trình.

**Để phát triển phần mềm cần những giai đoạn nào?**

Để phát triển phần mềm sẽ cần qua 4 giai đoạn chính. Bao gồm:

- Unit testing: Kiểm thử đơn vị.
- Integration testing: Kiểm thử tích hợp.
- System testing: Kiểm thử hệ thống.
- Acceptance testing: Công nhận kiểm thử.

**Giai đoạn nào thường xuất hiện lỗi khi phát triển phần mềm?**

Thông thường, lỗi sẽ xuất hiện ở giai đoạn làm việc sau khi lập trình viên code xong phần mềm và chuyển cho Tester. Quá trình testing và gỡ lỗi (bug) thường được diễn ra song song song với nhau. Do đó, đây là giai đoạn thường phát sinh nhiều lỗi nhất.

**Kiểm thử hệ thống là gì?**

System Testing (kiểm thử hệ thống) nghĩa là test toàn bộ hệ thống. Trong đó, tất cả các module/components được tích hợp theo thứ tự để xác minh rằng hệ thống làm việc đúng hay không. Quá trình này được thực hiện sau Integration Testing và đóng vai trò quan trọng trong việc phát hành một sản phẩm chất lượng cao.

***Có mấy phương pháp kiểm thử phần mềm?***

Nhìn tổng thể, hiện có 2 phương pháp chính :

- Kiểm tra thủ công (Manual Testing) do người phụ trách QA đảm nhận
- Kiểm tra tự động (Automation Testing) sử dụng các công cụ, lệnh và các phần mềm khác để chạy các hành động được xác định trước.

***Phân biệt giữa bug, defect và error ?***

- Bug là lỗi trong phần mềm được phát hiện trong thời gian thử nghiệm. Đây là những lỗi nghiêm trọng có thể chặn một chức năng, dẫn đến sự cố hoặc gây tắc nghẽn hiệu suất
- Defect là sự sai sót giữa kết quả mong đợi và kết quả thực tế, phát hiện sau khi sản phẩm đi vào sản xuất.
- Error là lỗi gây ra do sự hiểu nhầm, hiểu sai thông tin, ký hiệu giữa các bên tham gia thiết kế phần mềm (gồm kỹ sư phần mềm, lập trình viên, nhà phân tích và tester) , những người này đều là nhân sự của công ty phần mềm.

***Kiểm tra có thể thực hiện ở bất kỳ giai đoạn nào, đúng không?***

Kiểm tra hệ thống đòi hỏi tính đồng bộ ở tất cả các thành phần trong phần mềm. Do vậy, phải đợi tất cả các mã lệnh được cài đặt, phần mềm đã có thể vận hành bình thường thì việc kiểm tra mới có thể tiến hành

![image](https://user-images.githubusercontent.com/43572616/187675099-05c26818-e574-4a79-9646-8d08b55e7128.png)

![image](https://user-images.githubusercontent.com/43572616/187675126-ced870a2-3628-4d7d-966c-543afe1b3399.png)
![image](https://user-images.githubusercontent.com/43572616/187675145-cc851c28-98ed-4723-8fd4-5b41fb386dde.png)
