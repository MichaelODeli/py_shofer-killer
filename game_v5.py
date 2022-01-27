import turtle as tr
import pymsgbox as pmsg
import math
import PySimpleGUI as sg

# показатель инерционности. единица - шофер направлен прямо на пешехода. задается от 0.5 до 1.0
inerzion = 0.6

# проводим проверку вводимых данных пользователем
sg.theme('DarkBlue2')
layoutParam = [
    [sg.Text('Основные условия', font='Arial')],
    [sg.Text('Координаты шофера X - '), sg.Input(size=5, default_text='-10'), sg.Text('Y - '), sg.Input(size=5, default_text='3'), sg.Text('Скорость шофера (до 20)'), sg.Input(size=5, default_text='20')],
    [sg.Text('Координаты пешехода X - '), sg.Input(size=5, default_text='-2'), sg.Text('Y - '), sg.Input(size=5, default_text='3'), sg.Text('Скорость пешехода (до 20)'), sg.Input(size=5, default_text='10')],
    [sg.Text('Длина стороны квадрата (от 100 до 1000)'), sg.Input(default_text='400', size=5)],
    [sg.Text()],
    [sg.Text('Дополнительные условия', font='Arial')],
    [sg.Checkbox('Идеальные условия (нет инерциальности у шофера)')],
    [sg.Text('Радиус встречи шофера и пешехода (не обязательно)'), sg.Input(default_text='5', size=5)],
    [sg.Text('NEW!'), sg.Checkbox('Нововведения в движении пешехода')],
    [sg.Text('NEW!'), sg.Checkbox('Нововведения в движении шофера')],
    [sg.Text('NEW!'), sg.Text('Данные усовершенствования описаны в официальном GitHub проекта')],
    [sg.Submit(button_text='Начать игру'), sg.Submit(button_text='Выход')]
]
window = sg.Window('Параметры игры', layoutParam)
ticker = False
while ticker!=True:
    event, values = window.read()
    if event in (None, 'Выход', 'Cancel'):
        exit('User stopped the game')
    if event in ('Начать игру'):
        if values[0]=='' or values[1]=='' or values[2]=='' or values[3]=='' or values[4]=='' or values[5]=='' or values[6]=='':
            pmsg.alert(text='Ошибка ввода (Основные параметры не заданы).\nПопробуйте снова.', title='Ошибка при выполнении программы')
        else:
            x_sh = int(values[0])
            y_sh = int(values[1])
            sp_sh = int(values[2])
            x_p = int(values[3])
            y_p = int(values[4])
            sp_p = int(values[5])
            square = int(values[6])
            nice = 0
            if square<100 or square>1000:
                nice = 1
            elif square>=100 and square<=333:
                s = str(int(square/10))
            elif square>=334 and square<=666:
                s = str(int(square/20))
            else:
                s = str(int(square/30))
            if values[8]!='':
                radius = int(values[8])
                dop_uslovia = True
            if values[8]=='': 
                dop_uslovia = False
            if values[10]==True and dop_uslovia == False:
                pmsg.alert(text='Ошибка ввода (для новой стратегии шофера не задан радиус поиска).\nПопробуйте снова, .', title='Ошибка при выполнении программы')
            elif abs(x_sh)>int(s) or abs(y_sh)>int(s) or abs(x_p)>int(s) or abs(y_p)>int(s):
                pmsg.alert(text='Ошибка ввода (координаты игроков выходят за пределы игрового поля).\nПопробуйте снова, .', title='Ошибка при выполнении программы')
            elif nice == 1:
                pmsg.alert(text='Ошибка ввода (квадрат имеет сторону более 1000 или менее 100).\nПопробуйте снова.', title='Ошибка при выполнении программы') # v3
            else:
                if square>=100 and square<=333:
                    x_sh = x_sh * 10
                    y_sh = y_sh * 10
                    x_p = x_p * 10
                    y_p = y_p * 10
                elif square>=334 and square<=666:
                    x_sh = x_sh * 20
                    y_sh = y_sh * 20
                    x_p = x_p * 20
                    y_p = y_p * 20
                else:
                    x_sh = x_sh * 30
                    y_sh = y_sh * 30
                    x_p = x_p * 30
                    y_p = y_p * 30
                ideal_uslovia = values[7]
                newStratPesh = values[9]
                newStratShof = values[10]
                ticker = True

