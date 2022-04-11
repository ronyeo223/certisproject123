from flask import Flask, render_template, flash, request
import paho.mqtt.client as mqtt
app = Flask(__name__)

direction = {"dire1" : "Forward",
             "dire2" : "Left",
             "dire3" : "Back",
             "dire4" : "Right"}



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

#client = mqtt.Client()


@app.route('/', methods = ["GET", "POST"])
def my_link1():

   return render_template('index.html')




if __name__ == '__main__':
   app.run(debug = True)