#"Словарь частотности слов"
#Пользователь вводит текст. Программа считает, сколько раз встречается каждое слово (без учёта регистра).
#cat dog elephant bird rabbit

inpStr = str(input("Ввод: ")).lower()

word = inpStr.split()
resultList = {}

for i in word:
    if i in resultList:
        resultList[i] += 1
    else:
        resultList[i] = 1

for i, j in resultList.items():
    print(f'{i}: {j}')