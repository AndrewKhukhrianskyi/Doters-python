# range() создает ряд чисел

print(range(5)) # 0...5
print(range(1, 10)) # 1..10
print(range(0, 6, 2)) 

# Task 1 - add 5
for num in range(1, 100):
    print(num + 5)

# Task 2 - append number in arr
arr = []
for number in range(50):
    arr.append(number)
print(arr)

# Task 3 - Find Median
from random import randint

# Заполняем список числами
arr2 = [randint(2, 100) for elem in range(randint(10, 100))]
arr2 = [1,2,3,4,5,6]
arr2.sort()
print('TASK 3')
print(arr2)
if len(arr2) % 2 == 1:
    median = len(arr2) // 2
    print(arr2[median])
else:
    index_1 = len(arr2) // 2
    print(index_1)
    index_2 = index_1 - 1
    print(index_2)
    median = arr[index_1] + arr[index_2]
    print(median / 2)
    
    
