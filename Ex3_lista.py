from math import *
def distancia(x1,y1,x2,y2):
	return sqrt((x1-x2)**2+(y1-y2)**2)

def angulo(x1,y1,x2,y2):
	return atan((y1-y2)/(x1-x2))


print('Calcule a distancia entre dois pontos cartesianos')
x1=float(raw_input('digite acoordenada x1: '))
y1=float(raw_input('digite acoordenada y1: '))
x2=float(raw_input('digite acoordenada x2: '))
y2=float(raw_input('digite acoordenada y2: '))
modulo=distancia(x1,y1,x2,y2)
angulo=angulo(x1,y1,x2,y2)
print('o modulo e: ', modulo)
print('o angulo e: ', angulo)
raw_input()

# Nota: 1.0
# Nice work!
