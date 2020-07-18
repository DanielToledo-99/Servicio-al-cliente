from cisco import ruta_pedido
import os
from menu_usu_reclamos import reclamos
from cola_usu import Cola
def menu_trabajador():
    os.system('clear')
    print("------- BIENVENIDO AL SERVICIO AL CLIENTE DE BOOKSMART --------")
    print ("\t1 - Atencion de clientes")
    print ("\t2 - Modificar datos")
    print ("\t3 - Salir")
while True:
    menu_trabajador()
    opcionMenu1=input("Ingrese su opcion >>")
    if opcionMenu1=="1":
        os.system('clear')
        objetoCola = Cola(10)
        objetoCola.acciones()
    elif opcionMenu1=="2":
        persona=persona() #cambiar por el usuario 
        persona.cambios() # reemplazar y luego modificar base de datos
    elif opcionMenu1=="3":
        break
    else:
        print("Opcion incorrecta, vuelva a intentarlo")