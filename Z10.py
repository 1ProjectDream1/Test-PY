#Угадай число. Напиши игру "Угадай число". Программа "загадывает" число 
# с помощью import random и random.randint(1, 100). Пользователь вводит варианты, 
# а программа подсказывает "больше" или "меньше". Цикл продолжается, пока число не будет угадано.

import random

rand = random.randint(1,100)

while True:
    number = int(input("Введите число: "))

    if rand > number:
        print("Больше")
    elif rand < number:
        print("Меньше")
    else:
        print("Ура")
        break

