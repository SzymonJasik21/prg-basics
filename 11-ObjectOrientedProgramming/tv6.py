class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def show_status(self):
        if self.is_on:
            status_str = f"TV is on, channel {self.channel_no}"
            if 1 <= self.channel_no <= len(self.channels):
                status_str += f" ({self.channels[self.channel_no - 1]})"
            status_str += f", volume {self.volume}"
            print(status_str)
        else:
            print("TV is off")