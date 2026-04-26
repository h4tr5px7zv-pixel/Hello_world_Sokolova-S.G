# task_4-13-1.py
# Программа для нахождения минимального из четырёх чисел

# Ввод четырёх чисел
A = float(input("Введите первое число (A): "))
B = float(input("Введите второе число (B): "))
C = float(input("Введите третье число (C): "))
D = float(input("Введите четвёртое число (D): "))

# Принимаем A за текущий минимум
min_value = A

# Сравниваем с B
if min_value > B:
    min_value = B

# Сравниваем с C
if min_value > C:
    min_value = C

# Сравниваем с D
if min_value > D:
    min_value = D

# Вывод результата
print(f"Минимальное из чисел {A}, {B}, {C}, {D} равно {min_value}")