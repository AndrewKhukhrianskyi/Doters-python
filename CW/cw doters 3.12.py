# .append()
arr = [1, 2, 4, 8, 9]
arr.append(20)

print(arr)
from random import randint

arr = [randint(1, 1000) for elem in range(randint(5, 100))]
print(arr)
arr2 = []
for num in arr:
    if num % 2 == 1:
        arr2.append(num)
print(arr2)
print(sum(arr2))

