import paho.mqtt.client as mqtt
import ssl
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connesso al broker sicuro con codice: {rc}")

client = mqtt.Client()
client.on_connect = on_connect

#Attivo la crittografia passando il certificato della CA
client.tls_set(ca_certs="certs/ca.crt", certfile="certs/client.crt", keyfile="certs/client.key", tls_version=ssl.PROTOCOL_TLSv1_2)

#Disabilito il controllo sull'hostname per evitare falsi allarmi del certificato in ambiente locale
client.tls_insecure_set(True)

#Mi connetto sulla nuova porta sicura 8883
client.connect("127.0.0.1", 8883, 60)

client.loop_start()
try:
    while True:
        payload = '{"temeratura": 24.5, "password": "segretissima"}'
        client.publish("fabbrica/sensore_temperatura", payload)
        print("Messaggio cifrato inviato sulla porta 8883!")
        time.sleep(3)
except KeyboradInterrupt:
    client.loop_stop
    client.disconnect()
    print("\n Client disconnesso.")