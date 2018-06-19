import stepmotor as motor
import paho.mqtt.client as mqtt
from votingCalculator import VotingCalculator

calc = VotingCalculator()
delay = 2
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("paho/metest/axadodavote")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("-------------------------------------------")
    motostep = calc.getMotoSteps(msg.payload)
    if "NCW" in motostep:
        motor.backwards(motostep.replace("NCW", ""))
        print("Backward Steps: "+str(motostep.replace("NCW", "")))
    elif "CW" in motostep:
        motor.forward(motostep.replace("CW",""))
        print("Forward Steps: "+str(motostep.replace("CW", "")))
    print(msg.topic+" "+str(motostep) + " "+ msg.payload)
    print("-------------------------------------------")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

