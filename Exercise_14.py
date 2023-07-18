# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

your_number = int(input("Input your number: "))

list_of_degrees = []
for i in range(your_number+1):
    if 2**i <= your_number:
        list_of_degrees.append(i)

print(f"Possible degrees: {list_of_degrees}")
print("2 in further degrees will exceed your number")
