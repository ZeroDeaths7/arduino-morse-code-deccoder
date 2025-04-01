from flask import Flask, render_template, Response
from serial_reader import read_serial_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(read_serial_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
