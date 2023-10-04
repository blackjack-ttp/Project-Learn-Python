# Learn variables for Python programming
# The data type of the variable ( Kiểu dữ liệu của biến)

# int (số nguyên)
age = 25
number_of_students = -10

# float (số thực)
pi = 3.14159
height = 1.75

# str (Chuỗi) Kiểu dữ liệu chuỗi chứa một chuỗi các ký tự, được đặt trong dấu nháy đơn hoặc dấu nháy kép.
name = "Trần Thanh Phong"
message = 'Hello, world'

# bool (Boolean) trả giá trị true or false
is_student = False
is_about =      True

# list (Danh sách) Kiểu dữ liệu danh sách chứa một tập hợp các phần tử, các phần tử có thể là bất kỳ kiểu dữ liệu nào và được đặt trong dấu ngoặc vuông [].
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fruits = ['apple', 'orange', 'banana']

# dictionary (Từ điển) Kiểu dữ liệu từ điển chứa các cặp khóa-giá trị, trong đó mỗi khóa phải là duy nhất và không thay đổi, và được đặt trong dấu ngoặc nhọn {}.
student = {'name': "Trần Thanh Phong", "age": 25, 'gender': 'male'}

# set (Tập hợp) Kiểu dữ liệu tập hợp chứa một tập hợp các phần tử duy nhất và không có thứ tự, và được đặt trong dấu ngoặc nhọn {}.
primes = {2, 3, 4, 5, 6, 7, 8, 9}

# tuple (Bộ) Kiểu dữ liệu bộ chứa một tập hợp các phần tử không thay đổi, và được đặt trong dấu ngoặc đơn ().
point = (10, 20)

# None (NoneType) Kiểu dữ liệu NoneType chứa giá trị đặc biệt None, biểu thị không có giá trị hoặc giá trị không xác định
result = None

# Change the value of the variable (Thay đổi giá trị của biến)
x = 10
print('--1--Change the value of the variable: ', x)
x = 20
print('--2--Change the value of the variable: ', x)
print("================================================================")

# Assign multiple values to variables (Gán nhiều giá trị cho biến)
q = w = e = 10
print('result --1--', q)
print('result --2--', w)
print('result --3--', e)
print("================================================================")

# Biến toàn cục và cục bộ
# Biến toàn cục
global_var=10
def my_function():
    # Biến cục bộ
    local_var=20
    # Có thể truy cập vào biến toàn cục
    print(global_var)
    # Chỉ có thể truy cập vến cục bộ trong hàm
    print(local_var)
my_function()
print("================================================================")

# Arithmetic operators (Toán tử số học)
a = 1
b = 2
S = a + b
H = a - b
T = a * b
Th = a / b
print('Total: ', S)
print('Brand: ', H)
print('Tich: ', T)
print('Spear: ', Th)
print("================================================================")

# Kiểu dữ liệu boolearn
is_student=False
is_adult=True
print('Is student: ', is_student)
print('Is adult: ', is_adult)
print("================================================================")

# Toán tử so sánh
x=10
y=5
print(x==y) # False - x không bằng y
print(x!=y) # True - x khác y
print(x>y) # True - x lớn hơn y
print(x<y) # False - x nhỏ hơn y
print(x>=y) # True - x lớn hơn hoặc bằng y
print(x<=y) # False - x nhỏ hơn hoặc bằng y
print("================================================================")

# Toán tử logic: AND, OR, NOT
a=True
b=False
# Toán tử AND
result1=a and b # False - a và b đồng thời phải là True thì mới trả về True
result2=a and a # True - a và a đều là True nên trả về True
# Toán tử OR
result3=a or b # True - chỉ cần a hoặc b là True thì sẽ trả về True
result4=b or b # Flase - cả a và b đều là False thì trả về False
# Toán tử NOT
result5=not a # False - Kết quả là phủ định của a (a là True thì phủ định là False)
result6=not b # True - Kết quả là phủ định của b (b là False thì phủ định là True)
print("Toán tử AND", result1, result2)
print("================================================================")
print("Toán tử  OR", result3, result4)
print("================================================================")
print("Toán tử NOT", result5, result6)
print("================================================================")