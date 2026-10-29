from datetime import date, timedelta

def calcular_proxima_revision (dias_margen):
    fecha_actual = date.today()
    fecha_revision = fecha_actual + timedelta(days=dias_margen)
    return fecha_revision.strftime("%Y-%m-%d")
