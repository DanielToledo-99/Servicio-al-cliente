from cisco import ruta_pedido
from usuarios import persona
from menu_usu_reclamos import reclamos
import os
def menu_usu():
    os.system('clear')
    print("------- BIENVENIDO AL SERVICIO AL CLIENTE DE BOOKSMART --------")
    print("¿Como podemos ayudarlo?")
    print ("\t1 - Estado de mi pedido")
    print ("\t2 - Devoluciones o Reclamos")
    print("\t3 - Cambiar contraseña")
    print ("\t4 - Salir")
while True:
    menu_usu()
    opcionMenu1=input("Ingrese su opcion >>")
    if opcionMenu1=="1":
        os.system('clear')
        pedido= ruta_pedido()
        pedido.consulta()
    elif opcionMenu1=="2":
        reclamos = reclamos()
        reclamos.reclamos_menu()
    elif opcionMenu1=="3":
        os.system('clear')
        person=persona()
        person.cambios()
    elif opcionMenu1=="4":
        print("Gracias por su peferencia")
        break
    else:
        print("Opcion incorrecta, vuelva a intentarlo")