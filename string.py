# comentarios.

#type(variable)
#muestra el tipo de la variable

#\ para salto de línea
#\t salto tab

#si se pone una r ante de las "" o '', toma el texto completo x si hay una \c o \t dentro del texto.

#print(""" sirve para hacer salto de lineas
# sin tener que poner lo de arriba""")

#####################################################################################


#indice de cadenas

#profesor = "Michel Charnay"
#profesor[0]
#arroja M

#si se pone profesor[2:5]
#arroja che

#si se pone profesor[2:]
#arroja desde el indice 2 en adelante

#len(profesor)
#cuenta los caracteres


#arreglos

#arreglo = [1,2,3,4,5]
#arreglo, arroja el arrelgo

#arreglar elemento al arreglo
#arreglo.append(10)


#dentro de arreglo se pueden guardar más arreglos

#para leer datos por teclado:
#input()

#dato = input()

#parsear string a int
#int(variable)
#float(datos)

#para almacernar input decimal con mensajes antes:
#dato =float(input("trintroduce un valor decimal"))


#####################################################################################

#OPERADORES LOGICOS

#True
#False
#and
#or
#== 
# !=
# >
# <
# >=
# <=

#Expresiones Anidadas y operadores  de asignación

#  +=   suma por el mismo valor y da una respuesta
#  -=   resta por el mismo valor y da una respuesta
#  *=   multitplica por el mismo valor y da una respuesta
#  /=   divide por el mismo valor y da una respuesta
#  %=   mod por el mismo valor y da una respuesta}
#  **=   potencia por el mismo valor y da una respuesta



#####################################################################################

#ESTRUCTURAS DE CONTROLS

#IF

"""Hartas lineas de comentario IF
Michel = 10
if Michel == 10:
    print('Michel vale 10')
if Michel == 15:
    print('Michel vale 15')

"""



#IF ELSE

"""
Michel = 10
if Michel == 10:
    print("Michel vale 10")
else:
    print("Michel no vale 10")
"""


#ELSE IF
"""
Michel = 10
if Michel == 10:
    print('Michel vale 10')
elif Michel == 15:   
    print('Michel vale 15')
else:
    print('No cae en ningún lado')
"""


#WHILE
"""
num = 0
while num <= 3:
    num += 1
    print('Estoy iterando, van = ',num)
"""


"""
num = 0
while num <= 3:
    num += 1
    print('Estoy iterando, van = ',num)
    break
else:
    print('imprimo esto porque se acabó la iteración y es el else')
"""


#ejercicio grande de menu con while
"""
print('elige tu propio camino')
inicio = input('escribe empezar para iniciar el programa: ')
while (inicio == 'empezar'):
    print(""" ¿qué camino quieres elegir?
    Escribe la opción con número
    1 - Quiero que me saludes
    2 - Deseo multiplicar porque no se como hacerlo
    3 - Quiero salir de este programa, aprendí a como multiplicar""")
    opcion = input()
    if opcion == '1':
        print('te saludo')
    elif opcion == '2':
        numero1 = float(input('Introduce el número de multiplicar del primero: '))
        numero2 = float(input('Introduce el número de multiplicar del segundo: '))
        print('El resultado es : ', numero1*numero2)
    elif opcion == '3':
        print('Excelente desición que hayas tomado mi curso')
    else:
        print('No elegiste ningún número posible')             

"""



#####################################################################################


#FOR

"""
lista = [1,2,3,4,5,6]
indice = 0
for recorrer in lista:
    print(recorrer)
"""


#####################################################################################

#TUPLAS, DICCIONARIOS,  CONJUNTOS, PILAS Y COLAS.


#TUPLAS


#Conjuntos
"""
con = {5,4,3}
con.add(6)
con



cadena = "texto bla bla bla bla "
set(cadena)

"""


#diccionarios
"""
diccionario = {'nombre' : 'Michel', 'Profesion' : 'Ingeniero'}
type(diccionario)
diccionario['nombre']
diccionario['nombre'] = 'Antoine'
diccionario
del(diccionario['nombre']) 

"""


#PILAS
"""
apilar = [1,2,3,4]
apilar.append(3)
apilar.append(6)
apilar.append(8)
apilar.pop()
"""

#COLAS
"""
#Hay que llamar a las librerías de las colas

from collections import deque
colas = deque()

colas

type(colas)

colas = deque(['Michel', 'Estudiantes', 'Familia', 'Coockie'])

colas.pop()
colas.popleft()

"""
#las pilas no se pueden sacar primero, las colas sí.


#####################################################################################

#ENTRADAS O SALIDAS
#INPUTS OUTPUTS

#5 inputs por FOR dentro de un array

""" 
listas = []
print("Ingrese 5 números)
for i in range(5):
    listas.append(input("INgrese su número: "))

listas

"""


#OUTPUTS

""" 
nombre = "Michel"
apellido = "Charnay"

nombreCompleto = "Mi nombre es '{}' y mi apellido es '{}'".format(nombre,apellido)

"""

#####################################################################################

#FUNCIONES

