#!/bin/bash
# Скрипт для анализа оценок студентов из файла students.txt

echo "=== АНАЛИЗ ОЦЕНОК СТУДЕНТОВ ==="
echo "Исходные данные:"
cat students.txt
echo ""

echo "=== СТУДЕНТЫ С ОЦЕНКОЙ ВЫШЕ 80 ==="
awk '$2 > 80 {print $0}' students.txt
echo ""

echo "=== СТУДЕНТЫ С ОЦЕНКОЙ НИЖЕ 70 ==="
awk '$2 < 70 {print $0}' students.txt
echo ""

echo "=== ТОЛЬКО ПЕРВАЯ СТРОКА ФАЙЛА ==="
head -n 1 students.txt

