from time import time           #Importamos la librería time
from usuarios import persona     #Importamos la clase persona
personademo=persona()           #Instanciamos una nueva persona
#personademo.agregaNombrePersona() # ejemplo de llamado individual

statusId=[False,None]

status=[False]

def logIn():
  usr=input("usuario: ")
  password=input("password: ")
  fh = open("persona.txt", "r")		#Abrir archivo en modo lectura
  fila = 1							#Iniciamos contador de filasv", "r")		#Abrir archivo en modo mujeres
  status[0]=False
  for linea in fh:
    if fila > 1:
      data = linea.strip()
      lista = data.split(",")
      id = lista[0]			#Capturar primer elemento (nombre)
      usrfile = lista[1]
      passwordfile = lista[4]
      if ((usr==usrfile) and (password==passwordfile)): # para poder comparar o ingresado con lo que ya teniamos
        status[0]=True
        status.append(lista[0])
        status.append(lista[1])
        status.append(lista[2])
        status.append(lista[3])
        status.append(lista[4])
        status.append(lista[5])
    fila += 1
  return status
print (logIn())