# сначала координаты шофера, потом координаты пешехода



# # тестовые данные для отладки
# x_sh=200
# y_sh=40
# x_p=-40
# y_p=-70
# sp_sh=20
# sp_p=10
# square=400

def length(x1, y1, x2, y2):
    # расстояние между координатами
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def central(x1, y1, x2, y2):
    # точка по центру заданных координат
    x=(x1+x2)/2
    y=(y1+y2)/2
    return(x, y)

def win_check(x1, y1, x2, y2):
    if dop_uslovia==False and round(x1)==round(x2) and round(y1)==round(y2): # v1
        # условие, когда их координаты совпали - победил шофер
        return 1
    # check with https://profmeter.com.ua/communication/learning/course/course7/chapter0552/
    check = round((x2-x1)**2+(y2-y1)**2)
    if dop_uslovia==True and check<=radius**2: # v2
        # условие, когда их координаты совпали - победил шофер
        return 1
    elif math.fabs(x2)>=square or math.fabs(y2)>=square:
        # выход за пределы игрового поля - победил пешеход (именно его координаты проверям)
        # exit(0) # debug option
        return 2
    else:
        # print(check) # debug option
        return 0

def get_koef_sh(speed_pesh, speed_shof):
    return speed_shof/speed_pesh
    # соотношение, сколько проедет шофер за еденицу времени
    # учитывая, что за это же время пешеход пройдет 1 ед.

def move_pesh(x1, y1, x2, y2, til):
    # пешеход проходит 1 ед пути вне зависимости от условий
    # есть движение по углу, осталось найти этот самый угол
    if newStratPesh!=True:
        ac=math.sqrt((x2-x1)**2+(y2-y1)**2)
        ab=math.sqrt((y2-y1)**2)
        bc=math.sqrt((x2-x1)**2)
        ugol=math.degrees(math.acos(
            (bc**2+ac**2-ab**2)/(2*bc*ac)
        ))
        x21=x2+math.cos(math.radians(90+ugol))
        # необходимо добавить еще некоторые значения для верного подсчета
        if x21<=0:
            x21+=0.1
        else:
            x21+=0.2
        y21=y2+math.sin(math.radians(90-ugol))
        return(x21, y21)
    if newStratPesh==True:
        tiltt = til%5
        if tiltt!=0:
            ac=math.sqrt((x2-x1)**2+(y2-y1)**2)
            ab=math.sqrt((y2-y1)**2)
            bc=math.sqrt((x2-x1)**2)
            ugol=math.degrees(math.acos(
                (bc**2+ac**2-ab**2)/(2*bc*ac)
            ))
            x21=x2+math.cos(math.radians(90+ugol))
            # необходимо добавить еще некоторые значения для верного подсчета
            if x21<=0:
                x21+=0.1
            else:
                x21+=0.2
            y21=y2+math.sin(math.radians(90-ugol))
            return(x21, y21)
        else:
            if abs(x2)<=(square/2) and abs(x2)>=((square*0.9)/2):
                if x2<0:
                    x21=x2-1
                else:
                    x21=x2+1
                return(x21, y2)
            elif abs(y2)<=(square/2) and abs(y2)>=((square*0.9)/2):
                if y2<0:
                    y21=y2-1
                else:
                    y21=y2+1
                return(x2, y21)
            else:
                ac=math.sqrt((x2-x1)**2+(y2-y1)**2)
                ab=math.sqrt((y2-y1)**2)
                bc=math.sqrt((x2-x1)**2)
                ugol=math.degrees(math.acos(
                    (bc**2+ac**2-ab**2)/(2*bc*ac)
                ))
                x21=x2+math.cos(math.radians(90+ugol))
                # необходимо добавить еще некоторые значения для верного подсчета
                if x21<=0:
                    x21+=0.1
                else:
                    x21+=0.2
                y21=y2+math.sin(math.radians(90-ugol))
                return(x21, y21)
