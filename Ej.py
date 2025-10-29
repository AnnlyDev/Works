

from datetime import datetime

def calculator(Fecha_de_Nacimiento):
    actual = date.today()
    edad =actual.year - Fecha_de_Nacimiento.year
    edad -=((actual.month, actual.day) < (Fecha_de_Nacimiento.month, Fecha_de_Nacimiento.day))

    return edad

    print(calculator(data(2007, 1, 19)))