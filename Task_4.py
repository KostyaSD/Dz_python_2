
number = int(input("Введите число n: "))

arr = []
num = -number
for a in range(number * 2 + 1):
    arr.append(num + a)
print(arr)