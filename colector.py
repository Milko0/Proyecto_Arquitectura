import serial
import sqlite3
import time

# Establish a connection to the Arduino using the specified port
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino port

# Establish a connection to the SQLite database
conn = sqlite3.connect('sensor_data.db')  # Replace 'sensor_data.db' with your desired database name

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table to store the sensor data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        co2 INTEGER,
        temperature REAL,
        humidity REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Get the start time
start_time = time.time()

# Main loop to read data from Arduino and save it in the database for 60 seconds
while time.time() - start_time <= 60:
    # Read a line of data from the Arduino
    data = ser.readline().decode().strip()
    print(f"Received data: {data}")

    # Split the data into CO2, temperature, humidity, and timestamp values
    data_parts = data.split(',')
    if len(data_parts) == 4:
        co2, temperature, humidity, timestamp = data_parts
        # Insert the data into the database
        cursor.execute('INSERT INTO sensor_data (co2, temperature, humidity, timestamp) VALUES (?, ?, ?, ?)',
                       (co2, temperature, humidity, timestamp))
        conn.commit()

        # Print the data and time for debugging
        print(f"Time: {timestamp}, CO2: {co2} ppm, Temperature: {temperature} C, Humidity: {humidity} %")
    else:
        print("Invalid data format")

# Close the serial connection and the database connection
ser.close()
conn.close()
