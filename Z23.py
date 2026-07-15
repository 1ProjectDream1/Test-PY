#Задание 21: Шифр Цезаря
#Напиши две функции:
#encrypt(text, shift) - шифрует текст, сдвигая каждую букву
#decrypt(text, shift) - расшифровывает

alf = ['a','b', 'c', 'd',
       'e', 'f', 'g', 'h',
       'i','j','k','l',
       'm','n','o','p',
       'q','r','s','t',
       'u','v','w','x',
       'y','z']


def encrypt(text, shift):
    tmp = ""
    new_intex = 0
    for i in range(len(text)):
        for j in range(len(alf)):
            if text[i] == alf[j]:
                new_intex = (j + shift) % len(alf)
                tmp += alf[new_intex]
    print(tmp)
    return tmp

def decrypt(text, shift):
    tmp = ""
    new_index = 0
    for i in range(len(text)):
        for j in range(len(alf)):
            if text[i] == alf[j]:
                new_index = (j - shift) % len(alf)
                tmp += alf[new_index]
    print(tmp)


tmp = encrypt('test', 8)
decrypt(tmp, 8)

#Взлом шифра Цезаря
#Напиши функцию crack_caesar(encrypted_text), которая пытается расшифровать текст, 
#перебирая все возможные сдвиги (1-25), и выводит все варианты. Пользователь должен выбрать правильный.

def crack_caesar(encrypted_text):
    rez_tmp = ''
    new_index = 0
    listt = []
    for l in range(1, 26):
        rez_tmp = ''
        for i in range(len(encrypted_text)):
            for j in range(len(alf)):
                if encrypted_text[i] == alf[j]:
                    new_index = (j - l) % len(alf)
                    rez_tmp += alf[new_index]
        listt.append(rez_tmp)
        print(listt)
        select = input("Выберите вариант: ")

        for i in range(len(listt)):
            if i == select:
                print("Правильный вариант: " + listt[i])
        
        

    
    



crack_caesar(tmp)
