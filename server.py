import paho.mqtt.publish as publish

MQTT_HOST = "192.168.0.113"
MQTT_AUTH = {
    "username": "gp3",
    "password": "321"
}

TOPICO = "esp_led"

def enviar_mensagem(mensagem: str):
    publish.single(
        topic=TOPICO,
        payload=mensagem,
        hostname=MQTT_HOST,
        auth=MQTT_AUTH
    )