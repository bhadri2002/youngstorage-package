from pymongo import MongoClient
import paho.mqtt.client as mqtt
import os

client = MongoClient(str(os.getenv("MONGODB_URL")))

db = client[str(os.getenv("MONGODB_NAME"))]

mqtt_client = mqtt.Client()

# MQTT callback functions


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Connection to MQTT broker failed")


def on_message(client, userdata, msg):
    print("Received message:", msg.topic, msg.payload)


# Connect MQTT client
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("172.32.0.3", 1883, 60)

# Start MQTT client loop in a separate thread
mqtt_client.loop_start()
