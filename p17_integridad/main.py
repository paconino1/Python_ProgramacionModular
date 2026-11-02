if __name__ == "__main__":
  from verificador.estado import es_fichero_valido
  from verificador.proceso import simular_hash_archivo

  print("=== VERIFICADOR DE INTEGRIDAD DE ARCHIVOS ===")
  archivo = input("Nombre del archivo de configuración: ")

  print("[SISTEMA] Verificando existencia en almacenamiento... ")
  if es_fichero_valido(archivo):
    print("OK")
    checksum = simular_hash_archivo(archivo)
    print(f"Fichero correcto. Checksum: {checksum}")
  else:
    print("ERROR | El archivo no existe o no es un fichero válido.")
