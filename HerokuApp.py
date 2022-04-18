from flask import Flask, render_template, flash, request
import paho.mqtt.client as mqtt


app = Flask(__name__)

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
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
client.username_pw_set("esznwayl","gqXdqVuApw95")
client.connect("driver.cloudmqtt.com", 18626, 60)


@app.route("/")
def route():
   client.publish("$SYS/robot", "Dock", qos = 1)
   return render_template("index.html")


@app.route("/<string:dire>")
def start(dire):
   y = 0
   client.loop_start
   if dire == "Up":
      x = x + 25
      p = x + 25
      client.publish("$SYS/direction", "Up", qos = 1)
      client.publish("$SYS/robot", p)
   
   elif dire == "Left":
      client.publish("$SYS/direction", "Left", qos = 1)

   elif dire == "Down":
      client.publish("$SYS/direction", "Down", qos = 1)

   elif dire == "Right":
      client.publish("$SYS/direction", "Right", qos = 1)

   client.loop_stop
   return render_template("index.html")



if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0")
