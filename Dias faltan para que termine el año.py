import os
import datetime
from datetime import date


os.system('clear')

ahora = datetime.date.today()
print("Hoy es", ahora.day, "-", ahora.month, "-", ahora.year)


print("")

fin_ano = date(2022, 12, 31)
diferencia = ((fin_ano-ahora).days)
print("Quedan " + str(diferencia) + " días para que termine el año.")


