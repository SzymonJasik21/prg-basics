def m_to_cm(n):
    return n * 100

def cm_to_m(n):
    return n / 100

def cm_to_inch(n):
    return n / 2.54

def ft_inch_to_cm(ft, inch):
    return (ft * 30.48) + (inch * 2.54)

if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'20cm = {cm_to_inch(20)}in')
    print(f'5ft 11in = {ft_inch_to_cm(5, 11)}cm')