#"Группировка по длине"
#Пользователь вводит несколько слов через пробел. Программа группирует слова по их длине.

inpStr = str(input("Ввод: "))

listWord = inpStr.split()
newList = {}
resultList = {}

print(listWord)

for i in listWord:
    if i in newList:
        newList[i].append(len(i))
    else:
        newList[i] = [len(i)]

print(newList)

for i, j in newList.items():
    for element in j:
        if element in resultList:
            resultList[element].append(i)
        else:
            resultList[element] = [i]
print(resultList)
