if __name__ == "__main__":
  from dispensador.generador import obtener_siguiente_turno
  from dispensador.reloj_turno import obtener_hora_solicitud

  numero_turno = 0

  print("=== DISPENSADOR AUTOMÁTICO DE TURNOS ===")
  while True:
    input("Presiona [ENTER] para emitir ticket: ")
    numero_turno = obtener_siguiente_turno(numero_turno)
    hora_solicitud = obtener_hora_solicitud()
    print(f"Ticket #{numero_turno} emitido a las {hora_solicitud}")
