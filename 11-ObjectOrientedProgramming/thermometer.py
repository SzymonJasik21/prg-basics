import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.last_temperature = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on:
            self.last_temperature = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Thermometer is off. Turn it on to measure.")

    def display_temperature(self):
        if not self.is_on:
            print("Thermometer is off.")
            return

        if self.last_temperature is None:
            print("No measurement taken yet.")
            return

        message = f"Temperature: {self.last_temperature}C"
        
        if self.last_temperature >= 41.0:
            message += " (CRITICAL TEMPERATURE!!)"
        elif self.last_temperature >= 37.0:
            message += " (fever)"
            
        print(message)