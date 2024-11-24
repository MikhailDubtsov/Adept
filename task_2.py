salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
def calculate_required_capital(salary, spend, months, increase):
    total_capital = 0  # Общая необходимая подушка безопасности
    for month in range(months):
        # Рассчитываем нехватку средств
        deficit = spend - salary
        if deficit > 0:  # Если недостаток средств есть
            total_capital += deficit  # Увеличиваем общую подушку безопасности
        # Увеличиваем расходы на 3% для следующего месяца
        spend *= (1 + increase)
    return round(total_capital)  # Возвращаем округленное значение
required_capital = calculate_required_capital(salary, spend, months, increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
