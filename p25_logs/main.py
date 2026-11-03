if __name__ == "__main__":
  from auditor.os_info import obtener_nombre_so
  from auditor.trazabilidad import imprimir_linea_separadora

  print("=== AUDITORÍA DEL SISTEMA ===")
  print("[SISTEMA] Consultando núcleo del sistema operativo...")
  print(f"Plataforma detectada: {obtener_nombre_so()}")
  imprimir_linea_separadora()