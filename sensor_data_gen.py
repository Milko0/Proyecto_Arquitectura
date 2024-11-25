import csv
import random

def generate_sensor_data(num_locations, measurements_per_location, output_file, variation_factor=0.5):
    """

    :param num_locations: Número de ubicaciones.
    :param measurements_per_location: Número de mediciones por ubicación.
    :param output_file: Nombre del archivo de salida en formato CSV.
    :param variation_factor: Factor para controlar la suavidad de las variaciones (0.1 = muy suave, 1.0 = variaciones normales).
    """
    header = ['ID', 'id_ubi', 'CO2', 'Temperature', 'Humidity', 'Timestamp']
    data = []
    record_id = 1  

    for location_id in range(1, num_locations + 1):
        timestamp = 1.04  # Reinicia el timestamp para cada ubicación
        
        # Valores iniciales para CO2, Temperatura y Humedad
        co2 = random.randint(150, 170)
        temperature = round(random.uniform(29.0, 32.0), 1)
        humidity = round(random.uniform(58.0, 65.0), 1)

        for _ in range(measurements_per_location):
            # Variaciones controladas por el factor
            co2 += round(random.uniform(-1, 1) * variation_factor, 1)
            temperature += round(random.uniform(-0.2, 0.2) * variation_factor, 1)
            humidity += round(random.uniform(-0.3, 0.3) * variation_factor, 1)


            co2 = max(140, min(co2, 180))  # CO2 entre 140 y 180
            temperature = max(28.0, min(temperature, 33.0))  # Temperatura entre 28.0°C y 33.0°C
            humidity = max(55.0, min(humidity, 70.0))  # Humedad entre 55% y 70%


            data.append([
                record_id,
                location_id,
                round(co2, 2),
                round(temperature, 2),
                round(humidity, 2),
                round(timestamp, 2)
            ])
            record_id += 1
            timestamp += 2.02  # Incremento de tiempo para cada medición


    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) 
        writer.writerows(data)  

    print(f"Archivo '{output_file}' generado con éxito con {record_id - 1} registros.")


generate_sensor_data(
    num_locations=5,
    measurements_per_location=30,
    output_file='result_sensor_data.csv',
    variation_factor=0.3  
)
