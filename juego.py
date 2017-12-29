a = [[0,0,0,0,0],
	 [0,0,1,0,0],
	 [0,1,1,1,0],
	 [0,0,1,0,0],
	 [0,0,0,0,0]]

def imprimirTabla(tabla):
	for k in tabla:
		for j in k:
			print j,
		print

def revisarVecinos(tabla, pos):
	print str(pos[0])

c = 0
while c < 5:
	imprimirTabla(a)
	print "\n"
	vecinosVivos = 0
	for i in range(5):
		for j in range(5):
			revisarVecinos(a,(i,j))
			
	c = c+1
	imprimirTabla(a)
	print "\n"
	



