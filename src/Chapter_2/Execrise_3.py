# Xây dựng chương trình nhập vào một số nguyên dương N sau đó tính tổng N số nguyên dương đầu tiên. 
n=int(input('Nhập số nguyên N: '))
S=0
for i in range(1,n+1,1):
    S+=i
print('Total: ', S)