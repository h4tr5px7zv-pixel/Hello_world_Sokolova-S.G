# Сбор данных
researcher = input("Введите ФИО исследователя: ")
date = input("Введите дату (например, 08.02.2026): ")
experiment = input("Введите название эксперимента: ")
conclusion = input("Введите вывод эксперимента: ")

# Ширина рамки (можно менять)
width = 50

# Формирование рамки и записи в файл
with open("journal.txt", "w", encoding="utf-8") as file:
    # Верхняя граница
    file.write(f"+{'-' * (width - 2)}+\n")
    
    # Заголовок
    title = "Электронный лабораторный журнал"
    file.write(f"| {title:{(width - 3)}}|\n")
    
    # Разделитель после заголовка
    file.write(f"+{'-' * (width - 2)}+\n")
    
    # Данные исследователя
    file.write(f"| ФИО исследователя : {researcher:{(width - 25)}}|\n")
    file.write(f"| Дата             : {date:{(width - 25)}}|\n")
    file.write(f"| Эксперимент      : {experiment:{(width - 25)}}|\n")
    
    # Разделитель перед выводом
    file.write(f"+{'-' * (width - 2)}+\n")
    
    # Вывод
    file.write(f"| Вывод:                                           |\n")
    
    # Разбиваем вывод на строки по ширине
    words = conclusion.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= width - 4:  # 4 символа на рамку и пробелы
            line += word + " "
        else:
            file.write(f"| {line:<{(width - 3)}}|\n")
            line = word + " "
    if line:
        file.write(f"| {line:<{(width - 3)}}|\n")
    
    # Нижняя граница
    file.write(f"+{'-' * (width - 2)}+\n")

print("Журнал сохранен в файл journal.txt")