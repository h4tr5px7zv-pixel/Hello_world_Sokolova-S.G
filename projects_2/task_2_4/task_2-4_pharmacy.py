print("=== Фасовка пробиотиков ===")

total_capsules = int(input("Введите общее количество произведенных капсул: "))

pack_capacity = int(input("Введите количество капсул в одной упаковке: "))
full_packs = total_capsules // pack_capacity

remaining_capsules = total_capsules % pack_capacity

print(f"\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remaining_capsules}")

print(f"\n--- Проверка расчётов ---")
print(f"Всего капсул по расчёту: {full_packs} × {pack_capacity} + {remaining_capsules} = {full_packs * pack_capacity + remaining_capsules}")

if remaining_capsules > 0:
    print(f"\n⚠️ Внимание: {remaining_capsules} капсул{'а' if remaining_capsules == 1 else 'ы' if 2 <= remaining_capsules <= 4 else ''} не помещаются в полную упаковку.")
    print(f"   Требуется дополнительная упаковка или перефасовка.")
else:
    print(f"\n✅ Отлично! Все капсулы идеально распределились по упаковкам.")