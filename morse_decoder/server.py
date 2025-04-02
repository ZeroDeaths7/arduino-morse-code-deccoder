from flask import Flask, render_template, Response
import serial

app = Flask(__name__)

# Replace 'COM3' (Windows) or '/dev/ttyUSB0' (Linux/Mac) with your port
ser = serial.Serial('COM3', 9600, timeout=1)

def read_morse():
    while True:
        data = ser.readline().decode('utf-8').strip()
        if data:
            yield f"data: {data}\n\n"  # Server-Sent Events (SSE) format

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(read_morse(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
