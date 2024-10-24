def solve_equation(a, b, c):
    x = a - b - 4 * c
    return x

# Ввод значений a, b и c
try:
    a = float(input("Введите значение a (рациональное число): "))
    b = float(input("Введите значение b (рациональное число): "))
    c = float(input("Введите значение c (рациональное число): "))
    
    # Решение уравнения
    x = solve_equation(a, b, c)
    
    print(f"Решение уравнения x = {a} - {b} - 4 * {c} равно: x = {x}")
except ValueError:
    print("Ошибка: введите корректные рациональные числа.")
