#Палиндром. Запроси у пользователя слово. Преобразуй его в список символов. 
# Проверь, читается ли оно одинаково слева направо и справа налево (например, "шалаш", "топот").

string = str(input("Введите слово: "))
stringTmp = ""

for i in range(len(string)-1, -1, -1):
    stringTmp = stringTmp + string[i]
if string == stringTmp:
    print("Палиндром")
else:
    print("Не палиндром")

tmpSTR = ""

for i in reversed(string):
    tmpSTR = tmpSTR + i
if string == tmpSTR:
    print("Палиндром")
else:
    print("Не палиндром")