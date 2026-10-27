from red.ping import comprobar_host as ch
from red.auditoria import medir_latencia_simulada as lat

if __name__ == "__main__":
  print ("=== AUDITORÍA DE RED Y SERVIDORES ===")
  ip_o_dominio = input("Introduce el dominio o servidor a comprobar: ")
  print(f"[SISTEMA] Ejecutando diagnóstico de red sobre '{ip_o_dominio}'...")

  if ch(ip_o_dominio):
    latencia = lat()
    print(f"Resultado: Servidor ONLINE (Respuesta en {latencia} ms).")
  else:
    print("Resultado: Servidor OFFLINE (No hay respuesta).")