#Задача 5. «Угадай число» (навык: цикл while + логика)
#Компьютер загадывает число от 1 до 20 (в коде напиши secret = 13). Ты угадываешь. 
#После каждой попытки подсказка: "Больше" или "Меньше". Считай количество попыток.

import random as rd

rand = rd.randint(1,20)
counter = 0

while True:
    number = int(input("Введите число: "))
    if rand > number:
        print("Больше")
        counter = counter + 1
    elif rand < number:
        print("Меньше")
        counter = counter + 1
    else: 
        print("Угадал" + " Количетво попыток: " + str(counter))
        break