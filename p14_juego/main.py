if __name__ == "__main__":
  from combate.dado import lanzar_dado_20
  from combate.dano import calcular_dano_neto

  print("=== COMBATE POR TURNOS RPG ===")
  ataque = int(input("Puntos de ataque del personaje: "))
  defensa = int(input("Puntos de defensa del monstruo: "))

  resultado_dado = lanzar_dado_20()
  print(f"[SISTEMA] Tirando dado de impacto d20... ¡Obtenido: {resultado_dado}!")

  dano_neto = calcular_dano_neto(ataque, defensa)
  print(f"Daño neto infligido al objetivo: {dano_neto} PV.")
