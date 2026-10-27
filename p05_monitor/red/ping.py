import os, subprocess

def comprobar_host(ip_o_dominio):
  if os.name == "nt":
    parametro = "-n"
  elif os.name == "posix":
    parametro = "-c"

  resultado_ping = subprocess.run(["ping", parametro, "1", ip_o_dominio], capture_output=True)
  if resultado_ping.returncode == 0:
    return True
  else:
    return False