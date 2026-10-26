import almacenamiento.archivos as a, almacenamiento.compresion as c

if __name__ == "__main__":
  print("=== GESTOR DE COPIAS DE SEGURIDAD ===")
  
  if a.existe_archivo("main.py"):
    print("[SISTEMA] Verificando integridad del proyecto... OK")
  else:
    print("[SISTEMA] Verificando integridad del proyecto... ERROR")

  nombre_archivo = input("Introduce el nombre para el archivo de respaldo: ")

  if c.crear_copia_zip(nombre_archivo, "."):
    print(f"[SISTEMA] Creando archivo '{nombre_archivo}.zip'...")
  else:
    print("[SISTEMA] Error al crear el archivo ZIP.")

  print("Proceso finalizado con éxito.")