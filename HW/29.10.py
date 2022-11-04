# Task 1 - Age task
year = int(input('Введите год: '))
print("Ваш возраст:", 2021 - year, "лет")

# Task 2 - Perimeter
lines = int(input("Кол-во линий: "))
line_length = int(input("Длина линии: "))
print("Периметр=", lines * line_length)

# Task 3 - Litres
water = 20
print("Бегун пробегает", water * 0.5, "кругов.")

# Task 4 - Litres (Mod)
water_amount = int(input("Кол-во воды: "))
# float позволяет вводить числа в формате 2.5, 3.5 и тд.
water_per_circle = float(input("Сколько воды выпивает бегун за круг: "))
# round(a, b) округляет до определенного кол-ва знаков после запятой
# а - какое число округляется, b - до скольки знаков после запятой нужно округлить
print("Бегун пробегает", round(water_amount * water_per_circle, 2), "кругов.")