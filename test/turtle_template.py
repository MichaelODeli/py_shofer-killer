from turtle import *
from pymsgbox import *
# http://itrobo.ru/programmirovanie/python/grafika-turtle-cherepashka-v-piton.html

# # координатная ось
# pencolor('blue')
# forward(300)
# backward(600)
# forward(300)
# left(90)
# forward(300)
# backward(600)

# два круга от центра
# up()
# goto(200, 0)
# down()
# circle(200)
# up()
# goto(250, 0)
# down()
# circle(250)

# текст
# up()
# goto(0, -350)
# down()
# write('Do you know it?', False, 'center', font = ('Arial', 20, 'normal'))
# done()

# воскл знак
up()
goto(0, -200)
down()
left(90)
pnsz=int(prompt(text='Введите начальный размер кисти\nEnter start size of brush', title='Ввод данных')) # можно сделать ввод прямо во время выполнения хе-хе
while pnsz!=60:
    forward(10)
    pensize(pnsz)
    pnsz+=1
up()
goto(0, -240)
down()
dot(60)


done()