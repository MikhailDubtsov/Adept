import json
# TODO решите задачу
def task() -> float:
    # Чтение данных из JSON файла
    with open('input.json', 'r') as file:
        data = json.load(file)
    # Инициализация суммы
    total_sum = 0.0
    # Проход по каждому словарю в списке
    for item in data:
        # Вычисление произведения "score" и "weight"
        product = item.get("score", 0) * item.get("weight", 0)
        total_sum += product
    # Возврат суммы, округленной до 3 знаков после запятой
    return round(total_sum, 3)
print(task())
