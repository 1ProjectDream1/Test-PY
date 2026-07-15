#Поиск максимума. Запроси у пользователя 5 чисел (или введи готовый список [34, 7, 23, 98, 12]). 
# Найди в списке максимальное и минимальное значение, не используя встроенные функции max() и min() 
# (используй цикл и сравнение).

listt = []
tmp = 0

while True:
    number = int(input("Введите число: "))
    tmp += 1
    listt.append(number)
    if tmp == 5:
        break

minN = listt[0]
maxN = len(listt) - 1

for i in range(len(listt)):
    if listt[i] < minN:
        minN = listt[i]
print(f"Минимальное значение {minN}")
    
for i in range(len(listt)):
    if listt[i] > maxN:
        maxN = listt[i]
print(f"Максимальное значение: {maxN}")
