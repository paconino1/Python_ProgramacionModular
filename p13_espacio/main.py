if __name__ == "__main__":
  from disco.explorador import construir_ruta, obtener_directorio_actual
  from disco.limpieza import es_archivo_temporal

  print("=== ORGANIZADOR Y LIMPIEZA DE DISCO ===")
  nombre_archivo = input("Introduce el nombre del archivo a comprobar: ")
  directorio_actual = obtener_directorio_actual()
  ruta_completa = construir_ruta(directorio_actual, nombre_archivo)
  es_temporal = es_archivo_temporal(nombre_archivo)

  print(f"Ruta completa: {ruta_completa}")
  print(f"¿Es archivo temporal borrable?: {es_temporal}")
