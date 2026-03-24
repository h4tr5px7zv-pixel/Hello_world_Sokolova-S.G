#!/bin/bash
# Скрипт для создания и удаления файлов

echo "=== СОЗДАНИЕ ФАЙЛОВ ==="

# Создаем 10 файлов с именами test1.txt ... test10.txt
for i in {1..10}; do
    filename="test$i.txt"
    touch "$filename"
    echo "Создан файл: $filename"
done

echo ""
echo "Список созданных файлов:"
ls -la test*.txt 2>/dev/null || echo "Файлы не найдены"

echo ""
echo "=== УДАЛЕНИЕ ФАЙЛОВ В ОБРАТНОМ ПОРЯДКЕ ==="

# Удаляем файлы в обратном порядке (от 10 до 1)
counter=10
while [ $counter -ge 1 ]; do
    filename="test$counter.txt"
    
    # Проверяем, существует ли файл перед удалением
    if [ -f "$filename" ]; then
        rm "$filename"
        echo "Удален файл: $filename"
    else
        echo "Файл $filename не найден"
    fi
    
    counter=$((counter - 1))
done

echo ""
echo "Проверка оставшихся файлов:"
ls -la test*.txt 2>/dev/null || echo "Все файлы удалены"

