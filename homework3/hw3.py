# Номер ЗК 22130337
def decimal_to_base12(n):
    if n == 0:  # Базовый случай
        return ""
    else:
        remainder = n % 12
        # Для представления чисел больше 9 используем буквы A и B
        if remainder >= 10:
            remainder = chr(remainder + 55)  # A - 65, B - 66
        else:
            remainder = str(remainder)
        return decimal_to_base12(n // 12) + remainder

def get_valid_input():
    user_input = input("Введите целое неотрицательное десятичное число: ")
    try:
        number = int(user_input)
        if number < 0:
            raise ValueError("Число должно быть неотрицательным.")
        return number
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")
        return get_valid_input()  # Рекурсивный вызов для повторного ввода

number = get_valid_input()

if number == 0:
    print("0 в двенадцатеричной системе: 0")
else:
    result = decimal_to_base12(number)
    print(f"{number} в двенадцатеричной системе: {result}")
