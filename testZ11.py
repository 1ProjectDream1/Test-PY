#"Анализ текста 2.0"
#Пользователь вводит текст. Программа выводит:



strInput = str(input('Строка: '))

listWord = strInput.split()
print(listWord)
countWord = 0
chars = ''
#Самое длинное слово
for i in listWord:
    if i != ' ':
        count = 1 
        for j in i:
            count += 1
        if count > countWord:
            countWord = count
            chars = i
    count = 0
print(str(countWord) + ' ' + str(chars))

#Самую редкую букву (которая встречается 1 раз)
listChars = {}
countChars = 1

for i in strInput:
    if i.isalpha():
        if i in listChars:
            listChars[i] += 1
        else:
            listChars[i] = 1
print(listChars)

chars = ''
min_chars = float('inf')
for i, j in listChars.items():
    if j < min_chars:
        min_chars = j
        chars = i
print(str(min_chars) + ' ' + str(chars))
