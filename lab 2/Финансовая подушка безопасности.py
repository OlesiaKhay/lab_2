money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

number_month = 0
ostatok = money_capital

while True:
    ostatok = ostatok + salary - spend * (1 + increase) ** number_month
    if ostatok <= 0:
        break
    number_month += 1

print("Количество месяцев, которое можно протянуть без долгов:", number_month)
