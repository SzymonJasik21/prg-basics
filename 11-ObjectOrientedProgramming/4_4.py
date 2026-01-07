from tv4 import TV

def main():
    print("Create a TV set")
    my_tv = TV()

    print("Show TV status")
    my_tv.show_status()

    print("Turn TV on")
    my_tv.turn_on()

    print("Show TV status")
    my_tv.show_status()

    print("Display the list of available channels")
    my_tv.show_channels()

    print("Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery")
    channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(channels)

    print("Display the list of available channels")
    my_tv.show_channels()

    print("Show TV status")
    my_tv.show_status()

    print("Turn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()