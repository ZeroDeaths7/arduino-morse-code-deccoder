import serial
import time

# Change this to match your Arduino COM port (e.g., "COM3" on Windows, "/dev/ttyUSB0" on Linux)
SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

def read_serial_data():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the connection to stabilize

        while True:
            data = ser.readline().decode().strip()  # Read and clean the incoming data
            if data:
                yield f"data: {data}\n\n"  # Send data as an event-stream
    except Exception as e:
        print("Error:", e)
