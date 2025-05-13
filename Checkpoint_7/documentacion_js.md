# Documentación JavaScript

## ¿Qué diferencia a Javascript de cualquier otro lenguaje de programación?

JavaScript se diferencia de otros lenguajes de programación por varias razones:

- La diferencia principal es que es el único lenguaje que los navegadores web entienden de forma nativa, lo que permite ejecutar código en el propio navegador sin necesidad de instalaciones adicionales. 
- Es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de las variables de antemano y que este puede cambiar en tiempo de ejecución. Esta flexibilidad acelera el desarrollo.
- Tiene un modelo de ejecución asíncrono basado en el event loop. Esto permite que el manejo de eventos, operaciones de entrada/salida o interacciones en tiempo real se realice sin bloquear la ejecución del programa.
- Se conecta de una manera muy sencilla con otros programas o APIs. 
- Tiene un sistema de herencia basado en prototipos. Esto quiere decir que permite que los objetos hereden directamente de otros objetos modelo. Esto hace que las estructuras sean más dinámicas y adaptables. 

## ¿Cuáles son algunos tipos de datos JS?

Estos son los principales tipos de datos:

- Número:
  
```js
const edad = 32; // Entero
const númeroPi = 3.14; // Decimal
```
- BigInt: 

Representa números enteros con precisión arbitraria. 

```js
const bigInt = 268412394578214425n;
const x = 2n ** 53n; // 9007199254740992n
```

- String/Cadena:

Se utiliza para representar datos textuales. 
```js
const nombre = 'Beñat';
const saludo = 'Hola mundo!';
```

- Boolean: 

Representa una entidad lógica y puede tener dos valores: ``true`` y ``false``.
```js
const esVerdadero = true;
const esFalso = false;
```
- Símbolo:

Se utiliza para crear propiedades de objetos únicas, inmutables.

```js
const simbolo = Symbol('id')
```
- Indefinido: 

Es una variable a la que no se le ha asignado un valor. 

```js
let noDefinido;
console.log(noDefinido); // undefined
```
- Nulo:
```js
const nulo = null;
console.log(nulo); // null
```

En JavaScript, si queremos saber de qué tipo es el dato con el que estamos trabajando o queremos trabajar, se utiliza el código ``typeof``.

```js
typeof 'Beñat'; // string
typeof true; // boolean
```

## ¿Cuáles son las tres funciones de String en JS?

Para ver las tres funciones principales de string en JavaScript se trabajará con el siguiente ejemplo de cadena:

```js
const str = "Tres tristes tigres tragan trigo en un trigal";
```

- ``concat()``:

Se utiliza para concatenar dos o más cadenas.

```js
str.concat("tres veces al trimestre"); // "Tres tristes tigres tragan trigo en un trigal tres veces al trimestre"
```
- ``replace()``:

Se utiliza para reemplazar una parte de texto de una cadena con otro texto. Sirve para corregir textos o transformar formatos de texto. 

```js
str.replace("tragan", "comen"); // "Tres tristes tigres comen trigo en un trigal"
```

- ``slice()``:
Se utiliza para extraer una parte de una cadena a partir de los índices.

```js
str.slice(10); // "tigres tragan trigo en un trigal"
```
Otras funciones interesantes pueden ser ``includes()``, ``startsWith()`` o ``endsWith()``, que se utilizan para comprobar si una cadena contiene, empieza o termina con una subcadena concreta. 

```js
str.includes("leones"); // false
str.startsWith("Tres"); // true
```

## ¿Qué es un condicional?

Un condicional es una estructura que permite ejecutar diferentes bloques de código dependiendo de si una condición se considera verdadera (``true``) o falsa (``false``).

### Tipos de condicionales en JavaScript

1. ``if``:

Se utiliza para ejecutar una instrucción o un bloque de código solo si una condición se cumple, es decir, si es verdadera. Si la condición no se cumple, o es falsa, el código no se ejecuta. 

