if __name__ == "__main__":
  from algoritmos.base import es_lote_completado
  from algoritmos.proceso import imprimir_unidad_procesada

  print("=== CONTROL RECURSIVO DE EMPAQUETADO ===")
  unidades = int (input("Unidades totales del lote a procesar: "))

  if unidades <= 0:
    print("Error: El lote debe contener al menos una unidad.")
  else:
    while not es_lote_completado(unidades):
      print(imprimir_unidad_procesada(unidades))
      unidades -= 1
    print("Estado: Lote Finalizado")