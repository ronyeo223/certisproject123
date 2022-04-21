import paho.mqtt.client as mqtt
global y
y = 166
global x
x = 350
n = 25
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global y
    global x
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subcriptions will be renewed.
    client.subscribe("test/direction") 
    client.publish("test/robotloca", f"x = {x}, y = {y}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global y 
    global x 
    n=25
    print(msg.topic+" "+str(msg.payload))
    if msg.topic != "test/direction":
        if str(msg.payload) == "Dock":
            client.publish("test/robotloca", f"x = {x}, y = {y}")
        elif str(msg.payload) == "Up":
            y+=n
            client.publish("test/robotloca", f"x = {x}, y = {y}")
        elif str(msg.payload) == "Down":
            y-=n
            client.publish("test/robotloca", f"x = {x}, y = {y}")
        elif str(msg.payload) == "Left":
            x-=n 
            client.publish("test/robotloca", f"x = {x}, y = {y}")
        elif str(msg.payload) == "Right":
            x+=n
            client.publish("test/robotloca", f"x = {x}, y = {y}")



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever