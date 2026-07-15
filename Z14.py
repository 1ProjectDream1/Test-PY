#Список покупок. Создай пустой список. В цикле запрашивай 
# у пользователя товары для добавления в список покупок. Если пользователь вводит "стоп", 
# цикл прекращается, и программа выводит итоговый список с нумерацией (используй enumerate).

listt = []
tmp = 0

while True:
    string = str(input("Введите продукт: "))

    if string != "стоп":
        listt.append(string)
    else: 
        for count, item in enumerate(listt):
            print(count, item)
        break

        