from datetime import timedelta, datetime

def obtener_hora_expiracion(minutos=5):
  hora_actual = datetime.now()
  hora_expiracion = datetime.strftime(hora_actual + timedelta(minutes=minutos), "%H:%M:%S")
  return hora_expiracion