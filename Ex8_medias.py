def maiornota(notas):
	x=0
	for i in notas:
		if i>=x:
			x=i
	print 'Sua maior nota e: ', x 





x=0
i=0
soma=0
h=1
notas=[]
print 'Faca uma media para n numeros'
while (x!=-1):
	while True:
		try:
			x=int(raw_input('digite o %i numero: ' % h))
			break
		except:
			print "voce nao digitou um numero valido"
	notas.append(x)	
	if x<>-1:
		soma= x+soma
		i=i+1
		h=h+1
if i<>0:
	resultado= soma/i
	print 'a media e: %i' % resultado
else:
	print 'voce nao inseriu nenhuma nota'
maiornota(notas)
