def get_state(temp):
    if temp <= 0:
        return "Solid"
    elif temp > 0 & temp < 100:
        return "Liquid"
    else:
        return "Gas"
