import math
# тестовые данные
x1=-300
y1=-50
x2=50
y2=80
ax=x1
ay=y1
bx=x2
by=y2
d=2
g=ax+((d*(bx-ax))/(math.sqrt((bx-ax)*(bx-ax)+(by-ay)*(by-ay))))
h=ay+((d*(by-ay))/(math.sqrt((bx-ax)**2+(by-ay)**2)))
print(g)
print(h)
# нужно вычислить угол с помощью поиска угла наклона графика и арктангенса данного угла
x3=x1
y3=y2
ac=math.sqrt((x2-x1)**2+(y2-y1)**2)
ab=math.sqrt((y2-y1)**2)
bc=math.sqrt((x2-x1)**2)
ugol=math.degrees(math.acos(
    (bc**2+ac**2-ab**2)/(2*bc*ac)
))
print(ugol)
x21=x2+math.cos(math.radians(90+ugol))
if x21<=0:
    x21+=0.1
else:
    x21+=0.2
y21=y2+math.sin(math.radians(90-ugol))
print(x21)
print(y21)
