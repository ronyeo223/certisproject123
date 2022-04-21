import paho.mqtt.client as mqtt



global y
y = 166
global x
x = 350
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.publish("test/robotloca", f"x= {x} y = {y}")
    client.subscribe("test/direction", qos = 1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global y
    global x
    n = 25
    print(msg.topic+" "+str(msg.payload))
    if (msg.payload) == b'Up' or b'up':
        y += n
        client.publish('test/direction', f"x= {x} y= {y}")
        

def on_publish(client,userdata,result): #create function for callback
    client.publish("test/robotloca", f"x= {x} y = {y}")
    print(f"published data is : x= {x} y = {y}")
  
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("broker.emqx.io", 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
