x=0
i=0
soma=0
h=1
print 'Faca uma media para n numeros'
while (x!=-1):
	x=int(raw_input('digite o %i numero: ' % h))
	if x<>-1:
		soma= x+soma
		i=i+1
		h=h+1
if i<>0:
	resultado= soma/i
	print 'a media e: %i' % resultado
else:
	print 'voce nao inseriu nenhuma nota'
