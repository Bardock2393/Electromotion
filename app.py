import json
import time
from flask import Flask, render_template, make_response
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    url = "https://sbucket2393.s3.amazonaws.com/mykey"
    response = urlopen(url)
    variable = json.loads(response.read())
     
      

    Dc_Current = variable['Dc_current']
    Dc_Voltage =  variable['Dc_voltage']
    Dc_Power =  variable['Dc_power']
    Dc_Energy =  variable['moter_temperture']
    Ac_Current =  variable['Ac_current']
    Ac_Voltage =  variable['Ac_voltage']
    Ac_Power =    variable['throttle']
    Motor_Speed=  variable['motor_speed']
    throttle=  variable['throttle']
    x = time.time() + 19800

    

    

    data = [x * 1000,Dc_Current,Dc_Voltage,Dc_Power, Dc_Energy ,Ac_Current, Ac_Voltage, Ac_Power,Motor_Speed,throttle]

   
    time.sleep(1)
  
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
