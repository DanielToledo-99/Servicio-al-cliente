
import os
from usuarios import persona
def menu():
    os.system('clear')
    print("------- BIENVENIDO AL SERVICIO AL CLIENTE DE BOOKSMART --------")
    print("Por favor inicie sesion para poder ayudarlo")
    print ("\t1 - Iniciar Sesion")
    print ("\t2 - Salir")
usuario=persona()
while True:
    menu()
    opcionMenu=input("Ingrese su opcion >>")
    if opcionMenu=="1":
        os.system('clear')
        usuario.valida()
    elif opcionMenu=="2":
        print("Gracias por su peferencia")
        break
    else:
        print("Opcion incorrecta, vuelva a intentarlo")
