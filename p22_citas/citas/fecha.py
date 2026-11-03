import datetime

def obtener_fecha_cita_futura(dias):
  cita = datetime.date.today() + datetime.timedelta(days=dias)
  return cita.strftime("%d/%m/%Y")