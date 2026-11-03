if __name__ == "__main__":
  from logistica.peso import redondear_peso_superior
  from logistica.precio import calcular_tarifa_envio

  print("=== TARIFICADOR DE ENVÍOS EXPRESS ===")
  peso = float(input("Peso del paquete en báscula (kg): "))
  print("[SISTEMA] Redondeando tramo al kilo superior...")
  peso_redondeado = redondear_peso_superior(peso)
  tarifa = calcular_tarifa_envio(peso_redondeado)
  print(f"Peso facturable: {peso_redondeado} kg | Coste total del envío: {tarifa:.2f} €")