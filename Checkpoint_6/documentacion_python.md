# Conceptos de Python 

En este documento se explicarán conceptos clave de la programación en Python añadiendo ejemplos sencillos para comprender su aplicación en proyectos reales. 

## ¿Para qué usamos Clases en Python?

El propósito principal de las **Clases** en Python es actuar como plantillas o modelos que permiten crear objetos que agrupan datos y comportamientos relacionados dentro de una sola estructura. Al definir una clase nueva, se crea un nuevo tipo de **objeto** del cual se pueden generar múltiples instancias. Cada una de estas instancias puede tener atributos propios para mantener su estado, así como métodos que permiten modificarlo, definidos dentro de la clase. En comparación con otros lenguajes de programación, Python implementa el sistema de clases con una sintaxis y semántica bastante sencilla. Las clases en Python incluyen todas las características típicas de la programación orientada a objetos: permiten herencia múltiple, las subclases pueden redefinir métodos heredados y también pueden invocar explícitamente métodos de sus clases base. Los objetos pueden contener cualquier tipo y cantidad de datos. Además, al igual que los módulos, las clases en Python se definen en tiempo de ejecución y es posible modificarlas posteriormente. 

En Python los atributos y métodos de una clase son públicos por defecto (aunque existe la posibilidad de definir variables privadas). Todos los métodos funcionan como si fueran virtuales. No existe una forma abreviada para acceder a los atributos del objeto desde sus métodos: siempre se debe pasar una referencia al propio objeto (``self``). Las clases también son objetos, lo que permite manipularlas dinámicamente, importar o cambiar sus nombres. En Python es posible ampliar los tipos incorporados usando herencia. Los operadores estándar (como los aritméticos o de indexación) pueden redefinirse para adaptarlos al comportamiento de los objetos creados por el usuario.

### Ventajas de usar clases en Python

- La agrupación permite combinar datos y funciones relacionadas en una sola unidad (la clase). También, facilita el control sobre el acceso y la manipulación de atributos mediante modificadores de acceso (públicos, privados, protegidos).

- La herencia facilita la creación de nuevas clases basadas en otras existentes y, también, reduce la redundancia al permitir que las subclases reutilicen lógica de las clases base.

- El polimorfismo habilita que diferentes objetos puedan usar la misma interfaz o método de manera única según su tipo. Promueve la flexibilidad del código al permitir trabajar con objetos de distintas clases de manera uniforme.

- Gracias a la modularidad y mantenibilidad el código se estructura en módulos organizados, fáciles de entender y modificar. Permite extender funcionalidades sin afectar otras partes del código.

### Sintaxis:

Para crear una clase en Python, se utiliza la palabra clave ``class``, seguida del nombre de la clase con la primera letra en mayúscula, ya que esa es la convención habitual,  y dos puntos ``:``. 

```python
class MiClase:
```

## ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Las clases suelen incluir un método llamado ``__init__()``, también conocido como *constructor*. Este método, que comienza y termina con dos guiones bajos, se encarga de inicializar o establecer los valores iniciales de los atributos de la clase. 

El parámetro `self` se utiliza para referenciar la nueva instancia. Los atributos se denominan atributos de instancia, ya que pertenecen exclusivamente a cada objeto creado a partir de la clase. El nombre del atributo se utiliza para asignar propiedades únicas a cada instancia. Cada clase puede definir múltiples atributos de instancia, lo que permite una creación de objetos flexible.

### Sintaxis:

```python
class MiClase:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
```

#### Ejemplo:
```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacion(self):
        return f"{self.titulo} de {self.autor}"

libro = Libro('Nacidos de la bruma', 'Brandon Sanderson')
print(libro.informacion()) # Nacidos de la bruma de Brandon Sanderson
```

## ¿Cuáles son los tres verbos de API?

Una API actúa como un intermediario que permite la comunicación entre distintos programas, definiendo normas y mecanismos para el intercambio de información y funcionalidades de manera estructurada y eficiente. Los tres verbos principales son **GET**, **POST** y **PUT**.

- **GET**: Se utiliza para recuperar información de un servidor. Es un método seguro porque no altera los datos en el servidor, solo los consulta.
- **POST**: Sirve para enviar datos al servidor, ya sea para crear nuevos registros o procesar información. 
- **PUT**: Se usa para actualizar un recurso existente o crearlo si no existe en la ubicación especificada. 

Otro verbo muy utilizado es **DELETE**, que se utiliza para eliminar recursos específicos en el servidor.

