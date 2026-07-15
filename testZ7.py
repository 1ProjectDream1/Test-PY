#8. «Поиск максимального»
#Пользователь вводит числа, пока не введёт 0. Программа выводит максимальное из введённых (не считая 0).
list = []
tmp = 0
while True:
    number = int(input('Введите число: '))

    if number != 0:
        list.append(number)
    else:
        for i in range(len(list)):
            if tmp < list[i]:
                tmp = list[i]
        print(tmp)
        break