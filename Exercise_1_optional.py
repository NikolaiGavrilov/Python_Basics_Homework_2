# задача 1 сложная необязательная 
# Посчитать сумму цифр любого целого или вещественного числа. 
# Через строку решать нельзя.

import math 

your_number = float(input("Input your number:"))

while math.ceil(your_number) - your_number != 0.0:
    your_number *= 10

your_number = int(your_number)
summ = 0

digits_list = []
count = 0
while int(your_number % 10) != 0:
    digits_list.append(int(your_number%10))
    your_number /= 10
    count +=1

for i in range(count):
    summ += digits_list[i]

print(f"Your summ is {summ}")