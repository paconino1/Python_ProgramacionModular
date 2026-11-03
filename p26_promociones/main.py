if __name__ == "__main__":
  from tienda.calendario_promos import es_mes_promocional, datetime
  from tienda.ofertas import aplicar_rebaja_temporada
  import locale

  # Configuramos la localización para que aparezcan los nombres de los meses en español
  locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

  print("=== TICKET DE VENTA COMERCIAL ===")
  precio = float(input("Precio original del artículo (€): "))
  print("[SISTEMA] Evaluando campaña del mes actual...")
  if es_mes_promocional():
    print(f"¡Descuento promocional de {datetime.now().strftime('%B')} aplicado!")
    precio_final = aplicar_rebaja_temporada(precio)
    print(f"Precio final a cobrar: {precio_final:.2f} €")
  else:
    print("No hay promociones activas este mes.")
    print(f"Precio final a cobrar: {precio:.2f} €")