# Conceptos básicos de Python 

A continuación explicaré varios conceptos clave en Python. Primeró definiré el concepto y la sintaxis, y después aportaré ejemplos sencillos. 

## ¿Qué es un condicional?

Un condicional en Python permite ejecutar diferentes bloques de código dependiendo de si una condición es verdadera (`True`) o falsa (`False`). Se suele utilizar principalmente con las palabras clave  `if` y `else`, y puede complementarse con `elif`.

Para usar correctamente los condicionales se recomienda:
+ Explicar los condicionales más difíciles con comentarios, para que otras personas puedan entenderlo.
+ Escribir siempre de la manera más sencilla posible. Por ejemplo, usando `and` cuando se pueda, en lugar de varios `if`.
+ Utilizar paréntesis cuando se combinan distintos condicionales y operadores.
+ Chequear siempre que se hayan escrito los dos puntos `:`.



#### Sintaxis:
```python
if una_condicion:
    # Ejecuta el código si la condición es verdadera
elif otra_condicion:
    # Ejecuta el código si la otra condición es verdadera
else:
    # Ejecuta el código si las condiciones anteriores son falsas
```

#### Ejemplo:
```python
temperatura = 20

if temperatura >= 30:
    print("Hace calor.")
elif temperatura >= 15:
    print("Se está bien.")
else:
    print("Hace frío.")

# Como la temperatura es de 20 grados, el código mostrará: 
    Se está bien.
```

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles en Python permiten repetir un bloque de código dos o más veces. Son claves para reducir la redundancia en el código y mejorar la eficiencia, ya que automatizan la ejecución repetitiva de instrucciones sin necesidad de escribirlas muchas veces. En los bucles, la ejecución ocurre cuando la condición establecida es verdadera. Si la condición es falsa, el bucle no se ejecuta; en cambio, si es verdadera, el código se repite e itera un número determinado de veces, hasta que la condición declarada en el código sea falsa. 

Python tiene dos tipos de bucle principales:

###  Bucles `for` 
Utilizan iteradores para recorrer todos los elementos de objetos iterables, como listas, tuplas y cadenas. Permiten ejecutar un fragmento de código de forma repetitiva según la cantidad de elementos presentes en el iterable.

#### Sintaxis:

```python
for elemento in iterable:
    # Bloque de código
```

#### Ejemplo:
```python
for num in range(5):
    print(num)  

# Imprime 0, 1, 2, 3, 4
```

### Bucles `while` 

Ejecutan los bloques de código correspondientes mientras la condición del bucle sea verdadera. El bucle `while` continuará repitiéndose hasta que la condición se haya cumplido un número específico de veces.

#### Sintaxis:

```python
while condición:
    # Bloque de código
```

#### Ejemplo:

```python
num = 1
while num < 5:
    print(num)
    num += 1

# Imprime 1, 2, 3, 4
```

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión es una forma concisa y eficiente de crear listas en una sola línea de código en Python. Básicamente, combina lo que normalmente se haría en un bucle `for` (e incluso usando condiciones `if`) en una única expresión. Son útiles para mejorar la legibilidad y reducir la cantidad de líneas en un programa. Es un código más rápido en compración con los bucles tradicionales. Sin embargo, a veces puede ser un poco menos clara si se complica mucho.

#### Sintaxis:
```python
lista_nueva = [expresion for elemento in iterable]

lista_nueva2 = [expresión for elemento in iterable if condición]
```

#### Ejemplo:
```python
# Sin lista por comprensión
num_cuadrados = []
for num in range(1, 11):
    num_cuadrados.append(num ** 2)
print(num_cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Usando lista por comprensión
numeros = range(1,11)
cuadrados = [n**2 for n in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función cuando se llama. Estos valores se colocan entre paréntesis, justo después del nombre de la función. Se pueden enviar o añadir uno o varios argumentos, separándolos por con comas `,`. Por defecto, una función se debe llamar con el número correcto de argumentos. Es decir, si la función espera 2 argumentos, hay que llamar la función con 2 argumentos, ni más, ni menos. Si se intenta llamar la función con 1 o 3 argumentos por ejemplo, se obtendrá un error. 

Hay varios tipos de argumentos al definir y llamar funciones:

### - Argumentos por defecto

Los argumentos por defecto en Python son aquellos a los que se les asigna un valor durante la definición de la función, utilizando el operador de asignación `=`. Esto significa que, al momento de llamar a la función, estos argumentos son opcionales: si no se les proporciona un valor, usarán el valor definido por defecto. En caso de que durante la llamada a la función se proporcione un valor explícito para uno de estos argumentos, este nuevo valor sobrescribirá el valor por defecto. Una función puede tener cualquier cantidad de argumentos por defecto, pero es importante recordar que los argumentos que tienen valor por defecto deben aparecer después de los argumentos que no tienen valor por defecto. Además, los valores por defecto se evalúan una sola vez en el momento en que se define la función, lo que puede tener consecuencias si se usan objetos mutables como listas o diccionarios.

#### Ejemplo:

```python
def suma(a, b=4):
    return a + b

