#Напиши функцию fibonacci(n), которая возвращает список из n чисел Фибоначчи. 
#Затем выведи только четные числа из этого списка.
#Пример: fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibonacci(n): 
    fib1 = 0
    fib2 = 1
    result = 0
    listt = []
    listt.append(0)
    listt.append(1)
    for i in range(n-2):
        result = fib1 + fib2
        fib1 = fib2
        fib2 = result
        listt.append(fib2)
    print(listt)
    for i in range(len(listt)):
        if listt[i] % 2 == 0:
            print(listt[i])

fibonacci(10)