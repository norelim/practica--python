from datetime import datetime
from dateutil.relativedelta import relativedelta

class Persona:
    def fecha_nac():
        fecha_nacimiento = datetime.strptime("19/6/1978", "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        print(f"{edad.years} años")