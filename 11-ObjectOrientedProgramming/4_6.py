from tv6 import TV

def main():
    my_tv = TV()
    my_tv.turn_on()
    
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"])
    
    my_tv.set_channel(4)
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.show_status()
    
    my_tv.decrease_volume()
    my_tv.show_status()
    
    for _ in range(12):
        my_tv.increase_volume()
    print("Volume increased to max (10):")
    my_tv.show_status()

    for _ in range(15):
        my_tv.decrease_volume()
    print("Volume decreased to min (0):")
    my_tv.show_status()

if __name__ == "__main__":
    main()