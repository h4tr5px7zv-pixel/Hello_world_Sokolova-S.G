 
print("Введите данные о составе продукта (в граммах):")

proteins = float(input("Белки: "))

fats = float(input("Жиры: "))

carbohydrates = float(input("Углеводы: "))
 
calories = (proteins * 4) + (fats * 9) + (carbohydrates * 4)

print(f"\nОбщая калорийность продукта: {calories:.2f} ккал")

print(f"\nДетальный расчёт:")
print(f"Белки: {proteins} г × 4 = {proteins * 4:.2f} ккал")
print(f"Жиры: {fats} г × 9 = {fats * 9:.2f} ккал")
print(f"Углеводы: {carbohydrates} г × 4 = {carbohydrates * 4:.2f} ккал")