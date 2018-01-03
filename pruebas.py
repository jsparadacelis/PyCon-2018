a = [0,1,2]

def imprimirLista(a):

	if len(a) == 1:
		print str(a[0])
	else:
		print str(a[0])
		return imprimirLista(a[1:])

imprimirLista(a)
