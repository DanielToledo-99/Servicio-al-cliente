from cisco import ruta_pedido
import os
array_reclamos=[['Juan','123123','E'],['Juan','123123','E'],['Juan','123123','E']]
class reclamos:
    def reclamos_menu(self):
        while True:
            os.system('clear')
            print("------- BIENVENIDO AL SERVICIO AL CLIENTE DE BOOKSMART --------")
            print("¿Como podemos ayudarlo?")
            print ("\t1 - Reclamos y Devoluciones")
            print ("\t2 - Salir")
            opcionMenu=input("Ingrese su opcion >>")
            if opcionMenu=="1":
                os.system('clear')
                print("-------  SERVICIO AL CLIENTE DE BOOKSMART --------")
                tiempo= len(array_reclamos)*15
                print("EN ESPERA ESTAN ", len(array_reclamos)," PERSONAS DELANTE DE USTED Y EL TIEMPO APROXIMADO DE ATENCION ES DE ",tiempo," Minutos" )
                print("DESEA ESPERAR (1) O DEJENOS UN TELEFONO PARA PONERNOS EN CONTACTO CON USTED(2)")
                opcionMenu=input("Ingrese su opcion >>")
                if opcionMenu=="1":
                    print(" SU TIEMPO DE ESPERA ES DE", tiempo, ", DISCULPE POR LA DEMORA UNO DE NUESTROS TRABAJADORES SE PONDRA PRONTO EN CONTACTO ")
                    input("INGRESADO A LA COLA DE ESPERA, MANTENGASE CONECTADO HASTA QUE UN AGENTE SE COMUNIQUE CON USTED")
                elif opcionMenu=="2":
                    while True:
                        a=(input("Ingrese un numero para contactarnos con usted en la brevedad >>"))
                        if len(a)==9:
                            input("Ingresando a la cola... Pronto nos estaremos comunicando con usted")
                            break
                        else:
                            print("Numero ingresado incorrecto, vuelva a intentarlo")
                            input("")
            elif opcionMenu=="2":
                print("Gracias por su peferencia")
                break
            else:
                print("Opcion incorrecta, vuelva a intentarlo")