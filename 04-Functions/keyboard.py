def input_string(message):
    data = input(message)
    return data

def input_integer(message):
    data = input(message)
    return int(data)

def input_real(message):
    data = input(message)
    return float(data)

def input_boolean(message):
    data = input(message)
    return data.lower() == 'y'