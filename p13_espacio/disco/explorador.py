import os

def obtener_directorio_actual():
  return os.getcwd()

def construir_ruta(carpeta: str, archivo: str):
  return os.path.join(carpeta, archivo)