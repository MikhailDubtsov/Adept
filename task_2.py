# Параметры
disk_size_mb = 1.44  # объем дискеты в Мб
pages_per_book = 100  # количество страниц в книге
lines_per_page = 50   # количество строк на странице
chars_per_line = 25   # количество символов в строке
bytes_per_char = 4    # количество байт на символ

disk_size_bytes = disk_size_mb * 1024 * 1024  # Мб в байты

book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

number_of_books = disk_size_bytes // book_size_bytes

print(f"Количество книг, помещающихся на дискету:{number_of_books}")
