# Tuple - списки, которые нельзя менять
numbers = (1,2)


# Dictionaries - структурированный список
d = {'key' : 'value'}
# Обращение к выражению справа идет ТОЛЬКО по ключу
print(d['key'])
# Обращение к несуществущему ключу = ошибка
# print(d['key1'])
# Для того, чтобы добавить новое выражение словарь
"""
нужно написать следующее выражение
словарь[ключ] = значение
"""
d['key1'] = 'value1'
print(d)
key_data = ["Имя", "Фамилия", "Возраст"]
value_data = ["Иван", "Иванов", 25]
d = {}
d[key_data[0]] = value_data[0]
d[key_data[1]] = value_data[1]
d[key_data[2]] = value_data[2]
print(d)
# .keys(), .values(), .items()
# .keys - достаем ключи
# .values - достаем значение
# .items - достаем ключ и значение. РАБОТЕТ ТОЛЬКО В ЦИКЛЕ
print(list(d.keys()))
print(list(d.values()))

# Словарь хранит ключи без повторений
data = {}
ask = ''
while ask != 'exit':
  ask = input('Введите выражение слева: ')
  ask2 = input("Выражение справа: ")
  data[ask] = ask2
  print(data)

data = {'Тип фигуры': "Треугольник",
        "Периметр" : "10 см"}
# for ключ, значение in словарь.items():
for key, value in data.items():
    print(key)
    print(value)
