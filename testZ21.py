""""Товары в корзине"
Пользователь добавляет товары в корзину. Программа хранит словарь: {'товар': количество}.
Функции:
Добавить товар (если уже есть — увеличить количество)
Удалить товар (уменьшить количество или удалить полностью)
Показать корзину
Выход"""
basket = {}
while True:
    select = int(input("1. Добавить товар\n" \
                "2. Удалить товар\n" \
                "3. Показать корзину\n" \
                "4. Выход\n"))

    def selectOne(strList):
        name = strList[0]
        count = int(strList[1])

        if name in basket:
            basket[name] += count
        else:
            basket[name] = count
        return basket

    def selectTwo(strList, option):
        name = strList[0]
        if option == 1:
            count = int(strList[1])

            if name in basket:
                basket[name] -= count
                print(basket)
            else:
                return 'Нет такого товара!'
        elif option == 2:
            for i, j in basket.items():
                if i in basket:
                    countP = j
            if name in basket:
                basket[name] -= countP
                print(basket) 
    match select:
        case 1:
            inpStr = str(input("Введите название товара и количетво: "))
            splitStr = inpStr.split(':')
            print(selectOne(splitStr))
        case 2:
            print(basket)
            option = int(input("Удалять отлько определенный или все: 1)Да 2)Нет "))
            inpStr = str(input("Введите название товара и количетво "))
            splitStr = inpStr.split(':')
            print(selectTwo(splitStr,option))
        case 3:
            if len(basket) == 0:
                print("Корзина пуста!")
            else:
                for i, j in basket.items():
                    print(f"{i}:{j}")
        case 4:
            break


