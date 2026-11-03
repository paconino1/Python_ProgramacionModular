if __name__ == "__main__":
  from crono.medicion import obtener_marca_tiempo, diferencia_tiempo
  from crono.serie import pausa_descanso

  print("=== CRONÓMETRO DE ENTRENAMIENTO ===")
  segundos = float(input("Segundos de pausa de entrenamiento: "))
  print("[CRONO] Iniciando descanso...")

  inicio = obtener_marca_tiempo()
  pausa_descanso(segundos)
  fin = obtener_marca_tiempo()

  print(f"[CRONO] Tiempo de descanso completado: {diferencia_tiempo(inicio, fin)} segundos.")