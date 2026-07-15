# Дан список:
numbers = [10, 25, 32, 47, 58, 63, 71, 84, 99]

# Выведи:
# 1. Первые 3 элемента (используй срез)
# 2. Последние 3 элемента (используй отрицательные индексы)
# 3. Все элементы, кроме первого и последнего
# 4. Каждый третий элемент
# 5. Список в обратном порядке, но не весь, а элементы с индексами 2, 3, 4 в обратном порядке

#1
print(str(numbers[:3:]) + "\n")
#2
tmp = 0
for i in reversed(numbers):
    tmp += 1
    if tmp <= 3:
        print(i)

print("\n")
#3
for i in range(len(numbers) - 1):
    if i != 0 and i != len(numbers):
        print(numbers[i])
print("\n")

#4 
for i in range(len(numbers) - 1):
    if i % 3 == 0:
        print(numbers[i])
print("\n")

#5. Список в обратном порядке, но не весь, а элементы с индексами 2, 3, 4 в обратном порядке
for i in range(len(numbers) -1, -1, -1):
    if i == 2 or i == 3 or i == 4:
        print(numbers[i])

