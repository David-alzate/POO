import psycopg2
from usuario import *

# Clase para realizar el login que hereda contraseña y id de usuario
class login(usuario):
    def __init__(self,password, id):
        super().__init__(password, id)
    

# Método para iniciar Sesión 
    def iniciarSesion(conexion, id, password):
        # Hacemos la consulta SQL para validar que el id ingresado si exista en la base de datos
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
                usuario = cursor.fetchone()
                # Verificar que el usuario exista
                if usuario:
                    # Comprobar si la contraseña coincide
                    if password == usuario[6]:   # 5 es el índice de la columna 'contraseña' en la base de datos 
                        return True , "Inicio de sesión exitoso."
                    else:
                        mensaje = "Contraseña incorrecta."
                        return False, mensaje
                else:
                    mensaje = "El usuario no existe."
                    return False, mensaje
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
            return False

        
    def cerrarSesion(self):
        pass
        
