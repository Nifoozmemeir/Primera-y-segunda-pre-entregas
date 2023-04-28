Base_de_datos = {}
def datos_usuarios():
    N_de_usu = input("Ingrese su nombre de usuario: ")
    Contraseña = input("Ingrese su contraseña: ")
    Base_de_datos[N_de_usu] = Contraseña

def mostrar_datos():
    for dato in Base_de_datos.keys():
        print("El usuario es: "+ dato + " la contraseña es: " + Base_de_datos[dato])

def login():
    usu_input = input("Ingrese su nombre de usuario: ")
    if(Base_de_datos.get(usu_input) == None):
        while Base_de_datos.get(usu_input) == None:
            usu_input = input("Usuario Incorrecto, ingrese nuevamente: ")
        print("Usuario correcto!")
    pas_input = input("Ingrese su contraseña: ")
    while pas_input != Base_de_datos[usu_input]:
            pas_input = input("Contraseña equivocada, ingrese una nueva contraseña: ")
    print("Contraseña correcta!")
    print("Iniciaste sesión correctamente!")

print("Ingreso de usuarios")
datos_usuarios()
datos_usuarios()
datos_usuarios()
print("Los datos de los usuarios son: ")
mostrar_datos()
print("login de usuarios")
login()

with open("test.txt", "w") as testtxt:
    for dato in Base_de_datos.keys():
        testtxt.write(dato)
    for dato in Base_de_datos.values():
        testtxt.write(dato)
testtxt.close
