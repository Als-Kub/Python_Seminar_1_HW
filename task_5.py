""" Задание 5 - Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника. """

income = int(input("Enter income: "))
costs = int(input("Enter costs: "))
if income > costs:
    profit_rate = (income - costs) / costs * 100
    print(f"Your business is profitable. Profitability = {profit_rate} %")
    staff_number = int(input("Enter number of employees: "))
    profit_staff = (income - costs) / staff_number
    print(f"Profit per employee = {profit_staff}")
elif income == costs:
    print("Your business is at the breakeven point.")
else:
    print("Your business is unprofitable.")

