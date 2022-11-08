# importamos el modulo time
import time

# Variables para obtener hora y minutos

hor = time.strftime('%H')
min = time.strftime('%M')

# comprobamos la hora

if int(hor) >= 19:
    print("Es hora de ir a casa")

else:
    print("Quedan {} horas y {} minutos para ir a casa ".format(18- int(hor), 59- int(min)))
