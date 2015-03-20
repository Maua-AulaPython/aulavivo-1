def verificapar(x):
	a=x%2
	if (a==0):
		print 'E um numero par'
	else:
		print 'E um numero impar'

x=int(raw_input('insira um numero inteiro: '))
verificapar(x)
raw_input()
