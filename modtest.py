import serial
import time

# Set up the serial connection
ser = serial.Serial(
    port='COM7',       # Replace 'COMx' with the appropriate COM port (e.g., 'COM3' for Windows, '/dev/ttyUSB0' for Linux)
    baudrate=19200,    # Set baud rate to 19200
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1          # Timeout for read operations
)

# Function to send a single character to the Modbus device
def send_single_character(char):
    if ser.is_open:
        ser.write(char.encode())  # Send the character as bytes
        print(f"Sent: {char}")
    else:
        print("Serial port is not open")

# Example usage
try:
    ser.open()  # Open the serial port if not already open
except Exception as e:
    print(f"Error opening serial port: {e}")

# Run in a continuous loop
try:
    while True:
        send_single_character('ABC')  # Replace 'A' with the character you want to send
        time.sleep(2)  # Wait for 1 second before sending the next character (adjust the delay as needed)

except KeyboardInterrupt:
    print("Loop interrupted by user")

finally:
    # Close the serial connection
    ser.close()
    print("Serial port closed")
