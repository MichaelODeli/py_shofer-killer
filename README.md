# py_shofer-killer
Математическая дифференциальная игра, написанная на Python 3.8.6 64-bit

## Установка
Требуются установленные модули:
```
PyMsgBox==1.0.9
PySimpleGUI==4.56.0
```
Установите их с помощью команды для Windows-систем
```
pip install -r requirements.txt
```
или следующей командой для Linux-систем
```
pip3 install -r requirements.txt
```

## Использование
Следуйте инструкциям в программе

## Список версий
v1 (18/11/2021) - первый выпуск программы.

v2 (13/01/2022) - снижена инерциальность шофера; задан радиус окружности, при нахождении в которой шофера и пешехода, первый одержит победу.

v3 (24/01/2022) - возможность задать размеры квадрата для движения; проверка введенных значений; незначительные модификации кода; коды ошибок в консоли.

v4 (xx/02/2022) - новый интерфейс на PySimpleGUI

v5 (xx/02/2022) - нововведения в стратегии движения пешехода и шофера (подробнее в [updateLog.md](updateLog.md))

## Коды ошибок
`Err1` - ошибка ввода данных пользователем    
`ErrM` - недостаточно ОЗУ для решения задачи    
`ErrP` - ошибка при построении графика движения    