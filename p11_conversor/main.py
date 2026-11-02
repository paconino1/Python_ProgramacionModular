if __name__ == "__main__":
  from conversion.distancia import millas_a_metros
  from conversion.velocidad import nudos_a_kmh

  print("--- CONVERSOR DE NAVEGACIÓN MARÍTIMA ---")
  nudos = float(input("Introduce la velocidad de la nave (nudos): "))
  millas = float(input("Introduce la distancia a puerto (millas náuticas): "))
  print("-------------------------------------------")

  kmh = nudos_a_kmh(nudos)
  metros = millas_a_metros(millas)

  print("EQUIVALENCIA TÉCNICA:")
  print(f"Velocidad: {kmh:.2f} km/h | Distancia: {metros:.2f} metros.")