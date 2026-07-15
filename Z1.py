#Выведите числа от 1 до 100. Но если число делится на 3,
#вместо него выведите "Fizz", если на 5 — "Buzz", а если на 3 и 5 одновременно — "FizzBuzz".
import random

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)