# 1. Cấu trúc điều khiển IF-ELSE

num=10
# if điều_kiện:
if num>=10:
    # Mã thực thi nếu điều_kiện là True
    print("positive numbers")
else:
    # Mã thực thi nếu điều_kiện là False
    print("negative numbers")

# 2. Cấu trúc điều khiển SWITCH-CASE
# Python không hỗ trợ cấu trúc điều khiển switch-case
# Tuy nhiên, bạn có thể sử dụng một từ điển (dictionary) để thực hiện công việc tương tự.

def switch_case(argument):
    switcher ={
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
    }
    return switcher.get(argument, "Not determined")
num_cases = 3
print(switch_case(num_cases)) #Results: three

# 3. Cấu trúc điều khiển FOR-IN
fruits=["apple", "orange", "banana"]

# for <biến> in <dãy>:
for fruit in fruits:
    # Các lệnh muốn thực hiện trong vòng lập
    print("Fruit", fruit)

# 4. Cấu trúc điều khiển WHILE
count=1

# while điều_kiện:
while count<=5:
    # Mã thực thi trong điều_kiện là True
    print("Number of iterations", count)
    count+=1
