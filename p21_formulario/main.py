if __name__ == "__main__":
  from validadores.numeros import esta_en_rango
  from validadores.texto import es_texto_no_vacio

  print("=== FORMULARIO DE REGISTRO EN LÍNEA ===")
  nombre = input("Nombre de usuario: ")
  edad = int(input("Edad: "))

  if not es_texto_no_vacio(nombre):
    print("[SISTEMA] Nombre de usuario no puede estar vacío.")
  elif esta_en_rango(edad, 18, 65):
    print(f"[SISTEMA] Validando datos... ¿Registro aceptado? {esta_en_rango(edad, 18, 65)}")
  else:
    print(f"[SISTEMA] Validando datos... ¿Registro aceptado? {esta_en_rango(edad, 18, 65)}")