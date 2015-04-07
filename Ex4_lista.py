# -*- coding: utf-8 -*-

from math import *
def verifica(a,b,c):
	if((a+b)>c):
		return True
	else:
		return False

def area(a,b,c):
	area= (a*b)/2
	return area

print('Verifique se um triangulo e retangulo:')
a=int(raw_input('insira o primeiro cateto: '))
b=int(raw_input('insira o segundo cateto: '))
c=int(raw_input('insira a hipotenusa: '))
if verifica(a,b,c):
	area=area(a,b,c)
	print 'O triangulo eh retangulo e sua area e: ', area
else:
	print 'O triangulo nao eh retangulo, seus valores sao: \n A=%i \n B=%i \n C=%i', a,b,c
raw_input()
