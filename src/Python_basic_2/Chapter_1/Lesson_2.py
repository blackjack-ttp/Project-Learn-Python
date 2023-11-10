# 2.1.Nạp luôn cả mô-đun ?
# Bạn có thể sử dụng bất cứ source file nào dưới dạng như một Module bằng việc thực thi một lệnh import trong source file khác
import my_module

# Su dung ham greet tu module my_module
name="BlackJack"
greeting=my_module.greet(name)
print(greeting)

# Su dung ham add tu module my_module
result=my_module.add(5, 10)
print("Tong cua 2 so la: ", result)

# 2.2.Nạp từng thành phần của mô-đun
# Lệnh from…import được sử dụng để import thuộc tính cụ thể từ một Module. Trong trường hợp mà bạn không muốn import toàn bộ Module nào đó thì bạn có thể sử dụng lệnh này
# Import chỉ một hàm từ module math
from math import sqrt

# Sử dụng hàm sprt mà không cần thêm tiền tố math
number=25
square_root=sqrt(number)
print('Căn bậc hai của ', number, 'là: ', square_root)

# 2.3. Nạp hết tất cả thành phần
# Sử dụng lệnh from … import *
# Sử dụng lệnh này, bạn có thể import toàn bộ Module. Do đó bạn có thể truy cập các thuộc tính trong Module này
# Import tất cả thành phần từ module math
from math import *
# Sử dụng các hàm trong module math
print("Giá trị của pi: ", pi)
print("Sinh của 1: ", sinh(1))

# 2.4. Nạp mô-đun và sử dụng với tên khác
# Sử dụng lệnh import as
# Bằng cách sử dụng as, bạn có thể tắt ngắn cú pháp khi sử dụng các thành phần của module, giúp làm cho mã của bạn gọn gàng hơn và giảm thiểu khả năng xảy ra xung đột tên.
# Import module math voi ten ngan gon la m
import math as m

# su dung ham trong module math
x=10
y=20
gcd=m.gcd(x,y)
print('Uoc chung lon nhat cua ', x, 'va', y, 'la:', gcd)