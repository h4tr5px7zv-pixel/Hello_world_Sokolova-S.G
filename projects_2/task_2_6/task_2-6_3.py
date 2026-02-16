donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor not in ["I", "II", "III", "IV"] or recipient not in ["I", "II", "III", "IV"]:
    print("Ошибка: введена некорректная группа крови")
elif donor == "I":
    print(f"ПЕРЕЛИВАНИЕ ВОЗМОЖНО: донор с I группой (универсальный донор) может переливать кровь пациенту с {recipient} группой")
elif donor == recipient:
    print(f"ПЕРЕЛИВАНИЕ ВОЗМОЖНО: группы крови совпадают ({donor})")
else:
    print(f"ПЕРЕЛИВАНИЕ НЕВОЗМОЖНО: кровь донора ({donor}) не подходит пациенту с {recipient} группой")