import shutil as s

def crear_copia_zip(nombre_zip, carpeta_origen):
  s.make_archive(nombre_zip, 'zip', carpeta_origen)
  return True 