![Verbos API](/verbos_api.png)

Para conocer mejor cómo funcionan estos verbos, a continuación se creará una aplicación para gestionar un catálogo de libros almacenados en una base de datos SQLite. Permite realizar operaciones como la creación, lectura, actualización y eliminación de libros a través de diferentes rutas HTTP.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Se inicializa la aplicación Flask y la base de datos

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Se define el modelo de datos para la tabla "libros"

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), unique=False)
    autor = db.Column(db.String(100), unique=False)

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Se define el esquema de serialización para la tabla "libros"

class LibroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Libro
        load_instance = True

libro_schema = LibroSchema()
libros_schema = LibroSchema(many=True)

# Cómo crear un nuevo libro

@app.route('/libro', methods=['POST'])
def add_libro():
    titulo = request.json['titulo']
    autor = request.json['autor']
    nuevo_libro = Libro(titulo, autor)
    db.session.add(nuevo_libro)
    db.session.commit()

    libro = Libro.query.get(nuevo_libro.id)

    return libro_schema.jsonify(nuevo_libro)

# Cómo obtener todos los libros

@app.route('/libros', methods=['GET'])
def get_libros():
    all_libros = Libro.query.all()
    return jsonify(libros_schema.dump(all_libros))

# Cómo obtener un libro por id

@app.route('/libro/<id>', methods=['GET'])
def get_libro(id):
    libro = Libro.query.get(id)
    return libro_schema.jsonify(libro)

# Cómo actualizar un libro

@app.route('/libro/<id>', methods=['PUT'])
def update_libro(id):
    libro = Libro.query.get(id)
    libro.titulo = request.json['titulo']
    libro.autor = request.json['autor']
    db.session.commit()
    return libro_schema.jsonify(libro)

# Cómo eliminar un libro

@app.route('/libro/<id>', methods=['DELETE'])
def delete_libro(id):
    libro = Libro.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return "El libro ha sido eliminado"

# Se ejecuta la aplicación

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## ¿Es MongoDB una base de datos SQL o NoSQL?

![Logo MongoDB](/mongodb1.jpg)

MongoDB es una base de datos **NoSQL** orientada a documentos que destaca por su flexibilidad, escalabilidad y rendimiento. A diferencia de las bases de datos relacionales (SQL), que organizan la información en tablas estructuradas con filas y columnas, MongoDB almacena datos en documentos similares a JSON. Esto permite que los campos varíen entre documentos y que la estructura de datos evolucione con el tiempo sin necesidad de esquemas rígidos.

Cada registro en MongoDB es un documento, una estructura de datos compuesta por pares clave-valor que se asemeja a los objetos JSON. Sin embargo, internamente MongoDB usa BSON (Binary JSON), que conserva las ventajas de JSON, como la anidación, los arrays y los objetos, pero añade tipos binarios y control de longitud para mejorar el almacenamiento y la lectura. Las bases de datos en MongoDB se organizan en colecciones, equivalentes a las tablas en bases de datos SQL pero sin restricciones de esquema. Esta característica permite una gran flexibilidad en la gestión de la información.

### Ventajas:

- Alta disponibilidad gracias a la replicación y respaldo integrados.
- Escalabilidad horizontal mediante la fragmentación nativa.
- Seguridad robusta con validación de documentos y exploración de esquemas mediante Compass.
- Consultas avanzadas con indexación y agregación en tiempo real.
- Automatización y monitorización a través de herramientas especializadas.

### Ejemplo:

```json
  {
    "titulo": "Nacidos de la bruma",
    "autor": "Brandon Sanderson",
    "año": 2006
  }
```

## ¿Qué es una API?

Una API (Application Programming Interface) es un conjunto de herramientas que permite a distintos sistemas comunicarse entre sí y compartir funcionalidades. Es decir, actúa como un enlace entre aplicaciones, facilitando el intercambio de datos y la automatización de procesos.
Las APIs pueden desarrollarse en varios lenguajes de programación y siguen estándares para garantizar su correcta integración. Para que su implementación sea efectiva, es fundamental que cuenten con una documentación clara y detallada.

En el ámbito de las APIs web, existe un enfoque llamado REST (Representational State Transfer), que establece principios para diseñar interfaces bien estructuradas, optimizando la interacción entre servicios. Gracias a estos mecanismos, las APIs han revolucionado la manera en que las aplicaciones interactúan, posibilitando la creación de nuevas funcionalidades de forma eficiente y escalable.

![API REST](/api1.png)

