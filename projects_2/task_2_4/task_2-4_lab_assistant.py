print("=== Лабораторный помощник: Приготовление физиологического раствора ===")
volume = float(input("Введите нужный объем раствора (в мл): "))

salt_mass = volume * 0.009

water_volume = volume

rounded_volume = round(volume, 2)
rounded_salt_mass = round(salt_mass, 2)

with open("recipe.txt", "w", encoding="utf-8") as file:
    
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")  
    file.write(f"Общий объем: {rounded_volume} мл\n")
    file.write(f"Масса соли:  {rounded_salt_mass} г\n")
    file.write(f"Объем воды:  {rounded_volume} мл\n")

print("\n✅ Рецепт успешно сохранен в файл recipe.txt")

print("\n--- Содержимое файла recipe.txt ---")
with open("recipe.txt", "r", encoding="utf-8") as file:
    print(file.read())