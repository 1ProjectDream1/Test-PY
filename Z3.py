#Анализ текста (Частотный словарь)
#Напишите функцию, которая принимает строку текста и возвращает словарь, где ключ — слово (в нижнем регистре),
# а значение — сколько раз оно встречается.
#Усложнение: Уберите знаки препинания (запятые, точки) перед подсчетом.

text =  "Любовь как любовь, жизнь как жизнь"
text = text.replace(",", "")
text = text.lower()
text = text.split()

discription = {}

def textDescr(textD):
    for i in textD:
        if i in discription:
            discription[i] = discription[i] + 1 
        else:
            discription[i] = 1 
    print(discription)
    

textDescr(text) 