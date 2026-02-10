operator = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n")
    file.write(f"{operator}\t\t{pressure_value} Па\n")
print("Данные успешно сохранены в sensor_log.txt")