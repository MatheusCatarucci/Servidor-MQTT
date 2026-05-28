import paho.mqtt.client as mqtt
import threading

BROKER_IP   = "0.0.0.0"    # <- IP do broker (Gustavo)
BROKER_PORT = 1883

TOPIC_STATUS = "senai/grupo1/dispositivo/status"
TOPIC_CMD    = "senai/grupo1/dispositivo/cmd"

# Estado compartilhado com o app.py
estado = {"dispositivo": "OFF"}

# ───────────────────────────────────────────
def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Conectado ao broker. Código: {rc}")
    client.subscribe(TOPIC_STATUS)

def on_message(client, userdata, msg):
    valor = msg.payload.decode()
    estado["dispositivo"] = valor
    print(f"[MQTT] Status recebido: {valor}")

# ───────────────────────────────────────────
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def iniciar():
    client.connect(BROKER_IP, BROKER_PORT)
    thread = threading.Thread(target=client.loop_forever, daemon=True)
    thread.start()

def publicar(comando: str):
    client.publish(TOPIC_CMD, comando)
    print(f"[MQTT] Comando enviado: {comando}")