#Даны два словаря (например, {'a': 1, 'b': 2, 'c': 3} и {'b': 2, 'c': 4, 'd': 5}).
#Нужно найти:
#Общие ключи (которые есть в обоих словарях)
#Ключи, которые есть только в первом
#Ключи, которые есть только во втором

firstList = {'a': 1, 'b': 2, 'c': 3}
secondList = {'b': 2, 'c': 4, 'd': 5}
generalList = []
FirstSecondList = {'First': [], 'Second':[]}

for i in firstList:
    for j in secondList:
        if i == j:
            generalList.append(i)

for i in firstList:
    if i not in secondList:
        FirstSecondList['First'].append(i)
for i in secondList:
    if i not in firstList:
        FirstSecondList['Second'].append(i)
print(f"Общие ключи {generalList}")

for i, j in FirstSecondList.items():
    print(f"{i}:{j}")