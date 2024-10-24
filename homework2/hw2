def decimal_to_binary(n):
    if n < 0:
        return '-' + bin(-n)[2:]  # Убираем '0b' и добавляем знак
    return bin(n)[2:]  # Убираем '0b'

def decimal_to_octal(n):
    if n < 0:
        return '-' + oct(-n)[2:]  # Убираем '0o' и добавляем знак
    return oct(n)[2:]  # Убираем '0o'

def main():
    try:
        number = int(input("Введите целое десятичное число: "))
        
        binary = decimal_to_binary(number)
        octal = decimal_to_octal(number)
        
        print(f"Двоичное представление: {binary}")
        print(f"Восьмеричное представление: {octal}")
    
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()
