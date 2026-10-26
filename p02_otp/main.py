from seguridad import expiracion as e, aleatorio as a

if __name__ == "__main__":
  print("=== SERVIDOR DE AUTENTICACIÓN OTP ===")
  input("Presiona [ENTER] para solicitar un código SMS...")
  print("-------------------------------------------")
  print("Tu código de verificación es:", a.generar_codigo_numerico())
  print(f"Atención: Este código caducará a las {e.obtener_hora_expiracion()} (Válido durante 5 minutos).")