- Sintaxis:
```js
if (condición1); {
  // instrucción si la condición1 es verdadera
}
```
- Ejemplo:
```js
const edad = 20

if (edad >= 18); {
  console.log("Puedes conducir un coche.");
}
```

En este ejemplo, tenemos que si la edad es mayor o igual que 18, en pantalla se verá el siguinte mensaje: ``"Puedes conducir un coche."``. En este caso al ser la edad 20 años, nos saldrá ese mensaje.

2. ``else if``:

Se utiliza después de un ``if`` para evaluar una condición adicional si la anterior no se cumple. Se pueden añadir todas las condiciones que se deseen. 

- Sintaxis:
```js
if (condición1); {
  // instrucción si la condición1 es verdadera
} else if (condición2); {
  // instrucción si la condición1 es falsa y la condición2 es verdadera
}
```
- Ejemplo:
```js
const temperatura = 26

if (temperatura < 15); {
  console.log("Hace frío.");
} else if (temperatura < 25); {
    console.log("Se está bien.");
}
```

En este caso, si la temperatura es menor que 15 nos saldrá un mensaje que dice: ``"Hace frío."``, mientras que si es menor que 25 nos saldrá este otro mensaje: ``"Se está bien."``.

3. ``else``:

Se utiliza al final de una cadena de condiciones para ejecutar una instrucción o un bloque de código cuando ninguna condición anterior se cumple. Permite dar una alternativa si una condición no se cumple. 

- Sintaxis:
```js
if (condición1); {
  // instrucción si la condición1 es verdadera
} else {
  // instrucción si la condición1 es falsa
}
```
- Ejemplo:
```js
const temperatura = 26

if (temperatura < 15); {
  console.log("Hace frío.");
} else if (temperatura < 25); {
    console.log("Se está bien.");
} else {
    console.log("Hace calor.");
}
```

Siguiendo el ejemplo anterior, vemos que en este caso se añade que si la temperatura no es ni menor que 15 ni 25 grados saldrá un mensaje que dice: ``"Hace calor."``.

## ¿Qué es un operador ternario?

Un operador ternario es una forma corta de escribir una estructura condicional simple, parecido a un ``if/else``. Permite escribir el código en una sola línea. Se divide en tres partes. Primero, se evalúa la condición. Después, si la condición es verdadera (``true``), se ejecuta la primera instrucción. Y, si la condición es falsa (``false``), se ejecuta la segunda instrucción.

- Sintaxis:

```js
condición ? instrucción_si_verdadero : instrucción_si_falso;
```

- Ejemplo:

```js
const edad = 17;
const conducir = edad >= 18 ? "Puedes conducir un coche." : "NO puedes conducir un coche.";
console.log(conducir); // "NO puedes conducir un coche."
```

Si utilizaramos ``if/else``, el código sería el siguiente:

```js
const edad = 17;
let conducir;

if (edad >= 18) {
  conducir = "Puedes conducir un coche.";
} else {
  conducir = "NO puedes conducir un coche.";
}

console.log(conducir); // "NO puedes conducir un coche."
```

Este método permite anidar ternarios. Sin embargo, queda más claro si se utiliza ``if/else`` en este caso.

## ¿Cuál es la diferencia entre una declaración de función y una expresión de función?

La declaración de una función y la expresión de una función son dos maneras distintas de crear o definir funciones. Sin embargo, ambas se comportan de una manera diferente y tienen características distintas. 

A continuación se muestra cómo funcionan:

### Declaración de función:

#### Características:
   
- La declaración empieza con la palabra ``function``, y después se define el nombre de la función.
  
- Siempre se le debe dar un nombre a la función. Es **obligatorio**.

- **Hoisting:** Las declaraciones de función se cargan por completo al comienzo del ámbito donde se definen, lo que permite invocarlas incluso antes de que aparezcanen el código.

#### Sintaxis:

```js
function nombreFuncion() {
    return expresión;
}
```

#### Ejemplos:

