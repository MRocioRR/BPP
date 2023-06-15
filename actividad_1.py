### Buenas Prácticas de programación con Python

### Alumna: María del Rocío Roldán de la Rosa

### 22/05/2023


### ACTIVIDAD LECCIÓN 1 - Control de errores, pruebas y validación de datos ###


# 1. Crea una funcion que pida por pantalla un número al usuario y que  controle mediante excepciones lo siguiente:

#    a. Solo se podrá introducir numeros enteros

#    b. Si el numero es mayor de 10 lanza una excepción con raise la cual hayas creado previamente mediante ‘class 

#    Miexcepcion(Exception):’

# 2. Abre un fichero .txt y controla mediante excepciones las diferentes casuisticas para que el programa no termine de forma inesperada. 

#   Utiliza el finally para cerrar el fichero


# 1- Función para solicitar un número entero al usuario y controlar excepciones:
class MiExcepcion(Exception):
    pass


def pedir_numero():

    try:

        numero = int(input("Introduce un número entero: "))

        if numero > 10:

            raise MiExcepcion("El número ingresado es mayor que 10.")
        return numero

    except ValueError:

        print("Error: Solo se permiten números enteros.")

        return None

    except MiExcepcion as e:

        print("Error:", str(e))

        return None
    
if (pedir_numero()) is not None:
    print("El número ingresado es:", pedir_numero())
else:
    print("No se ha ingresado un número entero válido.")
    

numero_ingresado = pedir_numero()

if numero_ingresado is not None:
    print("El número ingresado es:", numero_ingresado)
else:

    print("No se ha ingresado un número entero válido.")

    

# 2 - Manejo de excepciones al abrir print(contenido)
def abrir_archivo(ejemplo):
    try:
        archivo = open(ejemplo.txt, "r")  # Abrir el archivo en modo lectura
        # Realizar operaciones con el archivo
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except PermissionError:
        print("Error: No se tienen los permisos necesarios para abrir el archivo.")
    except Exception as e:
        print("Error inesperado:", str(e))
    finally:
        if archivo:
            archivo.close()  # Cerrar el archivo en caso de que esté abierto