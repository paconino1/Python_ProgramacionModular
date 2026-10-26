import shutil as s

def crear_copia_zip(nombre_zip, carpeta_origen):
  try:
    s.make_archive(nombre_zip, 'zip', carpeta_origen)
    return True
  except Exception as e:
    print(f"Error al crear el archivo ZIP: {e}")
    return False