def es_texto_no_vacio(texto):
  texto_limpio = texto.strip()
  if texto_limpio != "":
    return True
  else:
    return False