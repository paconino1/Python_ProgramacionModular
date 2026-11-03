if __name__ == "__main__":
  from empaquetado.comprobacion import es_directorio_valido
  from empaquetado.zip_engine import comprimir_proyecto

  print("=== EMPAQUETADOR DE PROYECTOS ===")
  ruta_carpeta = input("Ingrese la ruta de la carpeta a empaquetar: ")
  nombre_salida = input("Ingrese el nombre del archivo de salida (sin extensión): ")

  if es_directorio_valido(ruta_carpeta):
    comprimir_proyecto(nombre_salida, ruta_carpeta)
    print("[SISTEMA] Proyecto empaquetado con éxito.")
  else:
    print("[SISTEMA] La ruta ingresada no es válida o no existe.")