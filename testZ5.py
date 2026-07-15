#6. «Мини-калькулятор»
#Пользователь вводит два числа и оператор (+, -, *, /).
#Программа вычисляет результат. Если оператор неизвестен — вывести ошибку.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
operation = input('Введите оператор: ')
result = 0

if operation not in ['+', '-', '*', '/']:
    print('Выберите правильный оператор')
else:
    match operation:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            result = a / b
    print('Резулта: '+ str(result))

