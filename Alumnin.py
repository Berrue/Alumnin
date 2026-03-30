import json

with open("alumnos.json", "r") as archivo:
    alumnos = json.load(archivo)

with open("materias.json", "r") as archivo:
    materias = json.load(archivo)
    
while True:
    print ("------- Bienvenido al sistema de alumnos -------")
    confirmacion = input("¿Esta usted registrado?: ")
   
    if confirmacion.lower() == "si":
     #Confirmacion    
        nombre_ingresado = input("ingrese su nombre: ")
        if nombre_ingresado in alumnos:
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
    opcion= int(input("¡Ingresaste! \n¿Donde queres dirigirte? \n1.Registro de materias \n2. Ver notas \n3. Ingresar notas \n4.Darse de baja de materias \n5.Salir del sistema"))
    if opcion == 1:
        print("Materias disponibles: ", materias)
        seleccion=input("Selecciona la materia a la que te queres inscribir", materias).lower()
        if seleccion in materias:
            # Verificacion de si el alumno ya tiene una lista de materias
            if "materias_inscriptas" not in alumnos[nombre_ingresado]:
                alumnos[nombre_ingresado]["materias inscriptas"] = []
            if seleccion not in alumnos[nombre_ingresado]["materias_inscriptas"]:
                alumnos[nombre_ingresado]["materias_inscriptas"].append(seleccion)
                # Lo guardamos:
                with open("alumnos.json", "w") as archivo:
                    json.dump(alumnos, archivo, indent=4)
                print(f'Te inscribiste con exito a {seleccion}!')
            # Si la materia no existe:
            else:
                print("Ya estas inscripto a esa materia")
        else: 
            print("lo sentimos, esa materia no existe")
    break
