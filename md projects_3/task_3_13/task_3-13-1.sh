#!/bin/bash
# Скрипт для замены пути к базе данных в файле settings.php

sed -i 's:/var/lib/mysql/data:/mnt/ssd/mysql:' settings.php

echo "Замена пути выполнена в файле settings.php"

