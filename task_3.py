"""Задание 3 - Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

number_1 = input("Enter a number: ")
number_2 = number_1 + number_1
number_3 = number_2 + number_1
sum_1_3 = int(number_1) + int(number_2) + int(number_3)
print(f"Sum = {sum_1_3}")
