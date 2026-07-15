#Задача 4. «Ближайшее к 10» (навык: сравнение с эталоном)
#Дан список [4, 15, 9, 20, 11]. Найди число, которое ближе всего к 10 (по модулю разницы).
#Алгоритм:
#Берём первое число как «лучшее».
#Для каждого следующего считаем abs(число - 10).
#Если разница меньше — заменяем лучшее.

list = [4, 15, 9, 20, 11]
firstValue = list[0]
absValueF = abs(firstValue - 10)
absValue = 0
bestNumber = 0

for i in range(1, len(list)):
    currentNumber = list[i]
    absValue = abs(currentNumber - 10)
    if absValue < absValueF:
        bestNumber = currentNumber
        absValueF = absValue
print(bestNumber)
