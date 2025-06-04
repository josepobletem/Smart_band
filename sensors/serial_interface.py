import serial

def read_serial_data(port="/dev/ttyUSB0", baudrate=9600):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            line = ser.readline().decode().strip()
            return int(line) if line else None
    except Exception as e:
        print(f"Error: {e}")
        return None
