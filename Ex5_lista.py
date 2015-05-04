from math import *
def calculalat(x,y,z):
	lamb=atan(y/x)
	return lamb

def calculalong(x,y,z):
	h=0
	N=1
	P=sqrt(x**2+y**2)
	a=6378160
	E=0.00669454185
	for i in range(5):
		f=atan((z/P)*(1-E*(N/(N+h))))
		N=a/(sqrt(1-E*sin(f)**2))
		h=(P/cos(f))-N
	return f, h

print('Calculo da latitude, longitude, altitude de uma coordenada cartesiana:')
x=float(raw_input('Insira a coordenada cartesiana x: '))
y=float(raw_input('Insira a coordenada cartesiana y: '))
z=float(raw_input('Insira a coordenada cartesiana z: '))
lat=calculalat(x,y,z)*180/pi
lon=calculalong(x,y,z)[0]*180/pi
h=calculalong(x,y,z)[1]
print 'Os valores das coordenadas graficas sao:'
print'Longitude:', lat
print'Latitude: ',lon
print'Altitude:', h
raw_input()

# Nota: 1.0
# Good job!
