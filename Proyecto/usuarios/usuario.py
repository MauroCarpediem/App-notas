
import datetime
import hashlib
import usuarios.conexion as conexion

conect = conexion.conectar()
database = conect[0]
cursor = conect[1]

class Usuario:

    def __init__(self,nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    # Getters (creacion pendiente)

    # Setters (creacion pendiente)

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) # El metodo update necesita un parametro en bytes por ende es necesario tansformar self.password em bytes con el metodo .encode('utf8')

        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    

    def identificar(self):
        # Consulta para verificar si el email y la password existen
        sql = "SELECT * FROM usuario WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)

        result = cursor.fetchone()
        return result

