"""
    * Tạo một danh sách chứa bình phương của các số từ 1 đến 10.
"""
squares = [x**2 for x in range(1, 11)]
print(squares)
print("================================================")
"""
    * Tạo một danh sách chứa các số nguyên tố từ 1 đến 50
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in range(1, 51):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)
print("================================================")

"""
    * Cho một danh sách các số, tạo một danh sách mới chứa các số âm.
"""
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
negative_numbers = []

for num in numbers:
    if num < 0:
        negative_numbers.append(num)

print(negative_numbers)
print("================================================")

"""
    * Tạo một danh sách chứa các số chẵn từ 0 đến 20.
"""
even_numbers = []

for num in range(0, 21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
print("================================================")

"""
    * Cho một danh sách các số, tạo một danh sách mới chứa các số lớn hơn 5 và chia hết cho 3
"""
numbers = [2, 4, 6, 8, 9, 12, 15, 18, 20, 21]
new_numbers = []

for num in numbers:
    if num > 5 and num % 3 == 0:
        new_numbers.append(num)

print(new_numbers)


