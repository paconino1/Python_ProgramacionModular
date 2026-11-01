import sys

def es_clave_correcta(clave):
  if clave == "ADM-1234-OK":
    return True
  return False

def cerrar_programa_si_error():
  print("Error: clave incorrecta. El programa se cerrará.", file=sys.stderr)
  sys.exit(1)