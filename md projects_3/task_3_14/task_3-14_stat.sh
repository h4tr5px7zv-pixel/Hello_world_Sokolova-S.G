#!/bin/bash
# Скрипт для статистического анализа оценок студентов из файла students.txt

echo "=== СТАТИСТИЧЕСКИЙ АНАЛИЗ ОЦЕНОК ==="
echo "Исходные данные:"
cat students.txt
echo ""

# Сумма всех оценок
sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $sum"

# Средняя оценка
average=$(awk '{sum += $2; count++} END {print sum/count}' students.txt)
echo "Средняя оценка: $average"

# Максимальная оценка
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)
echo "Максимальная оценка: $max"

# Дополнительно: минимальная оценка
min=$(awk 'NR==1{min=$2} $2<min{min=$2} END {print min}' students.txt)
echo "Минимальная оценка: $min"

# Дополнительно: количество студентов
count=$(wc -l < students.txt)
echo "Количество студентов: $count"

