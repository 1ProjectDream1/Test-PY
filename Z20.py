#Проверка на простоту. Напиши функцию is_prime(n), которая возвращает True, 
# если число простое, и False, если составное. Используй ее в программе, 
# которая запрашивает число у пользователя и выводит результат.

def is_Prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False  
    elif n % 3 == 0:
        return False
    else:
        for i in range(n):
            if n % 1 == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True

number = int(input("Введите число: "))
print(is_Prime(number))