if __name__ == "__main__":
  from control_acceso.contador import sumar_asistentes
  from control_acceso.limite import supera_aforo_maximo

  print("=== CONTROL DE AFORO EN TORNO ===")
  actuales = int(input("Aforo actual dentro del local: "))
  nuevos = int(input("Personas en la puerta intentando entrar: "))
  total_asistentes = sumar_asistentes(actuales, nuevos)
  if supera_aforo_maximo(total_asistentes):
    print("BLOQUEADO: Se supera la capacidad máxima autorizada (100 pers).")
  else:
    print(f"PERMITIDO: Aforo dentro del local: {total_asistentes} pers.")