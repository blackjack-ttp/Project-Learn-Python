# Đếm số lượng phần tử
names = ['An', 'Hòa', 'Hồng', 'Phước', 'Phong', 'Quang']
print(len(names)) #Output: 6

# Kiểm tra tồn tại của phân tử
# Cách 1
numbers = [1, 2, 3, 4, 4, 5, 3]
try:
    index = numbers.index(3)
    print("Phần tử 3 tồn tại trong danh sách ở vị trí", index)
except ValueError:
    print("Không tồn tại phần tử 3 trong danh sách")
    
# Cách 2
if 3 in numbers:
    print("Phần tử 3 tồn tại trong danh sách")
else:
    print("Không tồn tại phần tử 3 trong danh sách")

# Kiểm tra sự tồn tại của phân tử trong chuỗi
text = "Hello world"
if "world" not in text:
    print("Phần tử 'world' không tồn tại trong chuỗi")
else:
    print("Phần tử 'world' tồn tại trong chuỗi")
    
# Kiểm tra số lần xuất hiện của phần tử trong danh sách
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
count_3 = numbers.count(3)
if count_3 > 0:
    print("Phân tử 3 tồn tại trong danh sách và xuât hiện", count_3, "lần.")
else:
    print("Không tồn tại phần tử 3 trong danh sách")