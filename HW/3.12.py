# Task 1 - Even numbers 
arr = [1,5,6,2,3,4,5,0,0,9,10,11,3,25,37,44,1101,110]
even_arr = []

for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)

print(even_arr)

# Task 2 - String worker
list_sentence = input('Enter sentence: ').lower().split()
result = []

for word in list_sentence:
    if word.isalpha():
        result.append(word)
print(result)