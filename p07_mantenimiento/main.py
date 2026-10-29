if __name__ == "__main__":
  from datetime import date
  from agenda.calendario import obtener_vista_mes
  from agenda.citas import calcular_proxima_revision

  print("=== AGENDA TÉCNICA DE MANTENIMIENTO ===")
  dias_margen = int(input("¿En cuántos días corresponde la próxima revisión?: "))
  fecha_revision = calcular_proxima_revision(dias_margen)
  print(f"[SISTEMA] Próxima revisión técnica fijada para: {fecha_revision}")
  print()
  print(obtener_vista_mes(date.today().year, date.today().month))