def replace_missing_with_average(numbers):

    missing_index = numbers.index(None)

    total_sum = sum(num for i, num in enumerate(numbers) if i != missing_index)

    count = len(numbers)

    average = total_sum / (count - 1)

    numbers[missing_index] = average
    return numbers

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
result = replace_missing_with_average(numbers)
print(result)