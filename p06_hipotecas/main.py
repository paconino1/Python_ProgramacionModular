from finanzas.calculos import calcular_cuota_mensual
from finanzas.formato import mostrar_resumen_prestamo

print("--- SIMULADOR DE PRÉSTAMOS BANCARIOS ---")
capital = float(input("Introduce el capital solicitado (€): "))
interes_anual = float(input("Introduce el porcentaje de interés anual (%): "))
meses = int(input("Introduce los meses de amortización (ej. 300): "))
print("-------------------------------------------")

cuota = calcular_cuota_mensual(capital, interes_anual, meses)
mostrar_resumen_prestamo(capital, cuota)