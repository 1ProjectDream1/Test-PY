#"Шифр Цезаря"
#Пользователь вводит текст и число сдвига. Программа шифрует текст, 
#сдвигая каждую букву на указанное число.

inpStr = str(input("Введите тест: "))
inpInt = int(input("Введиде сдвиг: "))

def chiffon(st, number):
    result = ''

    for i in range(len(st)):
        tmpOrd = ord(st[i]) + number
        tmpChr = chr(tmpOrd)
        result = str(result) + tmpChr
    print(result)
    return result

resultC = chiffon(inpStr,inpInt)

def unchiffor(st, number):
    result = ''
    for i in range(len(st)):
        tmpOrd = ord(st[i]) - number
        tmpChr = chr(tmpOrd)
        result = str(result) + tmpChr
    return result

print(unchiffor(resultC, inpInt))

#Написал свой методы без ord и chr 
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!?.,'
def Mychiffon(st, number): 
    result = ''

    for i in range(len(st)):
        tmpUL = st[i]

        if st[i] == ' ':
            result = str(result) + ' '
        
        if tmpUL in symbol:
            result = str(result) + tmpUL

        if tmpUL.isupper():
            for j in range(len(upper)):
                if upper[j] == st[i]:
                    tmp = (j + number) % len(upper)
                    result = str(result) + upper[tmp]
        elif tmpUL.islower():
            for j in range(len(lower)):
                if lower[j] == tmpUL:
                    tmp = (j + number) % len(lower)
                    result = str(result) + lower[tmp]
    print(result)
    return result

strMy = Mychiffon(inpStr, inpInt)

def Myunchiffor(st, number):
    result = ''

    for i in range(len(st)):
        tmpUL = st[i]
        if st[i] == ' ':
            result = str(result) + ' '
        
        if tmpUL in symbol:
            result = str(result) + tmpUL

        if tmpUL.isupper():
            for j in range(len(upper)):
                if upper[j] == tmpUL:
                    tmp = (j - number) % len(upper)
                    result = str(result) + upper[tmp]
        elif tmpUL.islower():
            for j in range(len(lower)):
                if lower[j] == tmpUL:
                    tmp = (j - number) % len(lower)
                    result = str(result) + lower[tmp]
    print(result)
    return(result)

Myunchiffor(strMy, inpInt)
