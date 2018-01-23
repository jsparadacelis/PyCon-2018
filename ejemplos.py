from functools import reduce
from operator import mul
from itertools import islice
import timeit
naturales = range(1,11)


## Ejemplo No.1 Bucles en programacion imperativa
resultado = list()
for i in naturales:
	if(i % 2 == 0):
		resultado.append(i)



## Ejemplo No.2 Encapsulado funciones
def esPar(numero):
	return numero%2 == 0

def volverPar(numero):
	return numero/2

for i in naturales:
	if(esPar(i)):
		resultado.append(i)
		
## Ejemplo No. 3 Utilizando listas por comprension
#Ejemplo de listas por compresion
l2 = [n ** 2 for n in naturales] 
#equivalente a 
# l2 = []
# for n in naturales:
# 	l2.append(n**2)



##Ejemplo No. 4 Recursion


s = 0
for n in range(1, 11):
	s += n
##print(s)

##Lo anterior produce el mismo resultado que
def sum(seq):
	if len(seq) == 0: 
		return 0
	else:
		return seq[0] + sum(seq[1:])



def running_sum(numbers, start=0):
	if len(numbers) == 0:
		print()
		return
	total = numbers[0] + start
	print(total)
	running_sum(numbers[1:], total)

def sum(numbers):
	if len(numbers) == 1:
		return numbers[0]
	else:
		return numbers[0] + sum(numbers[1:])


def factorial(n):
	if n == 0 or n == 1: ##Caso base
		return 1
	else:
		return n*factorial(n-1)

## Aqui utilizamos reduce y el operador mul

def factorialHOF(n):
	return reduce(mul, range(1, n+1), 1)

##Utilizando las funciones lambda
def factorialReduce(n):
	return reduce(lambda x,y : x+y, [5,4],2)


mult_3_5 = lambda x: x%3==0 or x%5==0


#Ejemplo No. 5 utilizando la funcion map

def cuadrado(n):
	return n ** 2

l = [1, 2, 3]
l2 = map(cuadrado, l)

#Ejemplo No. 6 utilizando la funcion filter
def es_par(n):
	return (n % 2.0 == 0)

l = [1, 2, 3]
l2 = filter(es_par, l)


expr, res = "28*32***32**39", 1
for t in expr.split("*"):
    if t != "":
       res *= int(t)
  


expr = "28*32***32**39"
print filter(bool, expr.split("*"))


def factorial(numero):
	if numero == 0 or numero == 1:
		return 1
	else:
		return numero*factorial(numero-1)

print reduce(mul, map(int, filter(bool, expr.split("*"))), 1)
    
print factorial(5)

#Ejemplo  No. 6 Generadores 

def generator():
    i = 1
    while True:
        yield i
        i += 1

 
def take(n, iterable):
    return list(islice(iterable, n))
 
print take(5, generator())

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

#EJemplo de range entre Python2.X y Python 3.X
range(5)
#[1,2,3,4,5]

range(5)
#range(0,5) esto en python 3.X mismo resultado utilizando xrange() en python2.X

##Ejemplo de iterator

delUnoAlCinco = [1,2,3,4,5]
it = iter(delUnoAlCinco)
print it 


# print l2
# print mult_3_5(6)
# print factorialHOF(6)
# print factorialReduce(6)
# print sum(naturales)
