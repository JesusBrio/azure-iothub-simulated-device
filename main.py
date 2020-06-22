from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import time
import json
import uuid
from datetime import datetime
import random
import json
import threading as TH

def ReceiveMessage(client):
    while True:

        try:
            print("Escuchando mensaje del IotHub...")

            message = client.receive_message()
            
            message_json=json.loads(message.data.decode("utf-8"))
            print(message_json)
        except Exception as e:
            print(e)
            print ( "Client del IotHub con Error" )

def SendTelemetry(client):
    while True:
    
        try:
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            ill not take more pictures after the first one is taken
            t = time.localtime()
            timestamp = time.strftime('%b-%d-%Y_%H%M', t)
            pic_no = random.randint(1,1001)
            piece_no= random.randint(1,10001)
            roi_section=random.randint(1,5)
            plant_no=random.randint(1,6)
            line= random.randint(1,9)
            loc=1
            camera=random.randint(1,5)
            node_version=1
            confidence=round(random.uniform(0,1),4)
            project=1
            type_photo=1
            id_class=str(uuid.uuid1().hex)
            classification=random.getrandbits(1)
            id_roi=str(uuid.uuid4().hex)
            id_photo=str(uuid.uuid1().int)

            ini_string = {"pic_no":int(pic_no),"piece_no": int(piece_no), "roi_section":int(roi_section), "plant_no":int(plant_no), "line":int(line), "loc":int(loc), "camera":int(camera),"confidence":float(confidence),"classification":int(classification), "id_class":id_class, "id_photo":id_photo, "id_roi":id_roi} 
 
            # printing initial json 
            msg_txt_formatted = json.dumps(ini_string)      
            message = Message(msg_txt_formatted)


            # Enviar mensaje al IotHub
            print( "Mensaje enviado: {}".format(message) )
            client.send_message(message)
            print ( "Mensaje enviado satisfactoriamente" )
            time.sleep(30)
            #client.disconnect()
        except Exception as e:
            print(e)
            print ( "Client del IotHub con Error" )
    
if __name__ == "__main__":

    #Definimos el connection string
    connection_string = [CONNECTION STRING]
    
    #Creamos el objeto cliente que iniciará una sesión con el IotHub
    client = IoTHubDeviceClient.create_from_connection_string(connection_string)

    #Llamamos a la función ReceiveMessage pansandole el objeto cliente para empezar a escuchar los mensajes del IotHub
    ReceiveMessageThread = TH.Thread(target=ReceiveMessage, args=(client,))
    ReceiveMessageThread.start()
    #Llamamos a la función SendTelemetry pasandole el objeto cliente 
    # para empezar a enviar mensajes al IotHub
    
    SendTelemetryThread = TH.Thread(target=SendTelemetry, args=(client,))
    SendTelemetryThread.start()
