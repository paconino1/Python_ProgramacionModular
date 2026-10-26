from os import path
import os

def existe_archivo(ruta):
  ruta = os.path.join("..", ruta)
  return path.isfile(ruta)