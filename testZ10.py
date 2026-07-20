#"Анализ текста"
#Пользователь вводит текст. Программа выводит:

strIN = str(input('Введите текст: '))
countS = 0
count = 0
#Количество символов (без пробелов)
for i in strIN:
    if i not in ' ':
        countS = countS + 1
print("Количество символов: " + str(countS))

#Количество слов
tmpW = strIN.split()
print("Количество слов: " + str(len(tmpW)))

#Тоже считает количество слов, но есть проблема с последним пробелом,
#Если пользователь поставит пробел в конце, то защитает за слово
tmpStr = ''
countStr = 1
for i in strIN:
    if i == " ":
       countStr = countStr + 1 
print(countStr)

#Количество уникальных букв
uniqleList = []

for i in strIN:
    for j in i:
        if j not in uniqleList:
            if j != ' ':
                uniqleList.append(j)
print("Количество уникальных букв: " + str(len(uniqleList)))

#Самую частую букву
listStr = []
for i in strIN:
    if i not in listStr:
        listStr.append(i)

max_count = 0
max_chars = ''

for i in listStr:
    count = strIN.count(i)
    if count > max_count:
        max_chars = i
        max_count = count
print(max_chars, max_count)