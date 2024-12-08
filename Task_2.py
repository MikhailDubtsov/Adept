def find_common_participants(group1, group2, delimiter="|"):
    """
    Функция для нахождения общих участников между двумя группами.

    :param group1: Участники первой группы в виде строки
    :param group2: Участники второй группы в виде строки
    :param delimiter: Разделитель между участниками (по умолчанию "|")
    :return: Список общих участников, отсортированный в алфавитном порядке
    """
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим общих участников
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants

# Исходные строки с участниками
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Вызов функции для проверки работы
common = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common)

# Проверка работы функции с разделителем, отличным от "|"
participants_third_group = "Петров,Сидоров,Смирнов"
common_with_comma = find_common_participants(participants_first_group, participants_third_group, delimiter=",")
print("Общие участники с запятой:", common_with_comma)
