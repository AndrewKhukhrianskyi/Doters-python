'''
Config - это файл, который хранит параметры для работы приложения
(например, название приложения, размер экрана и тп)

Rules:
- Все переменные начинаются С больших букв (Примеp: TITLE)
'''

# Параметры приложения
TITLE = 'Анализатор текста V.1.0.0'

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700

WINDOW_STATUS_RESIZABLE = False, False

BUTTON_HEIGHT = 2
BUTTON_WIDTH = 7

TEXT_WIDTH = 50
TEXT_HEIGHT = 15

REGEX_WIDTH = 40
REGEX_HEIGHT = 1

LABEL_WIDTH = 40

# Работа с текстом
ANALYZE_TEXT_LIST = ["Кол-во гласных букв:",
                     "Кол-во согласных букв:",
                     "Кол-во символов:",
                     "Часто встречаемая буква:",
                     "Редко встречаемая буква:",
                     "Не встречаемая буква:",
                     "Кол-во чисел:",
                     "Среднее арифметическое по кол-ву текста:"]

LANGUAGE_RU ='абвгдеёжзийклмнопрстюфхцчшщьъэюя'
LANGUAGE_UA = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
LANGUAGE_EN = 'abcdefghijklmnopqrstuvwxyz'
