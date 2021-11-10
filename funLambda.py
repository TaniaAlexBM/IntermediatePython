# FUNCIONES LAMBDA
# funciones anónimas
# lambda argumento: expresión
# todo en una línea de código

palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))
# una variable va a guardar lo que la función retorna


# FUNCIÓN DE ORDEN SUPERIOR
# Función que recibe como parámetro otra función
# filter, map y reduce

# FILTER
myList = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x:x%2 !=0, myList))
print(odd)

# MAP
myList1 = [1,2,3,4,5]
cuad = list(map(lambda x:x**2, myList1))
print(cuad)

# REDUCE
from functools import reduce
myList2 = [2,2,2,2,2]
pot = reduce(lambda a,b:a*b,myList2)
print(pot)