import paho.mqtt.client as mqtt
import time

broker = "127.0.0.1" # Il nostro PC locale (dove sta girando Docker)
port = 1883
topic = "fabbrica/sensore_temperatura"

# Creiamo il client MQTT finto
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Sensore_Falso_1")
client.connect(broker, port)

print("Sensore connesso al broker. Inizio invio dati in chiaro...")

# Ciclo infinito che invia la temperatura ogni 3 secondi
while True:
    payload = '{"temperatura": 25.5, "status": "ATTENZIONE_SURRISCALDAMENTO", "password_sensore": "admin123"}'
    client.publish(topic, payload)
    print(f"Inviato: {payload}")
    time.sleep(3)