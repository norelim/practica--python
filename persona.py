from datetime import datetime
from dateutil.relativedelta import relativedelta

class Persona:
    def fecha_nac(fechaNac):
        fecha_nacimiento = datetime.strptime(fechaNac, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        #print(f"{edad.years}")

       # print(f"{edad.years} años")