Las API se suelen utilizar para automatizar tareas repetitivas mediante scripts que acceden a datos o servicios externos. También permiten a desarrolladores acceder a funcionalidades de un sistema sin necesidad de conocer su implementación interna.

Existen distintos tipos de API. Las API abiertas o públicas están disponibles pata cualquier desarrollador. Las API privadas son de uso interno dentro de una empresa. Las API de socios se comparten con socios específicos. Por último, las API web, son accesibles a través de protocolos como HTTP. 

### Protocolos API:

Los protocolos de API son esenciales para establecer una forma común de comunicación entre diferentes servicios web. Gracias a ellos, es posible acceder a funcionalidades de distintos sistemas, sin importar el lenguaje de programación o sistema operativo utilizado.

- **Remote Procedure Call (RPC)**: este protocolo permite que una aplicación (cliente) invoque funciones o procedimientos que se ejecutan en otra máquina (servidor), como si fueran locales. RPC facilita la interacción entre sistemas distribuidos, siguiendo una lógica cliente-servidor donde uno solicita y el otro responde con los datos requeridos.
  
- **Service Object Access Protocol (SOAP)**: es un protocolo basado en XML diseñado para intercambiar información estructurada en entornos distribuidos. Define reglas claras para la sintaxis de los mensajes entre aplicaciones, y puede utilizar protocolos de transporte como HTTP o SMTP para enviar y recibir datos. Aunque más complejo que otras opciones, SOAP es muy robusto y se utiliza en sistemas que requieren alta seguridad y estandarización.

- **Representational State Transfer (REST)**: más que un protocolo, REST es un estilo arquitectónico para diseñar servicios web. Opera sobre HTTP y se basa en el uso de recursos identificados por URLs, permitiendo operaciones estándar como GET, POST, PUT y DELETE. REST es una alternativa más simple y flexible a SOAP, ideal para desarrollos ágiles y escalables.

- **GraphQL**: es un lenguaje de consulta para APIs que permite al cliente especificar exactamente qué datos necesita. Esto reduce el tráfico de red y mejora la eficiencia, especialmente en aplicaciones móviles. También permite combinar información de varias fuentes en una sola solicitud.

### Ventajas:
- Permite construir software en componentes reutilizables.
- Facilita ampliar o modificar un sistema sin afectar todo el conjunto.
- Solo expone funciones necesarias, protegiendo el resto del sistema.
- Permite que aplicaciones escritas en distintos lenguajes trabajen juntas.

## ¿Qué es Postman?

![Logo Postman](postman1.png)

Postman es una herramienta que utilizan los desarrolladores que trabajan con APIs, que permite diseñarlas, probarlas y gestionarlas de manera ágil y ordenada. Tiene una interfaz clara y fácil de usar, donde los usuarios pueden enviar solicitudes HTTP a diferentes APIs, comprobando así su funcionamiento de forma rápida y precisa.

Una de sus funcionalidades más destacadas es la organización de solicitudes en Collections, que actúan como carpetas jerárquicas donde se agrupan peticiones relacionadas. Esto facilita la reutilización y mantiene una estructura lógica en los proyectos. Además, Postman ofrece repositorios colaborativos, donde los equipos pueden integrar recursos y herramientas para mejorar la gestión conjunta de APIs.

La plataforma abarca todo el ciclo de vida de una API, desde la etapa de diseño hasta su supervisión continua. Entre sus principales características se incluyen:
- Pruebas automatizadas, útiles para validar comportamientos y detectar errores de forma anticipada.
- Gestión de entornos, que permite configurar distintos escenarios según el contexto de desarrollo, prueba o producción.
- Documentación automática, generada a partir de las solicitudes y respuestas, lo que agiliza la creación de documentación técnica.
- Espacios de trabajo colaborativos, que fomentan el trabajo en equipo y la centralización de recursos del proyecto.

Postman se integra con herramientas clave en el proceso de desarrollo, como GitHub, facilitando la administración de versiones, documentación y pruebas automatizadas. También es compatible con múltiples protocolos web, incluyendo HTTP, HTTPS, REST, SOAP y GraphQL, lo que lo convierte en una solución flexible para diversas necesidades de desarrollo.

### Ventajas:

- Interfaz gráfica intuitiva y personalizable.
- Soporte para múltiples métodos HTTP (GET, POST, PUT, DELETE, etc.).
- Amplia comunidad de usuarios con recursos y documentación disponible.
- Posibilidad de agregar scripts personalizados en JavaScript para automatizar tareas avanzadas.

