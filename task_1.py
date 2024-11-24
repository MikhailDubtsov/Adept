money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
def calculate_months(money_capital, salary, spend, increase):
    months = 0  # Счетчик месяцев
    while money_capital + salary >= spend:  # Проверка бюджета
        months += 1  # Увеличиваем счетчик месяцев
        money_capital -= spend  # Уменьшаем подушку безопасности на текущие расходы
        spend *= (1 + increase)  # Увеличиваем расходы на 5% для следующего месяца
    return months  # Возвращаем количество месяцев
months = calculate_months(money_capital, salary, spend, increase)
print("Количество месяцев, которое можно протянуть без долгов:", months)
