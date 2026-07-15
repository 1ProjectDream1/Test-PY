#Новая задача: "Генератор паролей" (уровень: средний)
#Это первая задача из этого блока, в ней нужно будет применить почти всё, 
#что мы уже изучили. Она хорошо развивает умение строить логику из простых элементов.
#Условие:
#Напишите программу, которая генерирует случайный пароль заданной длины из цифр 
#и букв латинского алфавита (как строчных, так и заглавных).

import random as rd

def ranPass():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lenChars = len(chars)
    resultList = []
    result = ''
    number = int(input('Длинна пароля: '))
    for i in range(0, number):
        rnd = rd.randint(0,lenChars - 1)
        resultList.append(chars[rnd])
    print(resultList)

    for i in range(0, len(resultList)):
        result = str(result) + str(resultList[i])
    print(result)
    return result

password = ranPass()

def validPass(passw):
    lenPass = len(passw)
    if lenPass < 8:
        return 'Не надежный пароль'
    
    tmp = None
    flagUpper = False
    flagLower = False
    flagDigit = False
    count = 0
    for i in range(0, lenPass):
        tmp = passw[i]
        if tmp.isupper(): 
            flagUpper = True
        elif tmp.islower():
            flagLower = True
        elif tmp.isdigit():
            flagDigit = True
    if flagUpper and flagLower and flagDigit:
        return 'Надежный пароль'
    else:
        return 'Не надежный пароль'
        
print(validPass(password))