def move_shof(x1, y1, x2, y2,):
    d=get_koef_sh(sp_p, sp_sh)
    ax=x1
    ay=y1
    bx=x2
    by=y2
    # используя формулу, находим следующую точку по прямой
    # инерциальность еще в работе, возникли ошибки
    if ideal_uslovia==True:
        cx=ax+((d*(bx-ax))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
        cy=ay+((d*(by-ay))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
        return(cx, cy)
    else:
        if newStratShof!=True:
            newShx=ax+((d*(bx-ax))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
            newShy=ay+((d*(by-ay))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
            prevShx=x1
            peshX=x2
            if peshX>newShx:
                kf=abs(prevShx-newShx)
                kf=inerzion*kf
                newShx=prevShx+kf
            elif peshX<newShx:
                kf=abs(prevShx-newShx)
                kf=inerzion*kf
                newShx=prevShx-kf
            else:
                pass
            return(newShx, newShy)
        if newStratShof==True: # i dont do it, this is just zatravka
            newShx=ax+((d*(bx-ax))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
            newShy=ay+((d*(by-ay))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
            prevShx=x1
            peshX=x2
            if peshX>newShx:
                kf=abs(prevShx-newShx)
                kf=inerzion*kf
                newShx=prevShx+kf
            elif peshX<newShx:
                kf=abs(prevShx-newShx)
                kf=inerzion*kf
                newShx=prevShx-kf
            else:
                pass
            return(newShx, newShy)

try:
    # задаем начальные позиции в виде списка
    xSh=[int(x_sh)]
    ySh=[int(y_sh)]
    xP=[int(x_p)]
    yP=[int(y_p)]
    i=1 # счетчик
    while win_check(xSh[-1], ySh[-1], xP[-1], yP[-1])==0:
        # берем последнее значение и проводим манипуляции в отдельно вынесенной функции для шофера
        toMoveShof=move_shof(xSh[-1], ySh[-1], xP[-1], yP[-1])
        xSh.append(toMoveShof[0])
        ySh.append(toMoveShof[1])
        # аналогично для пешехода
        toMovePesh=move_pesh(xSh[-1], ySh[-1], xP[-1], yP[-1], i)
        xP.append(toMovePesh[0])
        yP.append(toMovePesh[1])
        i+=1 # увеличиваем счетчик
    print(i-1) # количество точек, которые прошли игроки
    winId=win_check(xSh[-1], ySh[-1], xP[-1], yP[-1]) # проверка на "выигрыш"
    if winId==2:
        pmsg.alert(text='Победил пешеход - выход за пределы игрового поля', title='Итоги игры')
    if winId==1:
        vmeste='( '+str(round(xP[-1], 1))+' ; '+str(round(yP[-1], 1))+' ) - точка встречи' # выводим положение точки встречи
        pmsg.alert(text='Победил водитель - догнал пешехода'+'\n'+vmeste, title='Итоги игры') # всплывающее окно с информацией
except MemoryError:
    pmsg.alert(text='ErrM - недостаточно ОЗУ для решения задачи', title='Ошибка при выполнении программы')
    exit('ErrM')
    # если ОЗУ будет переполнена от перебора решений - программа будет завершена. 
    # Во время пробных решений использование ОЗУ доходило до 1 Гб с 3 млн. значений в каждом из 4 списках
    
# координатная ось
tr.delay(1)
tr.pencolor('black')
tr.forward(square)
tr.backward(square*2)
tr.forward(square)
tr.left(90)
tr.forward(square)
tr.backward(square*2)
tr.up()

# txt='Если покажется, что прямые слишком ровные - обратите внимание,\nчто масштаб на рисунке 1 к 20. От этого не видно прямых углов.'
# pmsg.alert(text=txt, title='Предупреждение')
# построение движения пешехода
tr.delay(2)
tr.pencolor('blue')
tr.goto(xP[0], yP[0])
tr.down()
for i in range(len(xP)):
    tr.goto(xP[i], yP[i])
tr.up()

# построение движения шофера
tr.goto(xSh[0], ySh[0])
tr.down()
tr.pencolor('red')
for i in range(len(xSh)):
    tr.goto(xSh[i], ySh[i])
tr.done()