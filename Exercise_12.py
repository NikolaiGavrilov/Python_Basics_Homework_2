# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random

petya_x = random.randint(0, 1001)
petya_y = random.randint(0, 1001)
print(f"Petya: The summ of my numbers is {petya_x + petya_y}")
print(f"Petya: If we multiply them we will have {petya_x * petya_y}")
print(f"Petya: Can you guess the numbers?")

katya_number1 = 0
katya_number2 = 0
for katya_number1 in range(0,1001):
    for katya_number2 in range(0,1001):
        if katya_number1*katya_number2 == petya_x*petya_y and katya_number1+katya_number2 == petya_x+petya_y:
            katyas_answer = (f"Katya: Yes, your numbers are {katya_number1} and {katya_number2}")

print(katyas_answer)
