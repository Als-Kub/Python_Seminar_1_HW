"""Задание 2 -	Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк."""


input_seconds = int(input("Enter time in seconds: "))
hours = input_seconds//3600
if hours < 10:
    hours = "0" + str(hours)
minutes = input_seconds % 3600 // 60
if minutes < 10:
    minutes = "0" + str(minutes)
seconds = input_seconds % 3600 % 60
if seconds < 10:
    seconds = "0" + str(seconds)
print(f"{hours}:{minutes}:{seconds}")
