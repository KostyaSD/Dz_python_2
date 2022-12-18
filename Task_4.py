
number = int(input("Введите число n: "))

arr = []
path = 'file.txt'
count = 1

data = open(path, 'r')

for a in range(-number, number + 1):
    arr.append(a)
print("позиции элементов: ")

for line in data:
    line = int(line)
    count *= arr[line]
    print(f'{line} = {arr[line]}')
data.close()

print(f'промежуток {arr}\n'
      f'произведение элементов: {count}')




