
number = float(input("Введите вещественное число: "))

dig = []
i = 0
while i < len(str(number)):
    if str(number)[i] != '.':
        dig.append(int(str(number)[i]))
    i += 1
print(f"сумма чисел числа {number} = {sum(dig)}")
