salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

difference = 0 #разница между тратами и зп
money_capital = 0 #финансовая подушка безопасности
i = 0

while True:
    difference = spend * (1 + increase) ** i - salary


    if i == months:
        break
    i += 1
    money_capital = money_capital + difference
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.2f}")

