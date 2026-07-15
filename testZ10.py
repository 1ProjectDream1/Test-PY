#"Анализ текста"
#Пользователь вводит текст. Программа выводит:


#Самую частую букву

strIN = str(input('Введите текст: '))
countS = 0
#Количество символов (без пробелов)
for i in strIN:
    if i not in ' ':
        countS = countS + 1
print(countS)

#Количество слов
tmpW = strIN.split()
print(len(tmpW))

#Количество уникальных букв
uniqleList = []

for i in strIN:
    for j in i:
        if j not in uniqleList:
            if j != ' ':
                uniqleList.append(j)
print(len(uniqleList))



