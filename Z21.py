#Калькулятор в функции. Напиши функцию calculate(a, b, operation), которая принимает два числа 
# и строку с названием операции ("add", "sub", "mul", "div") и возвращает результат. 
# Вызови ее в цикле для разных пар чисел.

def calculate(a, b, operation):
    result = 0
    if operation == 'add':
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        result = a / b
    return result

numbA = float(input("Введите a: "))
numbB = float(input("Введите b: "))
oper = input("Введите операцию(add, sub, mul, div): ")

print(calculate(numbA, numbB, oper))
