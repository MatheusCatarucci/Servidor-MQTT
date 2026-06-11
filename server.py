import paho.mqtt.publish as publish

MQTT_HOST = "192.168.0.114"
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

def ascender_led():
    publish.single(
        TOPICO,
        "ON",
        hostname=MQTT_HOST,
        port=1883,
        auth=MQTT_AUTH
    )

    return {"status": "LED Ligado"}


def apagar_led():
    publish.single(
        TOPICO,
        "OFF",
        hostname=MQTT_HOST,
        port=1883,
        auth=MQTT_AUTH
    )

    return {"status": "LED Desligado"}
