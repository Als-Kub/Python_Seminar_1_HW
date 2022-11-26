"""Задание 1 - Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран."""

name = input("Hello! What's your name? Tell me, please:")
print(f"Nice to meet you, {name}!")
number_1 = int(input(f"{name}, enter the first number, please: "))
number_2 = int(input(f"{name}, enter the first number, please: "))
sum_numbers = number_1 + number_2
print(f"Sum of your numbers is equal to: {sum_numbers}")
