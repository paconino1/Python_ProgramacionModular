if __name__ == "__main__":
  from geometria.superficies import area_rectangulo
  from geometria.triangulos import calcular_hipotenusa

  print("=== CALCULADORA TÉCNICA DE OBRAS ===")
  ancho = float(input("Ancho de la habitación (m): "))
  largo = float(input("Largo de la habitación (m): "))
  print("-------------------------------------------")

  superficie = area_rectangulo(ancho, largo)
  diagonal = calcular_hipotenusa(ancho, largo)
  print(f"Superficie a embaldosar: {superficie} m² | Diagonal estructural: {diagonal:.2f} m")
