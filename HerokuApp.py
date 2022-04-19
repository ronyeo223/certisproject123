from flask import Flask, render_template
import paho.mqtt.client as mqtt


app = Flask(__name__)

global y
y = 166
global x
x = 350

direction = {"dire1" : "Up",
             "dire2" : "Left",
             "dire3" : "Down",
             "dire4" : "Right"}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
client.on_subscribe = on_subscribe
client.connect("broker.emqx.io", 1883)


@app.route("/")
def route():
   client.publish("test/robot", "Dock", qos = 1)
   client.subscribe("test/robotloca", qos = 1)
   client.message_callback("robotloca")
   return render_template("index.html")


@app.route("/<string:dire>")
def start(dire):
   global y
   global x
   n=25
   client.subscribe("test/robotloca")
   client.loop_start
   if dire == "Up":
      y += n
      client.publish("test/direction", "Up", qos = 1)
      client.publish("test/robot",f"x = {x}, y = {y}" )

   elif dire == "Left":
      x -= n
      client.publish("test/direction", "Left", qos = 1)
      client.publish("test/robot",f"x = {x}, y = {y}" )

   elif dire == "Down":
      y -= n
      client.publish("test/direction", "Down", qos = 1)
      client.publish("test/robot",f"x = {x}, y = {y}" )

   elif dire == "Right":
      x += n
      client.publish("test/direction", "Right", qos = 1)
      client.publish("test/robot",f"x = {x}, y = {y}" )


   client.loop_stop

   return render_template("index.html")



if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0")
