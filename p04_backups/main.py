import almacenamiento.archivos as a, almacenamiento.compresion as c
from os import path

if __name__ == "__main__":
  print("=== GESTOR DE COPIAS DE SEGURIDAD ===")
  
  if a.existe_archivo("main.py"):
    print("[SISTEMA] Verificando integridad del proyecto... OK")
    nombre_archivo = input("Introduce el nombre para el archivo de respaldo: ")
  else:
    print("[SISTEMA] Verificando integridad del proyecto... ERROR")

  print(f"[SISTEMA] Creando archivo '{nombre_archivo}.zip'...")
  if c.crear_copia_zip(nombre_archivo, ".\\almacenamiento"):
    print("Proceso finalizado con éxito.")
  else:
    print("[SISTEMA] Error al crear el archivo ZIP.")