#"Подсчёт голосов"
#Пользователь вводит имена кандидатов и количество голосов за них (в формате: "Имя: голоса"). 
#Программа суммирует голоса для каждого кандидата.
const_strig = '\':\''
count_golos = {}

while True:
    inpStr = str(input('Имя: '))
    if len(inpStr) == 0:
        break

    if ':' not in inpStr:
        print(f"Формат строки через {const_strig}")
        break

    splitStr = inpStr.split(':')
    name = splitStr[0]
    count = int(splitStr[1])

    if name in count_golos:
        count_golos[name] += count
    else:
        count_golos[name] = count
    
for i, j in count_golos.items():
    print(f'{i}: {j}')

