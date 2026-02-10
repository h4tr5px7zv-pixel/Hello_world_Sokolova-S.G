# Ввод данных от пользователя
reagent_name = input("Введите название нового реактива: ")
reagent_quantity = int(input("Введите количество (целое число): "))

# Вывод отчета в консоль
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report)

# Запись отчета в файл inventory.txt
with open("inventory.txt", "a", encoding="utf-8") as file:
    file.write(report + "\n")

print("Отчет сохранен в файл inventory.txt")