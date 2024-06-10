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