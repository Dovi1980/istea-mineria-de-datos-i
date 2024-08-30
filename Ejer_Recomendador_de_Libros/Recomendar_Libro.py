import csv
from Clear import limpiar
from pausa import pausa

#---------------------------------------------------------------------------------------------------
# --- Clase Libro ---
class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self): # Metodo para definir como se mostrara la informacion de cada libro
        return f"{self.titulo} por {self.autor} - {self.genero} - Puntuación: {self.puntuacion}"

#---------------------------------------------------------------------------------------------------
# --- Funciones ---

# Funcion para realizar la carga de informacion que contenga el csv en una lista
def leer_libros_desde_csv(archivo):
    lista_libros = []
    with open(archivo, newline="", encoding="utf-8") as archivo_csv:
        listado_cargado = csv.DictReader(archivo_csv)
        for fila in listado_cargado:
            libro = Libro(fila["titulo"], fila["autor"], fila["genero"], float(fila["puntuacion"]))
            lista_libros.append(libro)
    return lista_libros

# Op 1: Funcion agregar titulos al csv
def agregar_libro_al_csv():
    titulo = input("Ingrese el titulo del libro: ").title()
    autor =  input("Ingrese el autor: ").title()
    genero =  input("Ingrese el genero del libro: ").title()
    puntuacion = input("Ingrese la puntuacion del libro: ")
    archivo = 'Listado_Libros.csv'  
    with open(archivo, 'a', newline='', encoding='utf-8') as archivo_csv:
        escritura = csv.writer(archivo_csv)
        escritura.writerow([titulo, autor, genero, float(puntuacion)])
    return print(f"\nCarga exitosa...")

# Op 2: Funcion para buscar libros por genero
def buscar_por_genero(lista_libros, genero):
    return [libro.titulo +" escrito por "+ libro.autor for libro in lista_libros if libro.genero == genero] # Devuelvo un listado de los libros con el genero especificado

# Op 3: Funcion para recomendar libros por genero
def recomendacion(lista_libros, genero):
    recomendaciones = [libro for libro in lista_libros if libro.genero == genero] # Creo una lista segun el genero seleccionado
    recomendaciones.sort(key=lambda x: x.puntuacion, reverse=True) # Ordeno el listado de recomendados por mejor puntuacion
    return recomendaciones[0] # Devuelvo el libro con mejor puntuacion

#---------------------------------------------------------------------------------------------------
#----- Menu -----
def menu(lista_libros):
    print()
    y = "S"
    while y == "S" or y != "N":
        limpiar()
        print("""
    ######################################################
    #|--------------------------------------------------|#
    #|------->>>  Libreria "La Página Oculta" <<<-------|#
    #|--------------------------------------------------|#     
    ###################################################### 
    #|--------------------------------------------------|#
    #|------>>>         MENU PRINCIPAL         <<<------|#
    #|------>>>        Elija una opción        <<<------|#
    #|------>>>   1 > Agregar Nuevo Título     <<<------|#
    #|------>>>   2 > Busqueda por Género      <<<------|#
    #|------>>>   3 > Recomendación            <<<------|#
    #|------>>>         S > Salir              <<<------|#              
    #|--------------------------------------------------|#
    ######################################################
    
    """)
        op=input("\tIngrese una opción: ").upper()
        match (op):
            case  "1":
                agregar_libro_al_csv()
            case  "2":
                genero = input("Ingrese genero del libro: ").capitalize()
                print(f"\nLibros disponibles en el género {genero}:")
                print()
                for titulo in buscar_por_genero(lista_libros, genero):
                 print(titulo)
            case  "3":
                genero = input("Ingrese genero del libro: ").capitalize()
                print(f"\nRecomendaciones para el género {genero}:")
                print()
                print(recomendacion(lista_libros, genero))
            case  "S":
                print("\n\tHasta pronto...")
                return
            case _:
                print()
                print("\tIngreso Invalido...")
                pausa()
        y = str(input("\n\n\tDesea Continuar? - (S/N): ")).upper()
        while y != "S" and y !="N":
            print("\tRespuesta Incorrecta...")       
            y = str(input("\tDesea Continuar? - (S/N): ")).upper()
        limpiar()
    return

#---------------------------------------------------------------------------------------------------
#--- MAIN ---

# Cargar los titulos desde el archivo CSV
archivo = 'Listado_Libros.csv'  
listado = leer_libros_desde_csv(archivo)

menu(listado)

print("\nFIN DEL PROGRAMA.\n") 

