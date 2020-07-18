import urllib.parse
from pip._vendor import requests
from datetime import datetime, date, time, timedelta
import calendar
class ruta_pedido:

    def consulta(self):
        while True: 
            orig = ("Lima")
            dest = ("Arequipa")
            main_api = "https://www.mapquestapi.com/directions/v2/route?"
            key= "kOJAGLUHCqyQg9JK0GYAeGVpkwRhSfGP"
            array=[]
            url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
            json_data = requests.get(url).json() 
            json_status = json_data["info"]["statuscode"]  
            if json_status == 0:
                #print("API Status: " + str(json_status) + " = A successful route call.\n")
                print("==================== DETALLE DE TU PEDIDO =======================")
                print("Los pedidos realizados pasados las 11 am se enviaran al dia siguiente, Gracias por su comprension")
                print("Entrega desde " + (orig) + " a " + (dest))
                print("Kilómetros a recorrer:  " +str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
                #print("Combustible(Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
                print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
                print("=============================================")
                for each in json_data["route"]["legs"][0]["maneuvers"]:
                    a=(each["narrative"]) + " (" +str("{:.2f}".format((each["distance"])*1.61) + " km)")
                    array.append(a)
                    #print((each["narrative"]) + " (" +str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                    #print("=============================================\n")
                    #print("=============================================")
            elif json_status == 402:
                print("**********************************************")
                print("Status Code: " + str(json_status) + ";Entrada invalida para una o ambas ubicaciones.")
                print("**********************************************\n")
            else:
                print("************************************************************************")
                print("For Staus Code: " + str(json_status) + ";Refer to:")
                print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            hora=json_data["route"]["formattedTime"][0:2]
            ruta=int(hora)
            day=1
            ahora = datetime.now()
            hora_pedido=ahora.hour
            array_ruta=[]
            cont=0
            while ruta>0:
                ruta=ruta-1
                array_ruta.append(array[cont])
                cont=cont+3    
            

            if int(hora)>24:
                day=day+(int(hora)//24)
                print (day)
            if hora_pedido>9:
                day+=1 
            print ("Tu pedido se realiazo el >> ", "Fecha: " ,ahora.day,"/",ahora.month,"/",ahora.year, "Hora: ",ahora.hour,":",ahora.minute)
            print ("Llegara el dia >> ", ahora.day+day,"/",ahora.month,"/",ahora.year)
            print("Tu pedido esta en >> ", array_ruta[1])
            print("Para volver al menu presione 1")
            opcion=input("")
            if opcion=="1":
                break
            else:
                print("No hay mas opciones")
        