print(suma(3))        # 7
print(suma(3, 6))     # 9
```

### - Argumentos por palabra clave

Los argumentos por palabra clave permiten llamar a una función especificando explícitamente el nombre del parámetro seguido del valor que se le quiere asignar. Esta técnica ofrece flexibilidad, ya que no es necesario respetar el orden en que los parámetros fueron definidos dentro de la función, siempre que se indique el nombre correspondiente de cada argumento. Sin embargo, es indispensable que los nombres utilizados coincidan exactamente con los nombres de los parámetros en la definición de la función. Cuando se emplean argumentos por palabra clave, se pueden omitir los argumentos opcionales, ya que el mecanismo respeta los valores por defecto establecidos.

#### Ejemplo:

```python
def suma(a, b=4):
    return a + b

print(suma(a=3))              # 7
print(suma(b = 5, a = 4))     # 9
```
### - Argumentos posicionales

En una llamada de función utilizando argumentos posicionales, los valores se pasan respetando estrictamente el orden en que los parámetros fueron definidos en la función. Es decir, el primer argumento se asigna al primer parámetro, el segundo al segundo, y así sucesivamente. Si se combinan argumentos posicionales y argumentos por palabra clave en una misma llamada, los argumentos posicionales deben ir siempre primero, seguidos por los argumentos por palabra clave.

#### Ejemplo:

```python
def suma(a, b, c):
    return a + b + c

print(suma(4, 3, 5))         # 12
print(suma(4, c = 5, b = 3)) # 12(posicional primero, luego palabra clave)
```
### - Argumentos posicionales arbitrarios (args)

Cuando no se sabe de antemano cuántos argumentos posicionales va a recibir una función, Python permite usar argumentos posicionales arbitrarios. Para ello, se antepone un asterisco `*` al nombre del parámetro dentro de la definición de la función. Todos los argumentos adicionales que se pasen serán capturados en una tupla, lo que permite iterarlos o manipularlos de manera flexible dentro de la función. Antes del parámetro con `*`, se pueden definir uno o más argumentos normales si se desea.

#### Ejemplo:

```python
def suma(*b):
    resultado = 0
    for i in b:
        resultado += i
    return resultado

print(suma(1, 2, 3, 4, 5))  # 15
print(suma(10, 20))         # 30
```

### - Argumentos por palabra clave arbitrarios (kwargs)

Los argumentos por palabra clave arbitrarios se utilizan cuando una función necesita aceptar un número variable de argumentos que se pasan por nombre. Para ello, se anteponen dos asteriscos `**` al nombre del parámetro en la definición de la función. Todos los argumentos de este tipo serán recogidos en un diccionario, donde las claves corresponden a los nombres de los argumentos y los valores a los datos asociados. Esto permite acceder dinámicamente a todos los argumentos adicionales que se pasen durante la llamada de la función.

#### Ejemplo:

```python
def fn(**a):
    for clave, valor in a.items():
        print((clave, valor))

fn(numeros=5, colores="azul", frutas="manzana")

'''
Output:
('numeros', 5)
('colores', 'azul')
('frutas', 'manzana')

'''
```
## ¿Qué es una función Lambda en Python?

Las funciones Lambda se definen como una línea que ejecuta una sola expresión. Son utilizadas cuando se requiere realizar una operación sencilla y se prioriza la rapidez en la ejecución antes que la asignación formal de un nombre a la función. También reciben el nombre de funciones anónimas. Proporcionan una forma concisa de definir funciones pequeñas y sin nombre. Estas funciones se comportan de manera similar a las funciones tradicionales definidas con `def`, y son especialmente útiles para crear funciones breves de forma eficiente. Este tipo de funciones pueden tomar cualquier número de argumentos, pero solo pueden tener una expresión. Sin embargo, dado que solo pueden contener una única expresión, no son adecuadas para casos en los que se necesiten instrucciones de control de flujo. Estas funciones siempre tienen que estar asignadas a una variable, de lo contrario, no funcionarían.

#### Sintaxis:
```python
lambda argumentos: expresión
```

#### Ejemplo:
```python
# Función tradicional:
def suma(x,y):
    return(x + y)
print(suma(3,5))

# Función Lambda
suma = lambda a, b: a + b
print(suma(3, 5))  # 8
```


## ¿Qué es un paquete pip?

`pip` es el sistema de gestión de paquetes que se utiliza para instalar y administrar las bibliotecas externas en Python. Facilita tanto la instalación como la actualización de paquetes, garantizando que todas las dependencias necesarias se configuren correctamente y se mantengan actualizadas. Además, `pip` ofrece acceso a una amplia variedad de paquetes, lo que permite encontrar fácilmente las herramientas necesarias para cada proyecto.

### Cómo instalar un paquete:
```sh
pip install nombre_paquete

# Ejemplo:
pip install numpy
```

### Cómo usar el paquete instalado
```python
import numpy as np
```

