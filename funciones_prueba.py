import os
import time
#Usted dijo que se podian hacer comentarios en relacion a las funciones para ayudarnos

def validar_menu():
    os.system('cls')
    print("""MENÚ
    1.XXXXXXXX
    2.XXXXXXXX
    3.XXXXXXXX
    4.XXXXXXXX
    5.XXXXXXXX
      """)
    
def validar_opcion():
    while True:
        try:
            opcion = int(input("Escoga una opción del Menú (1 al 5): "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! Escoga una opción correcta")
        except:
            print("ERROR!   La opcion debe ser un número entero")

def ver_arreglo(): #Tiene como ejemplo el restaurant pero se puede cambiar nomás
    os.system("cls")
    print("\tVER RESTAURANT\n")
    contador = 1
    for x in range(3):
        print(f"Mesas para {(x+1)*2} personas: ",end=" ")
        for y in range(3):
            print(f"Mesa {contador}: {restaurant[x][y]} ", end=" ")
            contador += 1
        print("\n")
    time.sleep(3)

def mesas_disponibles(p_cantidad):
    contador = 1
    lista_mesas = []
    for x in range(3):
        for y in range(3):
            if restaurant[x][y] == 0:
                if p_cantidad <= 2:
                    lista_mesas.append(contador)
                elif p_cantidad >=3 and p_cantidad <= 4 and x in(1,2):
                    lista_mesas.append(contador)
                elif p_cantidad >= 5 and p_cantidad <=6 and x == 2:
                    lista_mesas.append(contador)
            contador += 1
    return lista_mesas

def validar_mesa(p_mesas):
    while True:
        try:
            mesa = int(input("Ingrese número de mesa: "))
            if mesa in(p_mesas):
                return mesa
            else:
                print("ERROR! NÚMERO DE MESA NO DISPONIBLE!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def reservar():
    os.system('clear')
    print("RESERVAR MESA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        print("YA TIENE UNA RESERVA!")
        return

def cancelar_reserva(): 
    os.system('clear')
    print("CANCELAR RESERVA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        posicion = lista_ruts.index(rut)
        fila = lista_filas[posicion]
        columna = lista_columnas[posicion]
        restaurant[fila][columna] = 0

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():#tambien se puede usar para nombre de usuario en algun tipo de videojuego o pagina
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad >= 18 and edad <= 100:
                return edad
            else:
                print("ERROR! LA EDAD DEBE ESTAR ENTRE 18 Y 100")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")

def validar_cantidad_prod():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_marca_auto():#si falta marca agregar nomas
    while True:
        marca = input("¿Que marca elige comprar (Nissan, Chevrolet, Renault?")
        if marca.lower() == "renault" or marca.lower() == "nissan" or marca.lower()=="chevrolet":
            print(f"disfrute su nuevo {marca}")
            return marca
        else:
            print("No tenemos disponible esa marca")

def validar_color_auto():
    while True:
        color= input("¿Que color  elige comprar (Blanco, Rojo, Gris?")
        if color.lower() == "blanco" or color.lower() == "rojo" or color.lower()=="gris":
            return color
        else:
            print("No tenemos disponible esa marca")
    
def validar_genero_libro():
    while True:
        gn_li= input("¿De que genero es el libro que quiere comprar (Ciencia Ficcion, Terror, Romance?")
        if gn_li.lower() == "ciencia ficcion" or gn_li() == "terror" or gn_li()=="romance":
            return gn_li
        else:
            print("No tenemos disponible esa marca")

def isbn_libro():
    while True:
        try:
            isbn = int(input("Ingrese el codigo del libro"))
            if isbn >= 1111111111111 and isbn <= 9999999999999:
                return isbn
            else:
                print("ERROR!Ingrese un codígo correcto")
        except:
            print("ERROR!Ingrese un número entero")

def validar_descuento():
    while True:
        try:
            desc = int(input("Ingrese descuento: "))
            if desc >= 0:
                return desc
            else:
                print("ERROR! DESCUENTO DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def pagar():
    os.system('clear')
    print("PAGAR CUENTA\n")
    rut = validar_rut()
    if rut in lista_ruts:
        posicion = lista_ruts.index(rut)
        descuento = validar_descuento()
        print(f"""BOLETA
        SUBTOTAL   {lista_totales[posicion]}
        IVA        {round(19/100 * lista_totales[posicion])}
        TOTAL      {round(119/100 * lista_totales[posicion])}
        DESCUENTO  {descuento}
        TOTAL      {round(119/100 * lista_totales[posicion]) - descuento}""")
    
def calcular_iva():
    precio = validar_numero("precio")
    iva = round(precio*19/100)
    print("El valor del iva del producto con precio",precio,"es",iva)

def descuento():
    precio = validar_numero("precio")
    descuento = validar_numero("descuento")
    total = precio - descuento
    print("El precio final es:",total)

def validar_numero(p_texto):
    while True:
        try:
            numero = int(input(f"Ingrese {p_texto} del producto: "))
            if numero > 0:
                return numero
            else:
                print(f"ERROR! EL {p_texto} DEBE SER POSITIVO!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def calcular_imc():
    peso = validar_peso()
    estatura = validar_estatura()
    imc = round(peso/estatura**2 , 1)
    print("Su índica de masa corporal(IMC) es:",imc)
    if imc < 18.5:
        print("Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Adecuado")
    elif imc >= 25.0 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Obesidad grado 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidad grado 2")
    else:
        print("Obesidad grado 3")

def validar_peso():
    while True:
        try:
            peso = float(input("Ingrese peso(Kg): "))
            if peso > 0:
                return peso
            else:
                print("ERROR! peso incorrecto, debe ser superior a cero!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_estatura():
    while True:
        try:
            estatura = float(input("Ingrese estatura(m): "))
            if estatura >= 0.1 and estatura <= 3:
                return estatura
            else:
                print("ERROR! LA ESTATURA DEBE ESTAR ENTRE 0.1 y 3 metros!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO!")

def validar_clave():
    while True:
        clave = input("Ingrese clave: ")
        validar_clave = input("Ingrese nuevamente la clave: ")
        if len(clave)>=6 and len(clave)<=16 and clave==validar_clave:
            break
        else:
            print("ERROR! largo incorrecto o claves no coinciden!")

def validar_telefono():
    while True:
        try:
            telefono = int(input("Ingrese teléfono: "))
            if len(str(telefono))==9:
                break
            else:
                print("ERROR! el teléfono debe tener 9 dígitos!")
        except:
            print("ERROR! debe ingresar ingresar un número entero!")

def validar_genero():
    while True:
            genero = input("Ingrese género(F,M,O): ")
            if genero.upper() in("F","M","O"):
                break
            else:
                print("ERROR! el género debe ser f, m, o!")



