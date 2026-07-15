#Сумма чисел. Запрашивай у пользователя числа до тех пор, пока он не введет 0. 
# Как только будет введен 0, выведи сумму всех введенных чисел.

summ = 0 

while True:
    number = int(input("Введите число: "))

    if number != 0:
        summ = summ + number
    else: 
        print(str(summ) + " Выход!")
        break