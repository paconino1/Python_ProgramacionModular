if __name__ == "__main__":
    from sorteos.azar import seleccionar_premio_azar
    from sorteos.premios import calcular_descuento_ganado

    print("=== TÓMBOLA DIGITAL DE PROMOCIONES ===")
    nombre = input("Introduce el nombre del cliente: ")
    print("[SISTEMA] Girando la ruleta de premios...")

    categoria = seleccionar_premio_azar("ORO", "PLATA", "BRONCE")
    descuento = calcular_descuento_ganado(categoria)

    print(f"¡Enhorabuena {nombre}! Categoria obtenida: {categoria} ({descuento}% de descuento).")
