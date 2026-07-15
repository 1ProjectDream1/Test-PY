#Дан список чисел: [3, 8, 12, 5, 9]. 
# Найди, есть ли в нём число 10. Выведи "Нашёл!" или "Нет".

list = [3, 8, 12, 5, 9]

flag = False

for i in range(len(list)):
    if list[i] == 10:
        flag = True
        break

if flag:
    print('Нашёл!')
else:
    print('Нет')

