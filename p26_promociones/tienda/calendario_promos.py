from datetime import datetime

def es_mes_promocional(mes_target=11):
  if datetime.now().month == mes_target:
    return True
  else:
    return False