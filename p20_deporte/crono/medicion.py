import time

def obtener_marca_tiempo():
    return time.time()

def diferencia_tiempo(inicio, fin):
    segundos = fin - inicio
    return round(segundos, 1)