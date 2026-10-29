import math

def calcular_cuota_mensual(capital, interes_anual, meses):
    interes_mensual = (interes_anual / 100) / 12
    if interes_mensual == 0:
        return capital / meses

    cuota = capital * (interes_mensual * math.pow(1 + interes_mensual, meses)) / (math.pow(1 + interes_mensual, meses) - 1)
    return cuota