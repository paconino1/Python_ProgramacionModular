import time, random

def medir_latencia_simulada():
  inicio = time.time()
  time.sleep(random.uniform(0.05, 0.2))
  fin = time.time()
  latencia = round(fin - inicio, 1) * 1000

  return latencia