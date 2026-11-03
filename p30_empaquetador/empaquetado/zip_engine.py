import shutil

def comprimir_proyecto(nombre_salida, ruta_carpeta):
  shutil.make_archive(nombre_salida, 'zip', ruta_carpeta)