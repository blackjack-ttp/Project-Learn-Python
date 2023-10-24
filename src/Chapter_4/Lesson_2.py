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

# Trich xuat mang con
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[:2]) #Tu vi tri 0 den 1
print(numbers[0:3]) #Tu vi tri 0 den 2
print(numbers[2:5]) #Tu vi tri 2 den 4

# Xoa phan tu mang
numbers = [1, 2, 3, 4, 5, 6, 7]
## Xoa phan tu thu 2 (chi muc 1) khoi mang
del numbers[1]
print(numbers) #Out: [1, 3, 4, 5, 6, 7]
## Xoa nhieu phan tu tu chi muc 1 den 3 (khong bao gom chi muc 3)
del numbers[1:3]
print(numbers) #Out: [1, 5, 6, 7]

## Xoa phan tu co gia tri la 2 khoi mang (chi xoa phan tu dau tien co gia tri 2)
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.remove(2)
print(numbers)

## Xoa phan tu co chi muc 2 khoi mang va tra ve gia tri da xoa
numbers = [1, 2, 3, 4, 5, 6, 7]
delete_value = numbers.pop(2)
print(numbers)
print('Phan tu da xoa', delete_value)

## Xoa phan tu cuoi cung cua mang va tra ve gia tri da xoa
delete_value = numbers.pop()
print(numbers)
print('Phan tu da xoa', delete_value)

# Noi 2 mang
array1=[1,2,3,4]
array2=[5,6,7,8]
## Noi 2 mang bang toan tu cong
result_array = array1 + array2
print(result_array)
## Noi 2 mang bang phuong thuc extend()
array1.extend(array2)
print(array1)
## Noi mang 2 vao mang 1 bang phuong thuc append()
for element in array2:
    array1.append(element)
print(array1)

# Dao nguoc mang
numbers = [1,2,3,4,5]
## Su dung phuong thuc revere() de dao nguoc mang
numbers.reverse()
print(numbers)

# Sap xep
numbers=[2,4,6,3,4,5,6,7,2,1,9,0]
## Sap xep theo thu tu tang dan (Mặc định)
numbers.sort()
print('Mang da duoc sap xep: ',numbers)
## Sắp xếp theo thứ tự giản dần
numbers=[2,4,6,3,4,5,6,7,2,1,9,0]
numbers.sort(reverse=True)
print('Mang da duoc sap xep: ',numbers)

# Duyệt cách phần tử trong mảng
numbers = [1,3,6,4,5,8,5]
for i in numbers:
    print(i)
is_decreasing=True
for i in range(0, len(numbers)) :
    print('Vị Trí: ' + str(i) + ' có giá trị là: ' + str(numbers[i]))