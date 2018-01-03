lista = [0,1,2]
matriz = [[0,1,2],[0,2,3],[2,3,4]]
 

def imprimirLista(a):
	if len(a) == 1:
		return str(a[0])
	else:
		return str(a[0]) + str(imprimirLista(a[1:]))



def imprimirMatriz(a):
	if len(a) == 1:
		return str(imprimirLista(a[0]))
	else:
		return str(imprimirLista(a[0]))+"\n"+str(imprimirMatriz(a[1:]))


print imprimirMatriz(matriz)	