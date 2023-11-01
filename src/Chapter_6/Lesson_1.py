"""
* List Comprehension
* List Comprehension trong Python là một cú pháp cho phép bạn tạo một danh sách mới bằng cách thực hiện một biểu thức trên mỗi phần tử của danh sách cũ hoặc từ một dãy giá trị.
* Đây là một cách ngắn gọn và hiệu quả để thực hiện các phép biến đổi trên danh sách mà không sử dụng vòng lặp truyền thống.
"""
# * Vi du
""" 
    * Dựa trên danh sách fruits, ta muốn có một danh sách mới, chỉ chứa các loại trái cây có chữ cái là a trong tên.
    * Nếu không sử dụng list comprehension bạn sẽ phải viết một câu lệnh for với điều kiện bên trong:
"""
# fruits = ["apple", "orange", "cherry", "kiwi", "mango"]
# newList = []

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)

""" 
    * Với list comprehension ta có thể làm tất cả những điều đó chỉ với một đoạn code
"""
# fruits = ["apple", "orange", "cherry", "kiwi", "mango"]
# newList = [x for x in fruits if "a" in x]

# print(newList)

""" 
    * Cú pháp
    * Giá trị trả về là một danh sách mới, giữ nguyên danh sách cũ
"""
# newList = [expression for item in iterable if condition == True]

"""
* Condition:
** condition là điều kiện mà phần tử phải thỏa mãn để được đưa vào danh sách mới..
** Ví dụ: chỉ chấp nhận các items không phải là apple.
** Với điều kiện x != “apple” sẽ trả về True cho tất cả các phần tử không phải là “apple”, làm cho danh sách mới chứa tất cả fruits mới chứa tất cả các loại fruit ngoại trừ apple
** condition là tùy chọn và có thể bỏ qua
"""

# newList = [x for x in fruits if x != "apple"]

# newList = [x for x in fruits]

"""
* Interable:
** iterable có thể là bất kỳ đối tượng iterable nào, như list, tuple, set,...
** Ví dụ ta có thể sử dụng hàm range() để tạo một lần lặp.
** Ta có một ví dụ tương tự, nhưng có thêm một condition
"""

# newList = [x for x in range(10)]
# newList = [x for x in range(10) if x < 5]

"""
* Expression:
** expression là phần tử hiện tại trong quá trình lặp, nhưng nó cũng là kết quả cuối cùng, mà ta có thể thay đổi trước khi nó trở thành một phần tử danh sách trong danh sách mới.
** Ví dụ: Đặt các giá trị trong danh sách mới thành chữ hoa.
** Ta có thể đặt kết quả thành bất cứ thứ gì:
** Ví dụ: đặt các giá trị trong danh sách mới thành “hello”
** expression là biểu thức được áp dụng lên mỗi phần tử của danh sách cũ để tạo phần tử tương ứng trong danh sách mới
** Ví dụ: Trả về orange thay vì banana. Trả về phần tử nếu nó không phải là banana, nếu là banana thì trả về orange.

"""
# newList = [x.upper() for x in fruits]

# newList = ['hello' for x in fruits]

# newList = [x if x != "banana" else 'orange' for x in fruits]