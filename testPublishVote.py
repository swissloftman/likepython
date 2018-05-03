import paho.mqtt.client as mqtt

client = mqtt.Client("axadodavote")
client.connect("iot.eclipse.org")
client.publish("paho/metest/axadodavote", payload="Like")
client.publish("paho/metest/axadodavote", payload="dislike")
