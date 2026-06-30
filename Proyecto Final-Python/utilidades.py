'''Author: Gerardo Gabriel Aquino Cano... Curso de Python - 29/06/2026 - Algunas utilidades para el menú principal. '''

def verificar_texto(texto):
    while True:
        if((texto.strip()!="") and (len(texto) > 2) and (texto.isspace() == False)):
            return texto
        else:
            print(f"{'-'*5} [ERROR] Debe completar este campo para continuar. {'-'*5} \n")
            texto = input("Intente nuevamente: ")

def producto(): #En esta función verificamos y comprobamos que el nombre sea ingresado correctamente.
    nombre = input("Nombre del producto: ").capitalize() #Pedimos al usuario el nombre del producto.
    nombre = verificar_texto(nombre) #Verificamos con esta función si el nombre no está vacío.
    return nombre #Se guarda el valor y es enviado al menú principal para ser guardado en la base de datos.

def cantidad(): #En esta función pedimos al usuario ingresar la cantidad de productos.
    while True: #Entramos al bucle para comprobar los valores.
        valor_cantidad = input("Cantidad del producto: ") 
        try:
            cantidad = int(valor_cantidad) #Convertimos esos valores en un números enteros.
            if cantidad > 0:
                return cantidad #Si el número es mayor a cero, lo enviamos al menú principal para ser guardado en la base de datos.
            else:
                print(f"{'-'*5} [ERROR] La cantidad debe ser mayor a 0. {'-'*5} \n")
        except ValueError:
            print(f"{'-'*5} [ERROR] ValueError!! Solo debe ingresar dígitos.{'-'*5} \n") #Si el valor es distinto a un número, se muestra el error en pantalla y se vuelve a pedir al usuario ingresar la cantidad.

def precio(): #Verifica si el precio es un número positivo antes de ser guardado en la base de datos.
    while True:
        valor_precio = input("Precio del producto: ") #Pedimos al usuario el valor del precio.
        valor_precio = valor_precio.replace(",", ".") #Reemplazamos algunos signos.
        try: 
            precio = float(valor_precio) #Convertimos el valor en un número flotante y verificamos que sea un número mayor a cero.
            if precio > 0:
                return precio #Se guarda el valor y es enviado al menú principal para ser guardado en la base de datos.
            else:
                print(f"{'-'*5} [ERROR] El precio debe ser mayor a 0. {'-'*5} \n")
        except ValueError:
            print(f"{'-'*5} [ERROR] ValueError!! {'-'*5} \n") #Si el valor es distinto a un número, se muestra el error en pantalla y se vuelve a pedir al usuario ingresar el precio del producto.

def categoria(): #Verifica si el nombre de la categoría cumple con las condiciones para ser guardado en la base de datos.
    nombre = input("Categoría: ").capitalize()
    nombre = verificar_texto(nombre) #verificamos si no está vacío y si tiene un mínimo de letras para guardarse
    return nombre #Enviamos los datos leídos al programa principal para que sea guardados en la base de datos.

def descripcion_producto(): #Verifica las condiciones del campo para ser guardado en la base de datos.
    texto = input("Descripción del producto (agregue algunos detalles breves, por favor): ").capitalize()
    texto = verificar_texto(texto) #verificamos si la descripción no está vacío y si tiene un mínimo de detalles para el producto.
    return texto #Enviamos la descripción al programa principal para que sea guardados en la base de datos.

def procesar_actualizacion(nombre, precio, cantidad, categoria, descripcion): #Se pregunta y se procesa los parámetros antes de enviarlos al menú principal...
    pregunta_nombre= input("\n -Desea cambiar el nombre del producto? (S/N): ").lower 
    if pregunta_nombre == "s": #Preguntamos si necesitamos cambiar el nombre
        nombre= nombre() #realizamos el cambio usando otra función y mostramos un mensaje en pantalla después de realizar dicho cambio...
        print(f"\n Nombre del Producto Actualizado...\n {'_'*70}")
    else: #Si el usuario no desea cambiar el precio, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\tNo se realizaron cambios...\n") 
    pregunta_precio= input("\n -Desea actualizar el precio? (S/N): ").lower #Preguntamos si necesitamos actualizar el precio
    if pregunta_precio == "s":
        precio= precio() #Actualizamos el precio reutilizando la funcion de precio...
        print(f"\n Precio Actualizado...\n {'_'*70}") #Confirmamos los cambios y devolvemos el precio actualizado...
    else: #Si el usuario no desea cambiar el precio, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\tNo se realizaron cambios...\n") 
    pregunta_cantidad= input("\n -Desea actualizar la cantidad de productos disponibles? (S/N): ").lower
    if pregunta_cantidad == "s": #Preguntamos si necesitamos cambiar la cantidad de productos disponibles...
        cantidad= cantidad() #Realizamos el cambio reutilizando otra función, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\n Cantidad disponible del producto actualizado... \n {'_'*70}")
    else: #Si el usuario no desea cambiar el precio, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\tNo se realizaron cambios...\n")
    pregunta_categoria= input("\n -Desea cambiar la categoria de su producto? (S/N): ").lower
    if pregunta_categoria == "s": #Preguntamos si necesitamos cambiar la categoría del producto...
        categoria= categoria() #Realizamos el cambio reutilizando otra función, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\n Se ha actualizado la categoría del producto... \n {'_'*70}")
    else: #Si el usuario no desea cambiar el precio, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\tNo se realizaron cambios...\n")
    pregunta_descripcion= input("\n -Desea actualizar la descripción de su producto? (S/N): ").lower
    if pregunta_descripcion == "s": #Preguntamos si necesitamos realizar cambios en la descripción del producto...
        descripcion= descripcion() #Realizamos el cambio reutilizando otra función, mostramos un mensaje en pantalla y pasamos al siguiente parámetro...
        print(f"\n Se ha cambiado la descripción del producto... \n {'_'*70}")
    else: #Si el usuario no desea cambiar el precio, mostramos un mensaje en pantalla y damos por terminado los cambios (o no) del producto...
        print(f"\tNo se realizaron cambios...\n")

    return nombre, precio, cantidad, categoria, descripcion
