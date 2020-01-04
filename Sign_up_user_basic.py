#enter data in the database
import pymysql
import hashlib
from pymysql import MySQLError

global nombre
global email
global contrasenia
global tipo_usuario
#----------------------------------------------------funciones-------------------------------------------------
#comprobación de existencia de usuario en la bd:
def nombreBD(name):
    try:
        db = pymysql.connect("localhost", "root", "", "login")
        cursor = db.cursor()
        consulta = "select nombre from usuarios where nombre=%s"
        valor = (name)
        cursor.execute(consulta, valor)
        result = cursor.fetchone()  # row method
        if result[0]==name:
            print("incorrecto, ya existe en la bd")
        else:
            print("esta si q si")
            return True
        db.close()

    except TypeError:
        return True
    except ConnectionRefusedError:
        print("error al conectarse a la base de datos, revise su coneccio al servidor y vuelva a intentarlo")

#funcion validación nickname
def nickname(nombre_usuario):
    long=len(nombre_usuario)#longitud del usuario
    y=nombre_usuario.isalnum()#comprueba que la cadena tenga valores alfanumericos

    if y==False:# la cadena contiene valores no alfanumericos
        print("el nombre de usuario puede contener solo letrasa y numeros: ")
    if long <4 or long >10:
        print("la longitud del nombre de usuario deberia ser entre 4 y 10 caractéres: ")
    if long >5 and long <10 and y==True:
        return True

#funcion validación password
def clave(password):
    validar=False
    long=len(password)
    espacio=False
    mayusculas=False
    minusculas=False
    numeros=False
    y=password.isalnum()
    correcto=True
    
    for carac in password:
        if carac.isspace()==True:
            espacio=True
        if carac.isupper()==True:
            mayuscula=True
        if carac.islower()==True:
            minuscula=True
        if carac.isdigit()==True:
            numeros=True
    if espacio==True:
        print("la contraseña no puede tener espacios")
    else:
        validar=True #se cumple el requsito de no tener espacios

    if long <5 and validar==True:
        print("la contraseña deberia tener al menos 5 caractéres")
        validar=False
    
    if (mayuscula==True) and (minuscula==True) and (numeros == True) and (y== False) and (validar ==True):
        validar=True
    else:
        correcto=False
    
    if (validar==True) and (correcto==False):
        print("la contraseña elegida no es segura")
    if (validar==True) and (correcto==True):
        return True

#función tipo 
def tip1(tipe):
    long1=len(tipe)
    h=tipe.isdigit()
    if h==False:# la cadena contiene valores no alfanumericos
        print("el tipo de usuario es un digito de 1 al 3!!!")
    if long1 <0 or long1 >2:
        print("de 1 al 3")
    if long1 ==1 and h==True:
        return True           
#----------------------------------------------------------fin funciones-------------------------------

#db = pymysql.connect("database_host","username","password","database_name")
db=pymysql.connect("localhost","root", "", "login")
cursor=db.cursor()

#comprobacion de existencia en la bd
correcto=False

#comprobacion de formato no rula despues de modificar la comprobacion de bd
print("el nombre se usuario deberia tener entre 4 y 10 caractéres: ")
while correcto==False:
    nombre = input(" ingerese el nombre de usuario: ")
    if nickname(nombre)==True and nombreBD(nombre) == True:
         print("nombre bd y el formato estan ok")
         correcto = True
    else:
         print("fotmato usuario incorrecto")


# introducir email:
email = input("email: ")

#introducir contraseña y comprobacion de formato
while correcto == True:
    print("la contraseña deberia tener al menos 5 caractéres, mayusculas y minusculas y un caracter especial: ")
    contrasenia = input("introduce tu contraseña: ")
    if clave(contrasenia) == True:
        print("la contraseña es adecuada ^^")
        correcto = False

#introduccion de tipo de admin
while correcto == False:
    tipo_usuario = input("introduce el tipo de ususario (1, 2 o 3): ")
    if tip1(tipo_usuario) == True:
        print("el tipo correcto")
        correcto = True

# encriptar contraseña.
cifrada = hashlib.md5(contrasenia.encode())

# consulta sql poara dar el alta al usuario verificado a traves de los procedimientos anteriores
sql = "INSERT INTO usuarios (nombre, email, contasenia, tipo) values(%s, %s, %s, %s)"
val = (nombre, email, cifrada.hexdigest(), tipo_usuario)
try:
    cursor.execute(sql, val)
    db.commit()
    print("datos introducidos en la bd correctamente ^^")
    # print("la contraseña creada es: ",contEncriptada)
except ConnectionRefusedError:
    print("error al conectarse a la base de datos, revise su coneccio al servidor y vuelva a intentarlo")
except MySQLError as e:
    print('Got error {!r}, errno is {}'.format(e, e.args[0]))
    print("error al introducir los datos en la bd :(")
db.close()


