a = [[0,0,0,0,0],
 	 [0,0,1,0,0],
 	 [0,1,1,1,0],
 	 [0,0,1,0,0],
 	 [0,0,0,0,0]]

#a = [[0,1,0],
#	 [1,1,1],
#	 [0,1,0]]

def imprimirTabla(tabla):
	for k in tabla:
		for j in k:
			print j,
		print

def revisarVecinos(tabla, pos): ##Revision de los vecinos de cada posicion
	print str(pos)

	if pos == (0,0):
			print "soy cero cesro"
			for k in tabla[0:pos[0]+2]:
				for j in k[0:pos[1]+2]:
					print j,
				print
			print "******************"

	elif pos[0] == 0:
		for k in tabla[0:pos[0]+2]:
			for j in k[pos[1]-1:pos[1]+2]:
				print j,
			print
		print "******************"
		
	elif pos[1] == 0:
			for k in tabla[pos[0]-1:pos[0]+2]:
				for j in k[0:pos[1]+2]:
					print j,
				print
			print "******************"
	
	else:
		for k in tabla[pos[0]-1:pos[0]+2]:
			for j in k[pos[1]-1:pos[1]+2]:
				print j,
			print
		print "******************"

c = 0


print "\n"
vecinosVivos = 0
for i in range(5):
	for j in range(5):
			print str(i)+"-"+str(j)
			revisarVecinos(a,(i,j))
		
c = c+1
imprimirTabla(a)
print "--------------------------"
print "\n"




