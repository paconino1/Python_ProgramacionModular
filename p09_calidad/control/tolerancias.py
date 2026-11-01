import math

def esta_en_tolerancia(medida, nominal=10.0, margen=0.5):
  desviacion = math.fabs(medida - nominal)
  return desviacion <= margen