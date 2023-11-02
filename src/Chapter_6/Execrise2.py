"""
    * 1. List comprehension
"""

squares = [value ** 2 for value in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

result = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(result)  # ['even', 'odd', 'even', 'odd', 'even']
print("================================================")

"""
    * 2. Hai phương thức map, filter trong PythonPermalink
    * 2.1. mapPermalink
    ** map trong python có dạng map(function, iterable) và áp dụng mỗi function cho từng mỗi item trong iterable.
    ** Sử dụng map và lambda
    * 2.2. filter
    ** filter trong python có dạng filter(function or None, iterable) và filter cho mỗi item trong iterable dựa trên các kết quả trả về của function.
    ** Sử dụng filter và lambda
"""

def double(number):
    return number + number

numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(result) # result không phải 1 list
print(list(result))  # [2, 4, 6, 8]
print("================================================")

numbers = [2, 4, 1, 2]
result = map(lambda i: i + i, numbers)
print(list(result))  # [4, 8, 2, 4]
print("================================================")

def checkEven(number):
    return number % 2 == 0

numbers = [0, 1, 2, 4, 7, 9, 12]
evenNumbers = filter(checkEven, numbers)
print(list(evenNumbers))  # [0, 2, 4, 12]
print("================================================")

numbers = [0, 1, 2, 4, 7, 9, 12]

result = filter(lambda i: i % 2 != 0, numbers)
print(list(result))  # [1, 7, 9]

"""
    * 3. dict comprehension, set comprehension
    * 3.1. dict comprehension
    ** dict comprehension là cách viết ngắn gọn để tạo một từ điển (dictionary) trong Python.
    ** Khi sử dụng dict comprehension cho đoạn code trên thì
    ** Sử dụng dict comprehension với điều kiện if
    ** Sử dụng dict comprehension với nhiều điều kiện if
    ** Sử dụng dict comprehension với điều kiện if-else
    * 3.2. set comprehension
    ** set comprehension để tạo một set mới dựa trên một cái đang tồn tại
    ** Sử dụng set comprehension cho đoạn code trên
    ** Sử dụng set comprehension với điều kiện if
"""

squareDict = dict()
for i in range(5):
    squareDict[i] = i * i

print(squareDict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print("================================================")

squareDict = {i: i * i for i in range(5)}
print(squareDict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print("================================================")

personInformation = {'Jack': 28, 'Allex': 41, 'Geomo': 50, 'John': 37}

evenAgeDict = {name: age for (name, age) in personInformation.items()
               if age % 2 == 0}
print(evenAgeDict)  # {'Jack': 28, 'Geomo': 50}
print("================================================")

personInformation = {'Jack': 28, 'Allex': 41, 'Geomo': 50, 'John': 37}

evenDict = {name: age for (name, age) in personInformation.items()
            if age % 2 != 0 if age < 40}
print(evenDict)  # {'John': 37}
print("================================================")

personInformationDict = {'Jack': 28, 'Allex': 41, 'Geomo': 50, 'John': 37}

newDict = {name: ('old' if age > 40 else 'young')
          for (name, age) in personInformationDict.items()}
print(newDict)
# {'Jack': 'young', 'Allex': 'old', 'Geomo': 'old', 'John': 'young'}
print("================================================")

names = ['John', 'Anna', 'Jack']
lowerCaseNames = set()
for name in names:
    lowerCaseNames.add(name.lower())

print(lowerCaseNames)  # {'anna', 'john', 'jack'}
print("================================================")

names = ['John', 'Anna', 'Jack']
lowerCaseNames = {name.lower() for name in names}
print(lowerCaseNames)  # {'anna', 'jack', 'john'}
print("================================================")

names = ['John', 'Anna', 'Jack']
lowerCaseNames = {name.lower() for name in names if name != 'Jack'}
print(lowerCaseNames)  # {'john', 'anna'}
