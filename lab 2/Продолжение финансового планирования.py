salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
d = 0
i = 0

while True:
    money_capital = spend * (1 + increase) ** i - salary


    if i == months:
        break
    i += 1
    d = d + money_capital
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {d:.2f}")


