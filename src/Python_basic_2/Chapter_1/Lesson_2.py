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