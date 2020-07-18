import os
class Cola ():
  
  def __init__(self, tam):
    self.cola = []
    self.Rear = None
    self.Front = None
    self.tam = tam
  
  def listarCola(self):
    print (self.cola)
    
  def enQueue(self, date):
    if len(self.cola) >= self.tam:
      print ("¡Cola Llena! // ¡Overflow!")
    else:
      self.Rear = date
      self.cola.append(date)
      
  
  def deQueue(self):
    if len(self.cola) == 0:
      print ("!Cola Vacia¡ // Underflow")
    else:
      self.cola.pop(0)
      return self.listarCola()
  
  def totalQueue(self):
    if len(self.cola) == 0:
      print ("¡Cola Vacia! // No hay clientes en espera")
    else:
      print (len(self.cola))
  def sizeQueue(self):
    print (self.tam)
        
  def getFront(self):
    if len(self.cola) == 0:
      print ("¡Cola Vacia! // No hay clientes en espera ")
    else:
      a = self.cola[0]
      self.Front = a
      c = self.Front
      while True:
        os.system('clear')
        print ("Cliente con orden de atencion 1 es: ", c)
        atentido=input("Concluyo la atencion del cliente (Y/N) >> ")
        a1=atentido.upper()
        if (atentido=="Y"):
          atentido2=input("Confirmando atencion (Y/N) >>")
          a2=atentido2.upper()
          if (a2=="Y" and a1=="Y"):
            #eliminando usuario de la tabla cola en la base de datos
            print("Usuario eliminado de la cola de atencion")
            break
        


  def acciones(self):
    objetoCola = Cola(10)#modificacion, aqui se tendra que guardar los elentos que se extraigan de la tabla cola
    objetoCola.enQueue("1")
    objetoCola.enQueue("2")
    objetoCola.enQueue("3")
    objetoCola.enQueue("4")
    print ("======== Menu de Cola de Atencion =========")
    print ("Seleccionar una opción")
    print ("1.- Listar Clientes en la Cola")
    print ("2.- Ver el Total de elementos de la Cola")
    print ("3.- Ver cuantos clientes estan es la cola")
    print ("4.- Obtener el primer cliente en la Cola")
    print ("5.- Salir")
    print ("================================")  

    opcionesMenu = input ("Escoja un numero (opción) :")
    os.system('clear')
    while True:
      if opcionesMenu == "1":
        os.system('clear')
        print ("Clientes en espera")
        objetoCola.listarCola()
        input("Presione cualquier tecla para volver al menu")
        os.system('clear')
        objetoCola.acciones()
      elif opcionesMenu == "2":
        os.system('clear')
        objetoCola.totalQueue()
        input("Presione cualquier tecla para volver al menu")
        os.system('clear')
        objetoCola.acciones()
      elif opcionesMenu == "3":
        os.system('clear')
        objetoCola.sizeQueue()
        input("Presione cualquier tecla para volver al menu")
        os.system('clear')
        objetoCola.acciones()      
      elif opcionesMenu == "4":
        os.system('clear')
        objetoCola.getFront()
        input("Presione cualquier tecla para volver al menu")
        os.system('clear')
        objetoCola.acciones()
      elif opcionesMenu == "5":
        break
      else:
        objetoCola.acciones() 