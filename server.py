import paho.mqtt.client as mqtt

BROKER_IP = "0.0.0.0"
BROKER_PORT = 1883
TOPIC_STATUS = "senai/grupo1/dispositivo/status"

estado = {"dispositivo": "off"}


def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    estado["dispositivo"] = payload


def obter_status() -> dict:
    return {"status": estado["dispositivo"]}


def iniciar():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER_IP, BROKER_PORT)
    client.subscribe(TOPIC_STATUS)
    client.loop_start()