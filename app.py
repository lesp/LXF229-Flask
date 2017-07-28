from flask import Flask, render_template
from gpiozero import LED

led = LED(4)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on/')
def on():
    led.toggle()
    return render_template('index.html')

@app.route('/off/')
def off():
    led.off()
    return render_template('index.html')
         

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