![Interfaz Postman](/postman2.png)

## ¿Qué es el polimorfismo?

El polimorfismo es uno de los principios fundamentales en la programación orientada a objetos, y su presencia en lenguajes como Python permite escribir código más flexible, reutilizable y extensible. El polimorfismo se refiere a la capacidad de un objeto de una clase concreta de ser tratado como una instancia de una clase común, siempre y cuando comparta una interfaz definida, es decir, un conjunto de métodos públicos.

Una de sus principales ventajas es que permite a una función operar con objetos de diferentes clases, siempre que estos implementen los métodos adecuados. De este modo, se evita la duplicación de código y se fomenta el desarrollo de sistemas más genéricos. Gracias a este mecanismo, los desarrolladores pueden definir una función "genérica" que interactúe con distintos tipos de objetos sin necesidad de escribir una implementación específica para cada uno.

El polimorfismo permite que una clase principal pueda tener múltiples clases anidadas con distintos comportamientos, logrando así una estructura flexible sin comprometer la coherencia del código. Por ejemplo, si se diseña una función que trabaja con distintos objetos con atributos similares, el polimorfismo evita la necesidad de crear funciones específicas para cada tipo de objeto.

### Ejemplo:

En el siguiente ejemplo, ``Suma`` y ``Multiplicacion`` tienen el mismo método ``calcular(a, b)``, pero cada clase implementa una operación diferente. La función ``operar()`` usa polimorfismo para trabajar con distintas clases sin necesidad de saber qué tipo de operación está ejecutando.

```python
class Suma:
    def calcular(self, a, b):
        return a + b

class Multiplicacion:
    def calcular(self, a, b):
        return a * b

# Polimorfismo
def operar(operacion, a, b):
    print(operacion.calcular(a, b))

suma = Suma()
multiplicacion = Multiplicacion()

operar(suma, 5, 3)          # 8
operar(multiplicacion, 5, 3) # 15
```

## ¿Qué es un método dunder?

Los métodos Dunder (del inglés double underscore), o métodos mágicos, son funciones especiales que forman la base del modelo de datos de Python y permiten que las clases creadas por el usuario trabajen con las funciones básicas del lenguaje. Estos métodos, que se identifican por sus dos barras bajas al inicio y al final de su nombre, son fundamentales para controlar el comportamiento de los objetos en distintas situaciones. 

Los métodos Dunder ``__str__``, ``__init__`` y ``__repr__`` son esenciales para la correcta inicialización y representación de los objetos en Python. 

- `__init__`: es el constructor de una clase en Python. Se ejecuta automáticamente cuando se crea una nueva instancia, permitiendo la inicialización de atributos.

- `__str__`: define la representación de un objeto mediante una cadena legible. Ofrece una salida clara y bien presentada con los valores y detalles de nuestra clase.

- `__repr__`: es muy similar a ``__str__``, pero  ``__repr__`` suele utilizarse más para una salida en bruto, por lo que generalmente no se formatea de manera elegante. Es útil, por ejemplo, para registrar información en logs o reportes de errores.

### Ejemplo:
En el ejemplo que se muestra a continuación, ``__init__`` inicializa el objeto con nombre y edad, ``__str__`` define cómo se muestra al imprimirlo, y ``__repr__`` da una representación más técnica y útil para desarrolladores.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

persona1 = Persona('Beñat', 32)

print(str(persona1))   # Beñat tiene 32 años
print(repr(persona1))  # Persona('Beñat', 32)
```

## ¿Qué es un decorador de python?

Un decorador es un patrón de diseño en Python que permite al usuario añadir nuevas funciones a un objeto existente sin modificar su estructura. Los decoradores suelen aplicarse a las funciones, y desempeñan un papel clave a la hora de mejorar o modificar el comportamiento de las funciones

### Ejemplo:

En el ejemplo que se muestra a continuación, ``@property`` convierte los métodos nombre y edad en atributos de solo lectura, y ``@nombre.setter`` permite modificar el valor de nombre de forma controlada. Estos decoradores permiten acceder y modificar atributos privados como si fueran públicos, pero manteniendo la encapsulación.

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre 
        self._edad = edad

    def descripcion(self):
        return f"{self._nombre} tiene {self._edad} años"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

persona1 = Persona('Beñat', 32)

print(persona1.nombre)  # Beñat
persona1.nombre = 'Aitor'
print(persona1.nombre)  # Aitor
print(persona1.descripcion())  # Aitor tiene 32 años
```







