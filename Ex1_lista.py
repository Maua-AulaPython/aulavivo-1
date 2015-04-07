from math import *
def distancia(x1,y1,x2,y2):
	return sqrt((x1-x2)**2+(y1-y2)**2)


print('Calcule a distancia entre dois pontos cartesianos')
x1=float(raw_input('digite acoordenada x1: '))
y1=float(raw_input('digite acoordenada y1: '))
x2=float(raw_input('digite acoordenada x2: '))
y2=float(raw_input('digite acoordenada y2: '))
d=distancia(x1,y1,x2,y2)
print('a distancia e: ', d)
raw_input()
