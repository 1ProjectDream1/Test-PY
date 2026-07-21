#"Обратный словарь"
#Пользователь вводит текст. Программа создаёт словарь, где ключ — буква, 
#начение — список слов, которые начинаются с этой буквы. cat dog elephant bird rabbit

inpStr = str(input('Ввод: '))

listStr = inpStr.split()
print(listStr)
resultList = {}

for i in listStr:
    letter = i[0]
    if letter in resultList:
        resultList[letter].append(i)
    else:
        resultList[letter] = [i]
print(resultList)