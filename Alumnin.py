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
        break
    else:
        print("ingrese 'si' o 'no'")
print ("¡Ingresaste!")
while True:
    opcion= int(input("¿Donde queres dirigirte? \n1. Registro de materias \n2. Ingresar notas \n3. Ver notas \n4. Darse de baja de materias \n5. Salir del sistema\n-"))
    if opcion == 1:
        print("Materias disponibles: ", materias)
        seleccion=input(f'Selecciona la materia a la que te queres inscribir: ').lower()
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
                continue
            # Si la materia existe en el diccionario del alumno:
            else:
                print("--------------------------------")
                print("Ya estas inscripto a esa materia")
                print("--------------------------------")
                continue
        else: 
            print("--------------------------------")
            print("lo sentimos, esa materia no existe")
            print("--------------------------------")
            continue
    if opcion == 2:
        m_seleccionada= input(f'¿A que materia deseas ingresarle una nota? \n Materias a las que estas inscripto: {materias}: ').lower()
        if m_seleccionada in alumnos[nombre_ingresado]["materias"]:
            nuevaNota = int(input(f'Ingresa la nota para {m_seleccionada}: '))
            
            print("")

        
    break