#para definiar una variblae global es :  global nombreVariable

"""
def estudiantes():
    print("Este es un mensaje de algún estudiante")

estudiantes()
"""




#si tiene un return string

"""
def metodo():
    return "asdlkjasld"

print(metodo())


"""



#si tiene un return int
"""
def metodo(a,b):
    return a+b

metodo()
"""



#meter valors dentro del método

"""
def estudiantes(valor):
    return valor*3

variable = 15
variable = estudiantes(variable)
variable
"""



#meter muchos argumentos y recorrerlos todos

"""
def metodo(*elemento):
   for elementos in eleneto:
       print(elementos)

metodo('Michel', 'Charnay', 'computadres', 10, [1,2,3])
"""

#meter diccionario y recorrerlo
"""
def nombre_diccionario(*cantidad, **elemento):
    b = 0
    for cantidades in cantidad:
        b+=cantidades
    print(b)
    for x in elemento:
        print(x, " ", lo[x])


nombre_diccionario(1,2,3,4,michel="charnay", Estudiantes='Genios',calificaciones=[7,8,9])
"""

#FUNCIONES RECURSIVAS

#SOn las funciones que se llaman a si misma

"""
def metodo(segundos):
    segundos -= 1
    if segundo >= 0:
        print(segundos)
        metodo(segundos)
    else:
        print('terminó la cuenta atrás')

metodo(10)    


"""





#####################################################################################

#ERRORES Y EXCEPCIONES EN PYTHON

#se hacen con try

"""
try:
    variable = float(input("Introduce un número: "))
    a = 2
    print("resultado: ", a*variable)
except:    
    print("Ingresaste cualquier otra cosa menos la que se pidio")

"""



#otro ejemplo
"""
while(True):
    try:
        variable = float(input("Introduce un número: "))
        a = 2
        print("resultado: ",a*variable)
    except:
        print("Ingresaste mal, otra oportunidad)
    else:
        print("Bine iniciado  :)")
        break
    finally:
        print("Perfecto amigo, terminó todo bien.")     

"""




#####################################################################################

#INVOCACIÖN DE EXCEPCIONES

"""
try:
    a = input("Número :")
    10/a
except Exception as x:
    print( type(x).__name__)

"""


#error traducido

"""
try:
    a = float(input("Numero :  "))
    10/a
except TypeError:
    print("Esto es una cadena")
except ValueError:
    print("La cadena debe ser un número")
except ZeroDivisionError:
    print("No se puede dividir por 0")
except Exception as x:
    print( type(x).__name__ )    



"""


#####################################################################################

#PROGRAMACIÓN ORIENTADA A OBJETOS

#CLASE VACÍA
"""

class Estudiante:
    pass

Estudiante = Estudiante()


"""


#Clase con métodos que si se quiere no se ponen

""" 
class Fabrica:
    def __init__(self,marca,nombre,precio,descripcion,ruedas=None,distribuidor=None):
        self.marca = marca
        self.nombre = precio
        self.descripcion = descripcion
        self.ruedas = ruedas
        self.distribuidor = distribuidor

Auto = Fabrica('Ford', 'Ranger', 'Camioneta 4x4', 4 )

Auto.nombre


"""




#CLASE CON ATRIBUTOS

""" 
class Auto:
    Rojo = False

    def __init__(self, puertas, color):
        self.puertas = puertas
        self.color = color
        print("Se creò un Auto con Puertas {} y color {}".format(puertas, color))

    def Fabricar(self):    
        self.Rojo = True

    def confirmar_fabricacion(self):
        if(self.Rojo):
            print("Auto Coloreado Rojo")
        else:
            print("Aun no está coloreado")    


a = Auto("2", "Rojo")

"""


#INIT (iniciardor) DEL (BORRADOR)
#si se ejecuta 2 veces, primero se ejecuta el init, después el delete

"""
class Fabrica:
    def __init__(self,tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)

    def __del__(self):
        print("Se elimino el auto", self.nombre)    

    def __str__(self):
        return "{} se fabrica con exito, en el tiempo {} y tiene esta cantidad {}".format(self.nombre,self.tiempo,self.ruedas)

a = Fabrica(10, "Alvaro", 4)
a = Fabrica(10, "Alvaro", 4)
"""



#ENCAPSULAMIENTO
#llamar métodfos y atributos privadas a travez de métodos y atributos publicos


"""

class encapsulamiento:
    __privado_atri = "Soy un atributo provadiu que no se puede acceder"

    def __privado_met(self):
        print("soy método que no se puede acceder porque es privado")

    def publico_atri(self):
        return self.__privado_atri

    def public_met(self):
        return self.__privado_met()

e = encapsulamiento()

e.publico_atri()


"""


#HERENCIA

"""
class Fabrica:
    def __init__(self,marca,nombre,precio,descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return """\
MARCA\t\t{}            
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t\t{} """.format(self.marca, self.nombre, self.precio, self.descripcion)


class Auto(Fabrica):
    pass


z = Auto('Ford', 'Ranger', '100.000', 'Camionera')
print(z)



"""








