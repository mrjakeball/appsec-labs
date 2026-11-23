import math

expression = input("Введите выражение: ")
parts = expression.split()
try:
    if len(parts) == 3:
        first_number = float(parts[0])
        second_number = float(parts[2])
        if math.isfinite(first_number) and math.isfinite(second_number):
            if parts[1] == "+":
                print(f"Результат: {first_number + second_number}")
            elif parts[1] == "-":
                print(f"Результат: {first_number - second_number}")
            elif parts[1] == "*":
                print(f"Результат: {first_number * second_number}")
            elif parts[1] == "/":
                if second_number != 0:
                    print(f"Результат: {first_number / second_number}")
                else:
                    print("На ноль делить нельзя!")
            else:
                print("Неизвестная операция!")
        else:
            print("Ошибка: допускаются только конечные числа!")
    else:
        print("Неверный формат ввода!")
except ValueError:
    print("Неверный формат ввода!")
