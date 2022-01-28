proceeds = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
if proceeds > costs:
    profit = proceeds - costs
    print("Фирма работает с прибылью")
    print(f"Рентабельность выручки составила {profit/proceeds}")
    employees = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сотрудника сотавила {profit // employees}")
elif proceeds == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")