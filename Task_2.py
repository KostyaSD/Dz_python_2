
number = int(input("Введите число N: "))
arr = []
i = 1
for a in range(number):
    i *= a + 1
    arr.append(i)
print(arr)