```js
function saludo() {
    return 'Kaixo';
}
```

En el siguiente ejemplo se muestra cómo funciona el hoisting:

```js
console.log(saludo("Beñat")); // Kaixo Beñat!

function saludo(nombre) {
    return 'Kaixo ${nombre}!';
}
```

### Expresión de función:

#### Características:

- Hay dos tipos de expresiones: anónima o con nombre.

- La función se guarda en una variable o constante.

- El hoisting no es completo. Solo se eleva la variable (``var``) o la constante (``let/const``); la definición de la función no. No se puede llamar a la función antes de la expresión.

#### Sintaxis:

```js
// Expresión anónima:

const nombre = function () {
  return expresión;
};

// Expresión nombrada:

const nombre = function nombreFuncion() {
  return expresión;
};
```

#### Ejemplos:

```js
// Expresión anónima:

const restar = function (a,b) {
  return a - b;
};

// Expresión nombrada:

const restar = function resta(a,b) {
  return a - b;
};
```

### ¿Cuándo utilizarlas?

Las declaraciones de función se utilizan más cuando queremos que la función esté disponible en todo el ámbito desde el inicio y también cuando queremos un código más legible. Las expresiones de función, en cambio, se utiliza más cuando necesitamos una función anónima. 

## ¿Qué es la palabra clave "this" en JS?

En JavaScript, ``this`` es una palabra clave que apunta al objeto asociado al contexto de ejecución en el momento de la llamada. Su valor se define según cómo se invoca la función, no por dónde fue creada. Existen varios patrones de vinculación de ``this`` que determinan su comportamiento en distintos contextos. A continuación, se explican los diferentes patrones de vinculación:

### 1. Vinculación implícita Implicit Binding:

Lo que está a la izquierda del punto en la llamada determina el valor de ``this``.

````js
const persona = {
  nombre: "Beñat",
  saludo() {
    console.log(`Kaixo, soy ${this.nombre}.`);
  }
};

persona.saludo(); // Kaixo, soy Beñat.
````

### 2. Vinculación explícita o Explicit Binding:

Se utilizan los métodos ``.call()``, ``.apply()`` o ``.bind()`` para forzar manualmente el valor de ``this``.

````js
function saludo() {
  console.log(`Kaixo, soy ${this.nombre}.`);
}

const user = { nombre: "Beñat" };

saludo.call(user);  // Kaixo, soy Beñat.
saludo.apply(user); // Hola, soy Beñat.

const saludoUser = saludo.bind(user);
saludoUser(); // Kaixo, soy Beñat.
````
### 3. Vinculación por new o New Binding:

En este caso se utiliza ``new`` para crear una instancia a partir de una función constructora, y ``this`` se vincula al nuevo objeto creado.

````js
function User(nombre) {
  this.nombre = nombre;
  console.log(this.nombre);
}

const Beñat = new User("Beñat");
````

### 4. Vinculación por contexto léxico o Lexical Binding:

En este caso las funciones no tienen su propio ``this``. Sin embargo, heredan el ``this`` del ámbito donde fueron definidas. 

````js
const User = {
    name: "Beñat",
    saludo: function() {
        setTimeout(() => {
            console.log(`Kaixo, soy ${this.name}.`);
        }, 1000);
    }
};

User.saludo(); // Kaixo, soy Beñat.
````

### 5. Vinculación predeterminada o Default Binding:

Si una función se ejecuta por sí sola, sin un contexto específico, ``this`` será el objeto global. En modo estricto (cuando ``"use strict"`` está activado) ``this`` dentro de una función independiente es ``undefined``. Este comportamiento hace que JavaScript sea más predecible y previene errores accidentales al acceder a ``this`` en funciones globales.

````js
// Modo no estricto:

function mostrarThis() {
  console.log(this);
}

mostrarThis();  // Window (en un navegador)

// Modo estricto:

"use strict";

function mostrarThis() {
  console.log(this);
}

mostrarThis();  // undefined
````