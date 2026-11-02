if __name__ == "__main__":
  from reportes.exportar import generar_nombre_reporte
  from reportes.sumas import sumar_tres_meses

  print("=== GENERADOR DE INFORMES CONTABLES ===")
  anyo = int(input("Año fiscal: "))
  trimestre = int(input("Trimestre (1-4): "))

  ingresos_mensuales = (1800.0, 1900.0, 1900.5)
  total = sumar_tres_meses(*ingresos_mensuales)
  nombre_reporte = generar_nombre_reporte(anyo, trimestre)

  print(f"Total acumulado: {total} € | Nombre archivo: {nombre_reporte}")
