
number = int(input("Введите число n: "))

arr = []
count = 0

for a in range(number):
    s = round((1 + 1/(a + 1))**(a+1), 2)
    if s % 2 == 0:
        s = int(s)
    count += s
    arr.append(f"{a + 1}: {s}")
count = round(count, 2)
print(f'Для n = {number}: {arr}\nСумма {count}')