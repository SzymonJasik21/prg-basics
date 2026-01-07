class Phone:
    def __init__(self, model):
        self.model = model
        self.battery_level = 50
        self.is_powered_on = False

    def toggle_power(self):
        self.is_powered_on = not self.is_powered_on
        status = "on" if self.is_powered_on else "off"
        print(f"Phone is now {status}.")

    def charge_battery(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Charging... Battery level: {self.battery_level}%")

    def make_call(self, number):
        if self.is_powered_on and self.battery_level > 0:
            print(f"Calling {number} from my {self.model}...")
            self.battery_level -= 5
        elif not self.is_powered_on:
            print("Cannot make a call. Phone is off.")
        else:
            print("Battery empty.")

    def display_status(self):
        print("Phone Properties:")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery_level}%")
        print(f"Powered On: {self.is_powered_on}")
        print()

def main():
    my_phone = Phone("iPhone 15")

    my_phone.display_status()
    
    my_phone.toggle_power()
    my_phone.charge_battery(20)
    my_phone.make_call("123-456-789")
    
    print()
    my_phone.display_status()

if __name__ == "__main__":
    main()