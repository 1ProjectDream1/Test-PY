#"Объединение словарей"
#Даны два словаря. Нужно создать новый словарь, который объединяет оба.
#Правила
#Если ключ есть только в одном словаре — берём его значение
#Если ключ есть в обоих — суммируем значения

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 1, 'd': 5}

buffer_dict1 = dict1.copy()
print(buffer_dict1)

for i, j in dict2.items():
    if i in buffer_dict1:
        buffer_dict1[i] += j
    else:
        buffer_dict1[i] = j

print(buffer_dict1)