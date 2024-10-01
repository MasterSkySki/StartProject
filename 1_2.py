# Определяем функцию для проверки билета
def is_lucky_ticket(number):
    # Преобразуем число в строку для удобства работы с отдельными цифрами
    str_number = str(number)
    
    # Проверяем, что номер является шестизначным
    if len(str_number) != 6:
        return "Номер должен быть шестизначным"
    
    # Извлекаем первые и последние три цифры
    first_half = str_number[:3]
    second_half = str_number[3:]
    
    # Вычисляем суммы первых и последних трех цифр
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    
    # Сравниваем суммы и возвращаем результат
    if sum_first_half == sum_second_half:
        return "Счастливый билет"
    else:
        return "Несчастливый билет"

# Примеры использования
number = 123456
print(f"Билет {number}: {is_lucky_ticket(number)}")

number = 123321
print(f"Билет {number}: {is_lucky_ticket(number)}")