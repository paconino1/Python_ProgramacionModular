if __name__ == "__main__":
    from control.tolerancias import esta_en_tolerancia
    from control.estadistica import calcular_media_piezas

    print("=== CONTROL DE CALIDAD - LOTE #482 ===")
    p1 = float(input("Introduce medida de muestra 1 (mm): "))
    p2 = float(input("Introduce medida de muestra 2 (mm): "))
    p3 = float(input("Introduce medida de muestra 3 (mm): "))
    print("-------------------------------------------")
    media = calcular_media_piezas(p1, p2, p3)

    if esta_en_tolerancia(media):
        estado = "ACEPTADO"
    else:
        estado = "RECHAZADO"

    print(f"Media del lote: {media:.2f} mm -> ESTADO: {estado}")