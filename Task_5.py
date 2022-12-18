import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# random.shuffle(a) #  1 вариант

for i in range(len(a) - 1, 0, -1): #  2 вариант
    j = random.randint(0, i + 1)
    a[i], a[j] = a[j], a[i]

print(a)

