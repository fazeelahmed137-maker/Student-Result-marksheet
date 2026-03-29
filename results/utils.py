def calculate_grade(percentage):
    if percentage < 40:
        return "RA"
    elif 40 <= percentage <= 49:
        return "C"
    elif 50 <= percentage <= 59:
        return "B"
    elif 60 <= percentage <= 74:
        return "A"
    elif 75 <= percentage <= 89:
        return "D"
    else:
        return "E"
