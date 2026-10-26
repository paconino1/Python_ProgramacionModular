from parking import tarifas as t, ticket as tk

if __name__ == "__main__":
  print("--- PARQUÍMETRO MUNICIPAL ---")
  minutos = int(input("¿Cuántos minutos desea estacionar?: "))
  print("-----------------------------------")
  print("TICKET DE ESTACIONAMIENTO ZONA AZUL")
  print("Fecha y hora de emisión: ", tk.obtener_fecha_hora_actual())
  print(f"Tiempo abonado: {minutos} minutos")
  print("IMPORTE TOTAL: ", tk.formatear_moneda(t.calcular_precio_estancia(minutos)))
  print("-----------------------------------")