#!/bin/bash

FILE_PATH="./system.log"
ERROR_CODE=1

# 1. Проверка существования файла
if [ -f "$FILE_PATH" ]; then
    echo "Лог-файл найден."
else
    echo "Ошибка: файл не существует."
fi

# 2. Анализ кода ошибки через case
case $ERROR_CODE in
    0)
        echo "Статус: Ошибок нет." ;;
    1)
        echo "Статус: Критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac

