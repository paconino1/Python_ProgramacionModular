from datetime import datetime

def obtener_fecha_hora_actual():
  fecha_hora_actual = datetime.now().strftime("%Y-%m-%d a las %H:%M:%S")
  return fecha_hora_actual

def formatear_moneda(importe):
  return f"{importe:.2f} €"