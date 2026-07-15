#Создай калькулятор, который:
#Запрашивает два числа и операцию (+, -, *, /)
#Сохраняет каждую операцию в список
#Показывает историю последних 5 операций
#Работает в цикле до команды "выход"
l = []

def calulator(a,b,operation):
    result = 0
    if operation == "+":
        result = a + b
        l.append(f"{a} {operation} {b} ""="f" {result}")
    elif operation == "-":
        result = a - b
        l.append(f"{a} {operation} {b} ""="f" {result}")
    elif operation == "*":
        result = a * b
        l.append(f"{a} {operation} {b} ""="f" {result}")
    elif operation == "/":
        result = a / b
        l.append(f"{a} {operation} {b} ""="f" {result}")


def main():
    while True:
        a = float(input("Введите первое число: "))
        b = float(input("Втрое число: "))
        operation = input("Выберите операцию: ")
        calulator(a,b,operation)
        print("История: " + "\n")
        for i in range(len(l)):
            print(l[i])

main()