'''Author: Gerardo Gabriel Aquino Cano... Curso de Python - 29/06/2026 - Menú principal del programa para registrar productos. '''

import conexiondb as db
import utilidades as ut

def registrar_productos(): #Esta función entra en un bucle para registrar productos y guardarlos en la base de datos.
    while True:
        producto = ut.producto() #Funcion que solicita, verifica el texto y devuelve el nombre del producto.
        precio = ut.precio() #Funcion que solicita, verifica si es un valor numéricoy devuelve el precio del producto.
        categoria = ut.categoria()
        cantidad = ut.cantidad() #Funcion que solicita, verifica el valor y devuelve la cantidad del producto.
        descripcion = ut.descripcion_producto()
        db.insertar_registros(producto, categoria, precio, descripcion, cantidad) #Aquí registramos los datos en la base de datos usando una función de la librería conexiondb.py
        continuar= input("\n¿Desea registrar otro producto? (S/N): \n\n").lower() #Verificamos si el usuario desea continuar y si no, volvemos al menú principal.
        if continuar != "s":
            break

def productos_registrados(): #Esta función muestra los registros de la base de datos.
    if db.hay_registros(): #Verificamos si hay registros en la base de datos.
        db.mostrar_registros() #Si hay registros, los mostramos.
    else: #Si no hay registros, mostramos un mensaje de error.
        print(f"\n {'-'*10} [ERROR!] No hay productos registrados. {'-'*10} \n")

def verificar_producto(): #Esta es una función de verificación y busqueda de productos registrados. 
    if db.hay_registros(): #Verificamos si hay registros en la base de datos.
        print(f"\t\n {'='*20} Buscar producto por ID {'='*20}\n")
        db.buscar_registro_por_id()#Invocamos a la función para buscar un registro por su ID.
    else: #Si no hay registros, mostramos un mensaje de error.
        print(f"\n {'-'*10} [ERROR!] No hay productos registrados. {'-'*10} \n")

def eliminar_producto(): #Esta es una función de verificación y eliminación de productos registrados.
    if db.hay_registros(): #Verificamos si hay registros en la base de datos.
        print(f"\t\n {'='*20} Eliminar producto {'='*20}\n")
        db.eliminar_registro_de_la_tabla() #Invocamos a la función para eliminar un registro de la tabla.
    else: #Si no hay registros, mostramos un mensaje de error.
        print(f"\n {'-'*10} [ERROR!] No hay productos registrados. {'-'*10} \n")

def actualizar_producto(): #El usuario actualiza los datos del producto registrado usando esta función.
    if db.hay_registros(): #Verificamos si hay registros en la base de datos.
        print(f"\t\n {'='*15} Que producto desea modificar sus datos? {'='*15}\n")
    else: #Si no hay registros, mostramos un mensaje de error.
        print(f"\n {'-'*10} [ERROR!] No hay productos registrados. {'-'*10} \n")

def menu(): #Menú principal donde se maneja la información y los registros de los productos...
    while True:
        print(f"\t {'='*30} --- Bienvenido al menú principal  --- {'='*30}\n")
        print("1. Registrar producto.\n")
        print("2. Mostrar lista de productos.\n")
        print("3. Buscar producto por ID.\n")
        print("4. Eliminar producto.\n")
        print("5. Actualizar datos de un producto.\n")
        print("6. Verificar cantidad de un producto registrado.\n")
        print("7. Cerrar Programa.\n")
        opcion = input("Ingrese una opción para continuar:  \t")
        match opcion:
            case "1":
                print(f"\t\n {'='*20} Registro de productos {'='*20}\n")
                registrar_productos()#Invocamos a la función para comenzar con los registros de los productos.
            case "2":
                productos_registrados()#Invocamos a la función para mostrar los registros de los productos.
            case "3":
                verificar_producto()#Invocamos a la función para buscar un registro por su ID.
            case "4":
                eliminar_producto()#Invocamos a la función para eliminar un registro de la tabla.
            case "5":
                actualizar_producto()
            case "6":
                print("Pendiente...")
            case "7":
                print(f"\t\n {'='*20} Cerrando Programa. Que tenga un buen día!! {'='*20}\n")
                break
            case _: #Caso por defecto, volvemos al menú principal si el usuario ingresa una opción inválida.
                print(f"\t\n\n{'-'*10}[ERROR] !!OPCIÓN INVÁLIDA!! Intente nuevamente...{'-'*10}\n\n")

menu() #Llamamos a la función y empezamos con esta fiesta-! digo... empezamos con el programa.