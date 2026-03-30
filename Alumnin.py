import json

with open("alumnos.json", "r") as archivo:
    alumnos = json.load(archivo)
    
while True:
    print ("------- Bienvenido al sistema de alumnos -------")
    confirmacion = input("¿Esta usted registrado?: ")
   
    if confirmacion.lower() == "si":
     #Confirmacion    
        nombre_ingresado = input("ingrese su nombre: ")
        if nombre_ingresado.lower() in alumnos:
            verificar_contraseña = input("Ingresa tu contraseña: ")
            if verificar_contraseña == alumnos[nombre_ingresado]:
                ingresado = True
                print (f'Bienvenido, {nombre_ingresado}, ¿como te puedo ayudar hoy?')
            break
        else:
            print("Lo sentimos, no estas registrado")
            
    # Registro
    elif confirmacion.lower() == "no":
        n_registro = input("Ingrese su nombre: ")
        c_registro = input("Ingrese su contraseña: ")
        alumnos[n_registro] = c_registro
        with open("alumnos.json", "w") as archivo:
            json.dump(alumnos, archivo, indent=4)
        print ("Registro realizado con exito")
        ingresado = True
        break
    else:
        print("ingrese 'si' o 'no'")
            
while ingresado == True:
    print ("¡Ingresaste! \n¿Donde queres dirigirte? \n1.Registro de materias \n2. Ver notas \n3. Ingresar notas \n4.Darse de baja de materias \n5.Salir del sistema")
    break
