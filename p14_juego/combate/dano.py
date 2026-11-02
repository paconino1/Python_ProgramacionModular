def calcular_dano_neto(ataque: int, defensa: int) -> int:
  return max(1, ataque - defensa)
