# Task 1 - Delete elements
def delete_values(word, delete_elements):
    word = word.lower()
    delete_elements = delete_elements.lower()
    delete_element_count = 0
    for element in delete_elements:
        delete_element_count += word.count(element)
        word = word.replace(element, '')
    return word, delete_element_count

result = delete_values("собака", "оа")
print(result)

# Task 2 - Delete elements (MOD)
def delete_values(word, delete_elements):
    word = word.lower()
    delete_elements = delete_elements.lower()
    delete_element_count = 0
    element_frequency = 0
    for element in delete_elements:
        if element_frequency < word.count(element):
            element_frequency = element_frequency
            freq_elem = element
        delete_element_count += word.count(element)
        word = word.replace(element, '')
    return word, delete_element_count, f'Most frequent element: {freq_elem}'

result = delete_values("собака", "оа")
print(result)

# Task 3 - Delete elements (MOD + Dict)
def delete_values(word, delete_elements):
    word = word.lower()
    delete_elements = delete_elements.lower()
    delete_element_count = 0
    element_frequency = 0
    letters_dictionary = {}
    for element in delete_elements:
        counter = word.count(element)
        if element_frequency < counter:
            element_frequency = counter
            freq_elem = element
        delete_element_count += counter
        letters_dictionary[element] = counter
        word = word.replace(element, '')
    print('Deleted elements: ')
    print(letters_dictionary)
    return word, delete_element_count, f'Most frequent element: {freq_elem}'

result = delete_values("собака", "оа")
print(result)