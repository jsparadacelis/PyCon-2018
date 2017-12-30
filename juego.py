# a = [[0,0,0,0,0,0],
#  	 [0,0,1,1,0,0],
#  	 [0,1,0,0,1,0],
#  	 [0,0,1,0,1,0],
#  	 [0,0,0,1,0,0],
#  	 [0,0,0,0,0,0]]

a = [[0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,1,0,0,0,0],
 	 [0,0,0,0,1,0,0,0,0,0],
 	 [0,0,0,0,1,1,1,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0]]

#a = [[0,1,0],
#	 [1,1,1],
#	 [0,1,0]]

def imprimirTabla(tabla):
	for k in tabla:
		for j in k:
			print j,
		print

def revisarVecinos(tabla, pos): ##Revision de los vecinos de cada posicion
	
	vecinos = 0
	if pos == (0,0):
		for k in tabla[0:pos[0]+2]:
			for j in k[0:pos[1]+2]:
				if j == 1:
					vecinos+=1

	elif pos[0] == 0:
		for k in tabla[0:pos[0]+2]:
			for j in k[pos[1]-1:pos[1]+2]:
				if j == 1:
					vecinos+=1

	elif pos[1] == 0:
		for k in tabla[pos[0]-1:pos[0]+2]:
			for j in k[0:pos[1]+2]:
				if j == 1:
					vecinos+=1
	
	else:
		for k in tabla[pos[0]-1:pos[0]+2]:
			for j in k[pos[1]-1:pos[1]+2]:
				if j == 1:
					vecinos+=1



	if(tabla[pos[0]][pos[1]] == 1):
		vecinos = vecinos -1

	
	return vecinos
 

#Una celula muerta con exactamente 3 celulas vecinas vivas "nace" (es decir, al turno siguiente estara viva).
#Una celula viva con 2 o 3 celulas vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblacion").

print "\n"
vecinosVivos = 0
imprimirTabla(a)
print "--------------------------"
print "\n"

t = [[0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0]]

for i in range(10):
	for j in range(10):
		
		vecinosVivos = revisarVecinos(a,(i,j))
		
		if a[i][j] == 0 and vecinosVivos == 3:
			t[i][j] = 1
		elif a[i][j] == 1 and vecinosVivos < 2:
			t[i][j] = 0
		elif a[i][j] == 1 and vecinosVivos > 3:
			t[i][j] = 0
		elif a[i][j] == 1 and (vecinosVivos == 2 or vecinosVivos == 3):
			t[i][j] = 1

		


imprimirTabla(t)
print "--------------------------"
print "\n"

r = [[0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0],
 	 [0,0,0,0,0,0,0,0,0,0]]

for i in range(10):
	for j in range(10):
		vecinosVivos = revisarVecinos(t,(i,j))
		if t[i][j] == 0 and vecinosVivos == 3:
			r[i][j] = 1
		elif t[i][j] == 1 and vecinosVivos < 2:
			r[i][j] = 0
		elif t[i][j] == 1 and vecinosVivos > 3:
			r[i][j] = 0
		elif t[i][j] == 1 and (vecinosVivos == 2 or vecinosVivos == 3):
			r[i][j] = 1


imprimirTabla(r)
print "--------------------------"
print "\n"




