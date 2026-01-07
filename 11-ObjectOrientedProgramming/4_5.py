from tv5 import TV

def main():
    my_tv = TV()
    my_tv.turn_on()
    
    stations = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"]
    my_tv.set_channels(stations)
    
    my_tv.set_channel(1)
    my_tv.show_status()
    
    my_tv.set_channel(4)
    my_tv.show_status()
    
    my_tv.set_channel(7)
    my_tv.show_status()
    
    my_tv.set_channel(8)
    my_tv.show_status()
    
    my_tv.set_channel(2)
    my_tv.show_status()

if __name__ == "__main__":
    main()