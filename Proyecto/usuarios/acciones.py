import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrarte enn el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Ingresa un email: ")
        password = input("Ingresa una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f'\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}')
        else:
            print("\nNo te has registrado correctamente")
    
    def login(self):
        print("\nVale!! Identificate en el sistema...")

        try:
            email = input("Ingresa tu email: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario('' ,'', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'\nBienvenido {login[1]} te has registrado en el sistema el {login[5]}')
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Login incorrento!! Los datos no coinciden con nuestros registros')

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que quiere hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == 'crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'mostrar':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'eliminar':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'salir':
            print(f"Ok {usuario[1]}, hasta pronto!")
            exit()
        
        