"""
Proyecto Python y Mysql
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario enn la bd
- Si elegimos login, identificara al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas

"""
from usuarios import acciones

print("""
Hola!! Bienvenido al asistente de creacion de notas
Acciones disponibles
    - registro
    - login
""")

realiza = acciones.Acciones() # Creo un objeto acciones

accion = input("¿Que quieres hacer?: ")

if accion == 'registro':
    realiza.registro()

elif accion == 'login':
    realiza.login()

