#!/bin/bash
# Скрипт для обработки файла students.txt

echo "=== ИСХОДНЫЙ ФАЙЛ students.txt ==="
cat students.txt
echo ""

echo "=== ТОЛЬКО ИМЕНА СТУДЕНТОВ ==="
awk '{print $1}' students.txt
echo ""

echo "=== ТОЛЬКО ОЦЕНКИ ==="
awk '{print $2}' students.txt
echo ""

echo "=== НОМЕР СТРОКИ И ИМЯ ==="
awk '{print NR ".", $1}' students.txt

