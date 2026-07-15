#Телефонная книга
#Создайте простую программу для хранения контактов. Используйте словарь:
#  ключ — имя, значение — номер телефона.
#Реализуйте текстовое меню: 
# (1) Показать все контакты, 
# (2) Добавить контакт, 
# (3) Найти контакт по имени, 
# (4) Удалить контакт, 
# (5) Выход.

discription = {'Name1': '2323424', 'Name2':'1111111', 'Name3':'33333333333'}


def showContact():
    print(discription)

def addContact(name, phone):
    discription[name] = phone
    print(discription)

def seachContact(name):
    for i in discription:
        if i == name:
            print("Контакт: " + " " + discription[name])

def deleteContact(name):
    del discription[name]
    print(discription)

def main():
    print("(1) Показать все контакты" + "\n" 
            "(2) Добавить контакт" + "\n"
            "(3) Найти контакт по имени" + "\n" 
            "(4) Удалить контакт" + "\n"
            "(5) Выход." + "\n")
    select = int(input("Выберите вариант: "))
    try:
        match select:
            case 1:
                showContact()
            case 2:
                addContact('Name4','5555')
            case 3:
                seachContact('Name1')
            case 4:
                deleteContact("Name4")
            case 5:
                exit
    except:
        print("Нету в списке!")
    

main()