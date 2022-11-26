"""Задание 4 -	Пользователь вводит целое положительное число.
 Найдите самую большую цифру в числе. Для решения используйте цикл while
  и арифметические операции."""

input_number = input("Enter a natural number: ")
i = 1
max_number = int(input_number[0])
while i < len(input_number):
    if int(input_number[i]) > max_number:
        max_number = int(input_number[i])
    i += 1
print(f"Maximum digit in your number: {max_number}")
