from time import time
from datetime import datetime
import os
from cisco import ruta_pedido
from menu_usu_reclamos import reclamos
class persona():
  def __init__(self):
    self.statusId=[False,None]
    self.status=[False]
  def logIn(self):
    os.system('clear')
    print("------ LOGIN ------")
    usr=input("Usuario: ")
    password=input("Password: ")
    fh = open("persona.txt", "r")		#Verficamos en la base de datos, cambio 
    fila = 1						
    self.status[0]=False
    for linea in fh:
      if fila > 1:
        data = linea.strip()
        lista = data.split(",")
        id = lista[0]			#Capturar primer elemento (nombre)
        usrfile = lista[1]
        passwordfile = lista[4]
        if ((usr==usrfile) and (usr==usrfile)):
          self.status[0]=True
          self.status.append(lista[0])
          self.status.append(lista[1])
          self.status.append(lista[2])
          self.status.append(lista[3])
          self.status.append(lista[4])
          self.status.append(lista[5])
      fila += 1
    return self.status

  def valida(self):
    while(True):
        print("------ LOGIN ------")
        print ("1 - Ingresar usuario y password")  
        print ("2 - Salir")      
        op=input("Ingrese opción >>")
        if (int(op)==1):
          os.system('clear')
          estado=self.logIn()
          #comprobar el tipo de perosna dependiendo de eso direccionar al menu correspondiente, base de dato
          if(estado[0]):
              self.statusId[1]=estado
              print ("Bienvenido " + str(estado[2]))
              #print(menu_usu()) # cambiar ruta una vez implementado la base de datos
              break 
        elif (int(op)==2):
            os.system('clear')
            print("Gracias por su preferencia vuelva pronto")
            break
        else:
          print ("Opcion Incorrecta, vuelva a intentarlo")
  def menu_cambios(self):
      os.system('clear')
      print("------- BIENVENIDO AL SERVICIO AL CLIENTE DE BOOKSMART --------")
      print("\t1 - Cambiar Usuario")
      print ("\t2 - Cambiar Contraseña")
      print ("\t3 - Salir")
  def cambios(self):
      while True:
        self.menu_cambios()
        opcionMenu=input("Ingrese su opcion >>")
        if opcionMenu=="1":
          os.system('clear')
          a=input("Ingrese su nuevo usuario >> ")
          #cambio con en la base de datos
          print("Cambio exitoso")
          input("Presione cualquier tecla para regresar al menu")
        elif opcionMenu=="2":
          os.system('clear')

          while True:
            a=input("Ingrese su nueva contraseña >> ")
            b=input("Confirme contraseña >> ")
            if (a ==b):
              #cambio con en la base de datos
              print("Cambio exitoso")
              break
            else:
              print("Las contraseñas no coinciden ...")
              input("")
              os.system('clear')
          input("Presione cualquier tecla para regresar al menu")
        elif opcionMenu=="3":
          break
        else:
          print("Opcion incorrecta, vuelva a intentarlo")
