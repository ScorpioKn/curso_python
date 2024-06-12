# funciones
matematicamente una funcion es una ioperacion que toma uno o mas valores llamados a `argumentos` y produce un valor denominado `resultado`
# FUNCIONES
matematicamente una funcion es una operacion 
que toma uno om mas valores llamados `argumentos`
y produce un valor denominado resultado.
f(x)=x/1+x**2
>[!NOTE]
>todos los lenguajes de programacion tienen 
funciones incorporadas (funciones internas), y funciones creadas por el usuario (fuciones externas)
en programacion una funcion es un subprograma, es una estrutura que nos permite agrupar codigo y sus principales objetivos son 
-`no repetir` fragmetos de codigos 
-`reutilizar` el codigo en distitos esenarios 
## estrutura de una funcion
una funcion viene `definida` por un `nombre`, k sus `parametros` y su valor de `retorno`.
una vez creada la funcion podemos solcitar su ejecucion 'invocado' la funcion por su 'nombre'
## definir una funcion en python
para definir una funcion en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. a continuacion especificaremos los `parametros` con `(si)` es una funcion sin parametros `(a)` si es una funcion con parametros, si se tuviera mas de un parametro iran separados por `,`, finalizremos con linea `:`, en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente devera `retornar` un resultado con la palabra reservada `return`.
[!tip]
como retorno tambien se puede utilizar la `funcion interna`, `print`, para depuracion de codigo no es recomendable usarlo en produccion.
**ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    reurn f"{saludo}, {saludo_dos}"
    #print(f"{saludo}, {saludo_dos}")
print(saludo())
```
### invocar una funcion
para invocar una funcion solom tendremos que escribir el `nombre` de la funcion seguido `()` parentesis.
```python
def saludo():
    print("hola")

#invocando la funcion
saludo()
```
## retornar un valor
las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
> [!WARNING]
> no confundir `print()` con `return`,. el valor retornado por `return` nos permite usarlo fuera de su contexto. y `print` solo mostrara el literal por terminal.
**ejemplo**
*en el archivo `lecture.py`
## retornando multiples valores
el secreto es necesario hacerlo mediante un tipo de
```python
def varios():
    return 2,3,4
varios()
#retona(2,3,4)
def lista():
    return["hola",45]
#retona["hola",45]
def dicc():
    return("nombre","jose","edad":45)
dicc()
#retona ("nombre","jose","edad":45)
```
## parametros y argumentos
si una funcion no dispuciera de valores de entrada estaria limitada en su actuacion.
es por ello que los `parametros` nos permiten variar los datos que consumen una funcion para obtener distintos resultados
**ejemplo**
*crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)
```
cuando llamamos a una funcion con `argumentos`, los valores de estos argumentos se copian en los correspondientes `parametros` dentro de la funcion.
```python
def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)
```
### argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico si no que **se asignan por nombre a cada párametro** ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros de la funcion. 
para utilizarlo basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia}, con {num_core}, cores y con una frecuencia {frecuencia} """)
    build_cpu(num_core=4,familia="intel",frecuencia=2.7)
```
### argumentos posicionales
los argumentos son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
    la cpu es de la familia {familia}, con {num_core}, cores y con una frecuencia {frecuencia} 
    """)
#haciendo uso de argumentos posicionales
build_cpu("intel",4,2.7)
```
### parametros por defecto
es posible especificar **valores por defecto** en los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.
**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","cruces","desaprobados")
```
## desempaquetado/empaquetado de argumentos/posicionales nominales
son técnicas en Python que permiten trabajar con un número variable de argumentos en funciones.

- Empaquetar argumentos posicionales: 
**ejemplo**
 
```python
def sumar(*numeros):
    total = sum(numeros)
    return total

resultado = sumar(1, 2, 3, 4)
```
 
 
- Empaquetar argumentos nominales

**ejemplo** 
 
 ```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="María", edad=30, ciudad="Lima")
```
 

 
 
- Desempaquetar argumentos nominales: 
Ejemplo:
 
```python
info = {"nombre": "Juan", "edad": 25}
mostrar_info(info)
```

## funciones internas de python(tarea)
En Python, las funciones internas (también conocidas como funciones anidadas) son funciones definidas dentro de otra función. Estas funciones internas pueden acceder a las variables locales de la función externa en la que están definidas. Aquí te muestro un ejemplo de cómo definir y utilizar funciones internas en Python:
**ejemplo**
```python
def calcular_cuadrado(numero):
    def cuadrado(num):
        return num ** 2
    
    resultado = cuadrado(numero)
    return resultado

numero = 5
resultado_cuadrado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {resultado_cuadrado}")
```