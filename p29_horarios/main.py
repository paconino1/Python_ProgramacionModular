if __name__ == "__main__":
  from tiempo_comercial.hora_local import obtener_dia_semana_actual, obtener_hora_24h_actual
  from tiempo_comercial.apertura import es_dia_laborable

  print("=== COMUNICADOR DE HORARIO ATENCIÓN AL CLIENTE ===")
  print("[SISTEMA] Consultando reloj del servidor...")
  dia = obtener_dia_semana_actual()
  hora = obtener_hora_24h_actual()

  if es_dia_laborable(dia) and (hora >= 9 and hora <= 20):
    print("Estado actual de la oficina: ABIERTO (Horario comercial activo).")
  else:
    print("Estado actual de la oficina: CERRADO (Horario comercial inactivo).")