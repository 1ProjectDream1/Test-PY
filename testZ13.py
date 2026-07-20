#"Подсчёт букв"
#Пользователь вводит текст. Программа считает, сколько раз встречается каждая буква (без учёта регистра).
#Условие:
#Приводим все буквы к нижнему регистру (.lower())
#Игнорируем пробелы и знаки препинания
#Выводим результат в алфавитном порядке

inpStr = str(input("Введите: "))
inpStr = inpStr.lower()

listChar = {}
for i in inpStr:
    if i.isalpha():
        if i in listChar:
            listChar[i] += 1
        else:
            listChar[i] = 1

for i, j in sorted(listChar.items()):
    print(i, j)
