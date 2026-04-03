import json

with open("alumnos.json", "r") as archivo:
    alumnos = json.load(archivo)

with open("materias.json", "r") as archivo:
    materias = json.load(archivo)

def guardar_datos(datos):
    with open("alumnos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

# Logeo
while True:
    print ("------- Bienvenido al sistema de alumnos -------")
    confirmacion = input("¿Esta usted registrado? (si/no): ")
   
    if confirmacion.lower() == "si":
     #Confirmacion    
        nombre_ingresado = input("ingrese su nombre: ")
        if nombre_ingresado in alumnos:
            verificar_contraseña = input("Ingresa tu contraseña: ")
            if verificar_contraseña == alumnos[nombre_ingresado]["password"]:
                print("Ingreso exitoso!")
                break
        else:
            print("Lo sentimos, no estas registrado")
            
    # Registro
    elif confirmacion.lower() == "no":
        n_registro = input("Ingrese su nombre para registrarse: ")
        c_registro = input("Ingrese su contraseña: ")
        alumnos[n_registro] = {
            "password": c_registro,
            "materias_inscriptas": {} #en el corchete irian las notas
        }
        guardar_datos(alumnos)
        print ("Registro realizado con exito, vuelva a loguearse para poder entrar\n")
        continue
    else:
        print("ingrese 'si' o 'no'")
print ("¡Ingresaste!")


while True:
    print("\n---MENU---")
    opcion= int(input("¿Donde queres dirigirte? \n1. Registro de materias \n2. Ingresar notas \n3. Ver notas \n4. Darse de baja de materias \n5. Salir del sistema\n-"))
    if opcion == 1:
        print(f'Materias disponibles: {materias}')
        seleccion=input(f'Selecciona la materia a la que te queres inscribir: ').lower()
        if seleccion in materias:
            # Verificacion de si el alumno ya tiene una lista de materias
            if "materias_inscriptas" not in alumnos[nombre_ingresado]:
                alumnos[nombre_ingresado]["materias_inscriptas"] = {}
            if seleccion not in alumnos[nombre_ingresado]["materias_inscriptas"]:
                # Lo guardamos con una nota 0 por defecto:
                alumnos[nombre_ingresado]["materias_inscriptas"][seleccion]= 0
                guardar_datos(alumnos)
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
        mis_materias = alumnos[nombre_ingresado]["materias_inscriptas"]
        if not mis_materias:
            print("Primero tenes que inscribirte a una materia.")
            continue
        m_seleccionada= input(f'¿A que materia deseas ingresarle una nota? \nMaterias a las que estas inscripto: {list(mis_materias.keys())}: ').lower()
        if m_seleccionada in alumnos[nombre_ingresado]["materias_inscriptas"]:
            if m_seleccionada in mis_materias:
                nueva_nota = int(input(f'Escribi la nota para {m_seleccionada}'))
                alumnos[nombre_ingresado]["materias_inscriptas"][m_seleccionada]= nueva_nota
                guardar_datos(alumnos)
                print("Nota cargada")
            else:
                print("No estas inscripto en esta carrera")
        if m_seleccionada not in materias:
            print("Ingresa una materia valida")
    if opcion == 3:
        mis_materias = alumnos[nombre_ingresado]["materias_inscriptas"]
        if not mis_materias:
            print("No estas inscripto a ninguna materia")
            continue
        for materia, nota in mis_materias.items():
            print("--------------------------------")
            if nota >= 4:
                print(f'{materia.capitalize()}: {nota}: aprobado')
            if nota >0 and nota < 4:
                print(f'{materia.capitalize()}: {nota}: desaprobado')
            if nota == 0:
                print(f'{materia.capitalize()} no tiene notas cargadas')
                
                
    if opcion == 4:
        mis_materias = alumnos[nombre_ingresado]["materias_inscriptas"]
        if not mis_materias:
            print ("no estas inscripto en ninguna materia")
            continue
        baja_materia = input(f'Ingrese la materia de la que quiere darse de baja \nMaterias a las que estas inscripto: {list(mis_materias.keys())}: ').lower()
        if baja_materia not in mis_materias:
            print ("No estas inscripto en esa materia")
            continue
        if baja_materia in mis_materias:
                mis_materias.pop(baja_materia)
                guardar_datos(alumnos)
                print (f'Diste de baja {baja_materia.capitalize()}.')
                
    if opcion == 5:
        print ("Muchas gracias por usar Alumnin, ¡hasta la proxima!")
        break