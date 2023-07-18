# Задача 10: На столе лежат n монеток. Некоторые из них 
# лежат вверх решкой, а некоторые – гербом. Определите 
# минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random
coin_head = 1
coin_tail = 0

i = 0

number_of_coins = int(input('Input the number of your coins: '))
while number_of_coins < 2:
    number_of_coins = int(input('There should be at least 2 coins. Try again: '))

coin_list = []
for i in range (number_of_coins):
    coin_list.append(random.randint(coin_tail, coin_head))
print(f"Coin results are: {coin_list}")

coin_head_count = 0
for i in range(number_of_coins):
    if coin_list[i] == coin_head:
        coin_head_count += 1
print(f"Resulting number of coin heads: {coin_head_count}")

coin_tail_count = 0
for i in range(number_of_coins):
    if coin_list[i] == coin_tail:
        coin_tail_count += 1
print(f"Resulting number of coin tails: {coin_tail_count}")

if coin_tail_count >= coin_head_count:
    print(f"Minimum coins to flip: {coin_head_count}")
else:
    print(f"Minimum coins to flip: {coin_tail_count}")
