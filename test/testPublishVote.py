import paho.mqtt.client as mqtt

client = mqtt.Client("axadodavote")
client.connect("iot.eclipse.org")
client.publish("paho/metest/axadodavote", payload="like")
client.publish("paho/metest/axadodavote", payload="dislike")
client.publish("paho/metest/axadodavote", payload="dislike")
client.publish("paho/metest/axadodavote", payload="dislike")
client.publish("paho/metest/axadodavote", payload="like")
client.publish("paho/metest/axadodavote", payload="like")
client.publish("paho/metest/axadodavote", payload="like")
client.publish("paho/metest/axadodavote", payload="like")
client.publish("paho/metest/axadodavote", payload="like")

