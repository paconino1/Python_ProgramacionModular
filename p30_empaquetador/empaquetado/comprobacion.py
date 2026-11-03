import os

def es_directorio_valido(ruta):
  if os.path.exists(ruta) and os.path.isdir(ruta):
    return True
  else:
    return False