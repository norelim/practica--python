from datetime import datetime
from dateutil.relativedelta import relativedelta

class Persona:
   def calcular_edad(fecha_nac):
        fecha_nacimiento_datetime = datetime.strptime(fecha_nac, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento_datetime)
        return edad.years
       # print(f"{edad.years}")

       # print(f"{edad.years} años")


