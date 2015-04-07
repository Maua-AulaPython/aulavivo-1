from math import *
import os

def distancia(x1,y1,x2,y2):
	return sqrt((x1-x2)**2+(y1-y2)**2)


def maior(x,y):
	tamanho=len(x)
	i=0
	j=1
	dist=-1
	l=1
	distmaior=-1
	while i<len(x):
		for h in range(len(x) - l):
			dist=distancia(x[i],y[i],x[j],y[j])
			if dist>=distmaior:
				distmaior=dist
			j=j+1
		i=i+1
		j=i+1
		l=l+1
	return distmaior






aux='s'
i=1
x=[]
y=[]
while aux=='s':
	os.system('cls')
	print('Calculo da maior distancia entre n pontos')
	print('insira o %i ponto:'% i)
	x1=float(raw_input('digite o x: '))
	x.append(x1)
	y1=float(raw_input('digite o y: '))
	y.append(y1)
	aux=raw_input('deseja colocar mais pontos? s/n: ')
resposta=maior(x,y)
print('a maior distancia e: ', resposta)
raw_input()
