from fichaje.reloj import obtener_hora_actual, calcular_minutos_transcurridos
from fichaje.validar import es_horario_laboral

if __name__ == "__main__":
  hora_actual = obtener_hora_actual()
  es_puntual = es_horario_laboral(hora_actual)

  print("=== TERMINAL AUTO-FICHAJE DE EMPLEADOS ===")
  print("[SISTEMA] Registrando fichaje de entrada...")
  print(f"Hora oficial capturada: {hora_actual}")
  if es_puntual:
    print("[SISTEMA] Estado de entrada: PUNTUAL (Llegada antes de las 09:00)")
  else:
    print("[SISTEMA] Estado de entrada: TARDE (Llegada después de las 09:00)")
  print("-------------------------------------------")
  print("Introduce tu hora prevista de salida (HH:MM): ", end="")
  hora_salida = input()
  minutos_trabajados = calcular_minutos_transcurridos(hora_actual, hora_salida)
  print(f"Duración total de tu jornada de hoy: {minutos_trabajados} minutos.")