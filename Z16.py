#Четные по порядку. Дан список чисел. Создай новый список, в который войдут только числа, 
#стоящие на четных индексах (0, 2, 4...). Выведи оба списка.
import random

listF = []
tmp = 0

while True:
    rand = random.randrange(0, 100)
    listF.append(rand)
    tmp += 1
    if tmp == 10:
        break

listS = []

for i in range(len(listF) -1):
    if i % 2 == 0:
        tmp = listF[i]
        listS.append(tmp)

print(listF)
print(listS)