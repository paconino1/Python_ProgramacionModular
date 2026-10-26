from datetime import datetime

def obtener_hora_actual():
    hora_actual = datetime.now().strftime("%H:%M")
    return hora_actual

def calcular_minutos_transcurridos(inicio, fin):
    formato_hora = "%H:%M"
    inicio = datetime.strptime(inicio, formato_hora)
    fin = datetime.strptime(fin, formato_hora)
    minutos_transcurridos = (fin - inicio).total_seconds() / 60
    return minutos_transcurridos