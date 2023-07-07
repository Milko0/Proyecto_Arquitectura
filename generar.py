import csv
import random
import time

def count_csv_lines(file_path):
    line_count = 0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for _ in reader:
            line_count += 1

    return line_count


def save_data_to_csv(id_ubi, co2, temperature, humidity, timestamp):

    csv_file = open('results_test.csv', mode='a', newline='')
    writer = csv.writer(csv_file)

    if csv_file.tell() == 0:
        writer.writerow(
            ['ID', 'id_ubi', 'CO2', 'Temperature', 'Humidity', 'Timestamp'])

    # Write the data to the CSV file
    else:
        test = count_csv_lines("results_test.csv")
        writer.writerow(
            [str(test), f'{id_ubi}', float(co2), float(temperature), float(humidity), str(timestamp)])

    # Write the header row in the CSV file
    csv_file.close()
start_time = time.time()
time_id=0
i=1
while time.time() - start_time <= 60:
    id_ubi=48
    co2=round(random.uniform(110, 120),2)
    temperature=round(random.uniform(20, 30),2)
    humidity=round(random.uniform(50, 60),2)
    lista_car=[id_ubi,co2,temperature,humidity,str(time_id)]
    print(f"valor {i}:",lista_car)
    time_id+=2
    i+=1
    save_data_to_csv(id_ubi,co2,temperature,humidity,str(time_id))
    time.sleep(2)