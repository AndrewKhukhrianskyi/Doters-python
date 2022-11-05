string = 'Python'

print(string[3])
print(string[0])
print(string[-5])

text = 'Питон - это мой лучший друг!'
# find позволяет искать слова\буквы
save = text.find("друг")
end = text.find('!')
print(save)
# Выполняем срез (save - откуда, end - до куда)
print(text[save:end]) 

# task 1
# Из букв слова составить слово "дикобраз"
text = "Вечера на хуторе близ диканьки"
save = text.find("диканьки")
save2 = text.find('о')
save3 = text.find('б')
save4 = text.find('ра')
save5 = text.find('з')
print("TASK 1")
print(text[save:save+3] + text[save2] + text[save3] + text[save4:save4 + 2] + text[save5])

# task 2
text = 'hl;dshdf;slshjdtrl;hkjdlbkjgsehrtoesufoiesurerpwtoirgkkdfg; y;rtyerk;frelg'
print("TASK 2")
print(text[-1])

# Task 3
text = "Молот"
print("TASK 3")
print(text[::-1])
