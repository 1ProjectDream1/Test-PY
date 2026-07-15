#Площадь круга. Напиши функцию circle_area(radius), которая возвращает площадь круга (π * r**2).
#Число π можно взять из модуля math (import math → math.pi).

import math

def circle_area(radius):
    P = math.pi * radius ** 2
    return P

result = circle_area(5)
print(result)


