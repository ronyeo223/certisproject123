from flask import Flask, render_template
import os

ip_list = ['192.168.229.150']
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(f"UP {ip} Ping Successful")

            return 'Ping Successful'
        else:
            print(f"DOWN {ip} Ping Unsuccessful")  

            return 'Ping Unsuccessful'
        

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")
