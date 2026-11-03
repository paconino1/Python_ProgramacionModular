if __name__ == "__main__":
  from citas.fecha import obtener_fecha_cita_futura
  from citas.identificador import generar_codigo_cita

  print("=== SISTEMA DE CITA PREVIA BANCARIA ===")
  dias = int(input("¿Para dentro de cuántos días desea la cita?: "))
  print("-------------------------------------------")
  
  print(f"Cita confirmada para el {obtener_fecha_cita_futura(dias)}.")
  print(f"Localizador de reserva: {generar_codigo_cita()}.")