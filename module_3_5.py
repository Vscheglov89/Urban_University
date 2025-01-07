def get_multiplied_digits(number): # Преобразуем число в строку для обработки
    str_number = str(number)

    if number == 0: # Если число равно 0, возвращаем 0
        return 0

    product = 1 # Инициализируем произведение

    for digit in str_number:
        digit_value = int(digit)
        if digit_value != 0:  # Игнорируем нули
            product *= digit_value

    return product


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)