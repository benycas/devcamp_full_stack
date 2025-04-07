# Cree un bucle For de Python.
for i in range(1, 11):
    print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(a, b, c):
    return a + b + c
print(suma(3, 4, 5))  # 12

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_lambda = lambda a, b, c: a + b + c
print(suma_lambda(3, 4, 5))  # 12

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'
lista_nombre = ('Jessica', 'Paul', 'George', 'Henry', 'Adán')

if nombre in lista_nombre:
    print(f"{nombre} coincide con un valor de la lista.")
else:
    print(f"{nombre} no coincide con un valor de la lista.")