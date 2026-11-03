if __name__ == "__main__":
  from perfil.ficha import mostrar_ficha
  from perfil.opciones import obtener_estado_usuario

  print("=== GESTOR DE FICHAS DE RECURSOS HUMANOS ===")
  nombre = input("Nombre del empleado: ")
  departamento = input("Departamento: ")
  print("-------------------------------------------")

  mostrar_ficha(nombre, departamento)
  print(f"Usuario {nombre} estado: {obtener_estado_usuario()}")