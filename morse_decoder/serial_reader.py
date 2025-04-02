import serial
import time

# Change this to match your Arduino COM port (e.g., "COM3" on Windows, "/dev/ttyUSB0" on Linux)
SERIAL_PORT = "COM8"
BAUD_RATE = 9600

def read_serial_data():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Wait for the connection to stabilize

        while True:
            data = ser.readline().decode().strip()  # Read and clean the incoming data
            if data:
                # Split by spaces or colons and take the last part (assumed to be the letter)
                parts = data.split()
                decoded_letter = parts[-1]  # Take the last segment
                yield f"data: {decoded_letter}\n\n"  # Send only the final decoded letter
    except Exception as e:
        print("Error:", e)
