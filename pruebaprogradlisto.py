import csv


nombre = ""
cargo = ""
busqueda_cargo = ""
sueldobrut = 0
descsalud = 0
descafp = 0
totaldesc = 0
sueldoliq = 0
lista_trabajadores = []
nueva_lista = []

  

try:

    while True:


        print('''::::::: Menu :::::::
                
                1)Registrar Trabajador
                2)Listar trabajadores
                3)Imprimir plantilla sueldos
                4)Salir''')
        

        opc = input("Ingrese la opcion deseada: ")
        while not opc.isnumeric():
            opc = input("Error, la opcion ingresada debe ser un numero: ")



        opc = int(opc)


        if opc == 1:

            nombre = input("Ingrese su nombre y apellido: ")
            while True:
                cargo = input("Ingrese su cargo: ")
                if cargo == "Mesero":
                    break
                elif cargo == "Cocinero":
                    break
                elif cargo == "Cajero":
                    break
                if not cargo == "Mesero":
                    print("Error, el cargo ingresado no es correcto")
                    print("El cargo ingresado debe ser: Mesero, Cocinero o Cajero ")
                    print("(Recuerde usar mayuscula al principio)")
                    


            sueldobrut = int(input("Ingrese su sueldo bruto: "))
            descsalud = sueldobrut * 0.07
            descsalud = int(descsalud)
            descafp = sueldobrut * 0.1
            descafp = int(descafp)
            totaldesc = descsalud + descafp
            totaldesc = int(totaldesc)
            sueldoliq = sueldobrut - totaldesc
            sueldoliq = int(sueldoliq)
            lista_trabajadores = [nombre,cargo,sueldobrut,descsalud,descafp,sueldoliq]
            nueva_lista.append(lista_trabajadores)



            with open("datos_persona.csv","w", newline="") as archivo:
                escritor_personas = csv.writer(archivo)
                escritor_personas.writerow(["Nombre y Apellido   /","Cargo  /","Sueldo Bruto   /","Desc Salud      /","Desc AFP   /","Sueldo Liquido  "])
                escritor_personas.writerows(nueva_lista)

        if opc == 2:
            with open("datos_persona.csv","r", newline="") as archivo:
                lector_personas = csv.reader(archivo)
                for lista in lector_personas:
                    print(lista)

        if opc == 3:
            
            busqueda_cargo = input("Escriba el cargo a buscar: ")
            with open("datos_persona.csv","r", newline="") as archivo:
                lector_personas = csv.reader(archivo)
                for personas in lector_personas:
                    if personas[1] == busqueda_cargo:
                        print(f"Nombre: ",personas[0],"/","Sueldo Bruto: ",personas[2],"/","Descuento Salud: ",personas[3],"/","Descuento AFP: ",personas[4],"/","Sueldo Liquido: ",personas[5],"/",)
                        

        if opc == 4:
            break
except:
    print("Error Desconocido")




    


        
    
    