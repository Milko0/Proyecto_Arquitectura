import random
import time

class Arduino:
    def __init__(self):
        # Almacenar el tiempo inicial
        self.start_time = time.time()

    def read_arduino_data(self):
        co2_value = round(random.uniform(150, 170), 2)
        temperature_value = round(random.uniform(29.0, 32.0), 2)
        humidity_value = round(random.uniform(58.0, 65.0), 2)
        timestamp = time.time() - self.start_time  # Tiempo desde el inicio en segundos
        return co2_value, temperature_value, humidity_value, round(timestamp, 2)
