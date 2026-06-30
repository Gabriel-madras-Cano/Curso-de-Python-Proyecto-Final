'''Author: Gerardo Gabriel Aquino Cano... Curso de Python - 29/06/2026 - Conexión a la base de datos '''

import sqlite3 #Importa la librería sqlite3 para trabajar con bases de datos SQLite...

def crear_conexion(): #Función para crear una base de datos de prueba...
    conexion = sqlite3.connect("productos.db")
    print("Base de datos creada con éxito...")
    conexion.close()

def crear_tabla(): #Función para crear una tabla en la base de datos...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL)
    ''')
    conexion.commit()
    conexion.close()

def insertar_registros(producto, categoria, precio, descripcion, cantidad): #Función para insertar datos en la tabla de la base de datos...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor() #Después de conectarnos con la base de datos, usamos el cursor para ejecutar comandos SQL.
    cursor.execute("INSERT INTO productos (nombre, categoria, precio, descripcion, cantidad) VALUES (?, ?, ?, ?, ?)", (producto, categoria, precio, descripcion, cantidad)) #Utilizamos las variables que guardamos de la función en el index.py
    conexion.commit() #Guardamos los cambios y registramos el nuevo producto en la base de datos.
    conexion.close()


def mostrar_registros(): #Función para mostrar los registros de la tabla de la base de datos...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos") #Despues de establecer conexión con la base de datos, usamos el cursor para mostrar los registros de la tabla.
    registros = cursor.fetchall()
    print(f"\t\n {'='*20} Productos Registrados {'='*20}\n")
    for registro in registros:
        print(f"\n -ID: {registro[0]} \n -Nombre: {registro[1]} \n -Categoría: {registro[2]} \n -Precio: {registro[3]} \n -Descripción: {registro[4]} \n -Cantidad: {registro[5]}\n {'_'*80}\n ")
    conexion.close()

def hay_registros(): #Función para verificar si hay registros en la tabla de la base de datos...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos") #Después de establecer conexión con la base de datos, usamos el cursor para contar los registros de la tabla.
    cantidad_registros = cursor.fetchone()[0]
    conexion.close()
    return cantidad_registros > 0

def buscar_registro_por_id(): #Función para buscar un registro en la tabla de la base de datos por su ID...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    id_buscar = input("\n Ingrese el ID del producto a buscar: ") #Pedimos al usuario que ingrese el ID del producto que desea buscar...
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_buscar,))
    registro = cursor.fetchone()
    if registro:
        print(f"\n ~ID: {registro[0]} \n ~Nombre: {registro[1]} \n ~Categoría: {registro[2]} \n ~Precio: {registro[3]} \n ~Descripción: {registro[4]} \n ~Cantidad: {registro[5]}\n {'-'*80} \n")
    else:
        print(f"\n {'-'*10} [ERROR!] El producto con el ID {id_buscar} no existe. {'-'*10} \n")
    conexion.close()

def eliminar_registro_de_la_tabla(): #Función para eliminar registros de la tabla de la base de datos...
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    id_eliminar = input("Ingrese el ID del producto a eliminar: ")
    try:
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_eliminar,))
    except Exception as e:
        print(f"\n {'-'*10} [ERROR!] Ocurrió un error al eliminar el producto con el ID {id_eliminar}. Error: {e} {'-'*10} \n")
    conexion.commit()
    conexion.close()

def actualizar_productos(): #Funcion que agrega o actualiza datos sobre un producto seleccionado
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    id_buscar = input("Ingrese el ID del producto que quiera actualizar sus datos: ") #Pedimos al usuario que ingrese el ID del producto que desea buscar...
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_buscar,))
    registro = cursor.fetchone()
    if registro:
        print(f"\n ID: {registro[0]}, Nombre: {registro[1]} \n Categoría: {registro[2]} \n Precio: {registro[3]} \n Descripción: {registro[4]} \n Cantidad: {registro[5]}\n ")
    else:
        print(f"\n {'-'*10} [ERROR!] El producto con el ID {id_buscar} no existe. {'-'*10} \n")
    conexion.close()

crear_conexion() #Si la función establece conexión con la base de datos, se imprime un mensaje indicando que la base de datos se ha creado con éxito.
crear_tabla() #Si la función crea la tabla en la base de datos, se imprime un mensaje indicando que el registro de productos se ha creado con éxito.