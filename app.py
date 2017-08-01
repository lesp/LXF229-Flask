from flask import Flask, render_template
from gpiozero import LED, Motor
from time import sleep

led = LED(4)
motor = Motor(forward=17, backward=27)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle/')
def on():
    led.toggle()
    return render_template('index.html')
     
@app.route('/motor-forwards/')
def motorforwards():
    motor.forward()
    sleep(1)
    motor.stop()
    return render_template('index.html')

@app.route('/motor-backwards/')
def motorbackwards():
    motor.backward()
    sleep(1)
    motor.stop()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
