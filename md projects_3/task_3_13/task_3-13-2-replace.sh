#!/bin/bash
# Скрипт для замены пробелов на табуляцию в файле sequences.txt

sed -i 's/ /\t/g' sequences.txt

echo "Замена пробелов на табуляцию выполнена в файле sequences.txt"

