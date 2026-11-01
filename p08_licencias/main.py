from sistema.argumentos import obtener_clave_desde_cli
from sistema.validacion import es_clave_correcta, cerrar_programa_si_error

if __name__ == "__main__":
  clave = obtener_clave_desde_cli()

  print("=== VALIDACIÓN DE LICENCIA CLI ===")
  print(f"[SISTEMA] Verificando clave '{clave}'...")

  if not es_clave_correcta(clave):
    cerrar_programa_si_error()

  print("Acceso concedido. Licencia activa correctamente.")