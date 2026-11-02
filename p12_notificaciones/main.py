if __name__ == "__main__":
  from mensajeria.envio import imprimir_cabecera_urgente
  from mensajeria.formato import enviar_alerta, enviar_multicast

  print("=== SISTEMA DE NOTIFICACIONES MULTICANAL ===")
  mensaje = input("Introduce el mensaje de alerta a enviar: ")
  imprimir_cabecera_urgente()
  enviar_alerta(mensaje)
  print("-------------------------------------------")
  enviar_multicast("User1", "User2", mensaje)