"""
    * Chapter 1: Mô-đun và Gói trong Python
    ** MÔ-ĐUN VÀ LỢI ÍCH CỦA MÔ-ĐUN
    ** CÁCH NẠP MÔ-ĐUN ĐỂ SỬ DỤNG
    ** CẬP NHẬT NỘI DUNG CỦA MÔ-ĐUN
    ** CÁC MÔ-ĐUN CHUẨN
    ** GÓI, ĐĂNG KÝ GÓI
"""
"""
    * MÔ-ĐUN (Module) VÀ LỢI ÍCH CỦA MÔ-ĐUN.
    ** Mô-đun
    ** Lợi ích của mô-đun
    ** Lệnh import trong Python
"""
"""
    * MÔ-ĐUN 
    ** Module: Module được sử dụng để phân loại code thành các phần nhỏ hơn liên quan với nhau. Hay nói cách khác, Module giúp bạn tổ chức Python code một cách logic để giúp bạn dễ dàng hiểu và sử dụng code đó hơn.
"""
"""
    * Lợi ích của mô-đun.
    ** Tái sử dụng mã nguồn: Module cho phép bạn tái sử dụng các đoạn mã đã viết trong các chương trình khác nhau. 
    ** Tổ chức mã nguồn: Khi chương trình trở nên lớn và phức tạp, sử dụng module giúp tổ chức mã nguồn dễ dàng hơn. 
    ** Đóng gói và ẩn thông tin: Bạn có thể đóng gói các đoạn mã vào một module và chỉ để các chức năng cần thiết được sử dụng bên ngoài module. 
    ** Tích hợp và mở rộng chức năng: Khi bạn cần thêm tính năng mới vào chương trình, bạn có thể viết một module mới để mở rộng chức năng của chương trình mà không cần sửa đổi mã nguồn gốc.
    ** Hiệu suất và tối ưu hóa: Bằng cách import chỉ các module cần thiết, bạn có thể tối ưu hóa việc sử dụng bộ nhớ và hiệu suất chương trình
"""
"""
    * Lệnh import trong Python
    ** Bạn có thể sử dụng bất cứ source file nào dưới dạng như một Module bằng việc thực thi một lệnh import trong source file khác.
"""
# Import module math
import math

# Sử dụng hàm trong module math
radius = 5
area = math.pi * math.pow(radius, 2)
print("Diện tích hình tròn: ", area)

# Sử dụng một hằng số trong module math
print("Hằng số pi: ", math.pi)