
def mostrar_menu(): #Función para mostrar el menu
    print("--------------------------------------------------------------------------------")
    print("Selecciona una opción")
    print("1.- Calcular el area de un cuadrado")
    print("2.- Calcular el area de un círculo")
    print("3.- Calcular el area de un triángulo")
    print("4.- Salir") #Aqui se explican las opciones que tiene para elejir
    return input("Ingrese una opción: ") #Con esto el usuario ingresa la opción que desa realizar

def area_cuadrado():
    lado_del_cuadrado = int(input("Ingrese el valor del lado de su cuadrado: ")) #Se le pide que ingrese el area del cuadrado
    if lado_del_cuadrado <= 0: #Validamos que el area sea un numero mayor a 0
        print("Error: El lado debe ser un número positivo.") #En caso de ser menor a cero dira este error y se regresa al inicio
        return
    area_del_cuadrado = lado_del_cuadrado * lado_del_cuadrado #Formula para sacar el area
    print("El area del cuadrado es: ", area_del_cuadrado) #Mostramos el area del cuadrado

def area_circulo():
    radio_circulo = int(input("Ingrese el valor del radio de su círculo: ")) #Pedimos el radio del circulo
    if radio_circulo <= 0: #Validamos que el radio sea mayor a cero
        print("Error: El radio debe ser un número positivo.") 
        return
    pi = 3.1416 #Asignamos el valor a pi
    area_del_circulo = pi * (radio_circulo * radio_circulo) #Realizamos la formula del area
    print("El area del círculo es: ", area_del_circulo) #Mostramos el area del círculo

def area_triangulo():
    base_del_triangulo = int(input("Ingrese el valor de la base del triángulo : ")) #Pedimos el valor de la base
    altura_triangulo = int(input("Ingrese la altura del triángulo: ")) #Tambien pedimos el valor de la altura
    if base_del_triangulo <= 0 or altura_triangulo <= 0: #Validamos que las dos sean mayor a 0
        print("Error: La base y la altura deben ser números positivos.")
        return
    area_del_triangulo = (base_del_triangulo * altura_triangulo) / 2 #Realizamos la formula del area
    print("El area del triángulo es: ", area_del_triangulo) #Mostramos el area del triángulo

def ejecutar_programa():
    while True: #Con esta función creamos el menu que se utilizara para guiar al usuario a traves del sistema
        op=mostrar_menu()
        if op == "1": #Al seleccionar la opción 1 llama a la función del cuadrado
            area_cuadrado()        
        elif op == "2": #Al seleccionar la opción 2 llama a la función del círculo
            area_circulo()
        elif op == "3": #Si seleccionan esta opción llama a la función del triángulo
            area_triangulo()
        elif op == "4": #Con esta opcion el programa se terminaria de ejecutar
            print("Gracias por usar el programa") #Agradecemos al usuario
            break #Se rompe el ciclo
        else: #En dado caso de que ponga otro numero se mostrara el mensaje y se desplegaria el menu 
            print("Opcion no valida")

ejecutar_programa() #Ejecuta el programa