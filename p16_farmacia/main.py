if __name__ == "__main__":
  from medicina.dosis import sumar_fraccion_dosis
  from medicina.paciente import es_dosis_pediatrica

  print("=== ASISTENTE DE DOSIFICACIÓN FARMACÉUTICA ===")
  edad = int(input("Edad del paciente: "))
  f1_n = int(input("Numerador toma 1: "))
  f1_d = int(input("Denominador toma 1: "))
  f2_n = int(input("Numerador toma 2: "))
  f2_d = int(input("Denominador toma 2: "))

  dosis_total = sumar_fraccion_dosis(f1_n, f1_d, f2_n, f2_d)
  dosis_pediatrica = es_dosis_pediatrica(edad)
  print(f"Dosis total acumulada: {dosis_total} de ampolla | Paciente pediátrico: {dosis_pediatrica}")
