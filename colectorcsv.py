import serial
import csv
import time

# Establish a connection to the Arduino using the specified port
# Replace 'COM3' with your Arduino port
ser = serial.Serial('COM3', 9600)

# Open the CSV file in write mode
# Replace 'results.csv' with your desired filename


# Global variable to track the incremental ID


def count_csv_lines(file_path):
    line_count = 0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for _ in reader:
            line_count += 1

    return line_count


def save_data_to_csv(id_ubi, co2, temperature, humidity, timestamp):

    csv_file = open('results.csv', mode='a', newline='')
    writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        writer.writerow(
            ['ID', 'id_ubi', 'CO2', 'Temperature', 'Humidity', 'Timestamp'])

    # Write the data to the CSV file
    else:
        test = count_csv_lines("results.csv")
        writer.writerow(
            [str(test), f'{id_ubi}', float(co2), float(temperature), float(humidity), str(timestamp)])

    # Write the header row in the CSV file
    csv_file.close()


# Get the start time
start_time = time.time()

# Main loop to read data from Arduino and save it in the CSV file for 60 seconds


def extract_last_element(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        last_element = None
        for row in reader:
            if len(row) >= 2:
                last_element = row[1]  # 2nd column (index 1)
        if (last_element == None):
            return 1
        return last_element


id_ubi = extract_last_element("results.csv")

while time.time() - start_time <= 60:
    # Read a line of data from the Arduino
    data = ser.readline().decode().strip()
    print(f"Received data: {data}")

    # Split the data into CO2, temperature, humidity, and timestamp values
    data_parts = data.split(',')
    if len(data_parts) == 4:
        co2, temperature, humidity, timestamp = data_parts
        timestamp = str(round((int(timestamp)/1000), 2))

        # Call the save_data_to_csv function to save the data
        last_ubi = int(id_ubi)+1
        save_data_to_csv(f"{str(last_ubi)}", co2,
                         temperature, humidity, timestamp)

        # Print the data and time for debugging
        print(
            f"Time: {timestamp}, CO2: {co2} ppm, Temperature: {temperature} C, Humidity: {humidity} %")
    else:
        print("Invalid data format")

# Close the serial connection and the CSV file
ser.close()
