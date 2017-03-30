import getpass



admistradores=["Anthonny","Apellido","Calderon","20","Anthonnyc10@gmail.com","Administrador",1,2014085419,12345]
listaUsuarios=[402320214,123456,2]
#usuarios={}




def login():

    while True:
        try:
            cedula=int(input("Digite su numero de cedula\n"))
            password=int(input("Digite su contraseña\n"))
            if cedula and password in admistradores:
                print("Registrado",verificar())
                break

            else:
                print("Usted no esta registrado",registro())
                break
        except ValueError:
            print("Solo numeros")

def verificar():
    for x in admistradores:
        if x==1:
            print(" Usted es un Administrador")


####################################################
#FUNCION DONDE SE CREARA EL REGISTRO DE LOS JUGADORES
####################################################


def registro():
            nombre=input("Escriba un nombre\n")
            listaUsuarios.append(nombre)
            apellido=input("Escriba el apellido\n")
            listaUsuarios.append(apellido)
            correo= input("Digite el correo electronico\n")
            listaUsuarios.append(correo)
            tipo_Usuario=int(input("Tipo Usuario Administrador 1 o  2 Jugador\n"))
            listaUsuarios.append(tipo_Usuario)
            while True:
                try:
                    pasword=int(input("Escriba una contraseña\n"))
                    listaUsuarios.append(pasword)

                    break
                except ValueError:
                    print("solo numeros")

            while True:
                try:
                    edad = int(input("Digite la edad\n"))
                    listaUsuarios.append(edad)
                    break
                except ValueError:
                    print("solo numeros")

            print("Registrado")



################################FUNCIONES QUE USAREMOS CUANDO YA HEMOS FINALIZADO EL REGISTRO Y EL LOGIN###################################
#MENU PRINCIPAL DEL JUGADOR AQUI SELECCIONA LA OPCION QUE DESEA REALIZAR

def menuAdministrador():
    while True:
        try:
            print("MENU ADMINISTRADOR")
            print("1: Aprobar jugadores")
            print("2: Torneos")
            print("3: Records jugadores")
            print("4: Salir")
            solicitud=int(input("<<<<<Digite una opcion>>>>>\n"))
            break
        except ValueError:
            if solicitud==1:
                print(aprobarJugadores())
            elif solicitud==2:
                print(torneos())
            elif solicitud==3:
                print(records())

            else:
                pass
menuAdministrador()



##############################################
##FUNCIONES QUE PERTENECEN AL ADMINISTRADOR###
##############################################
def aprobarJugadores():
    aprobarJugadores()
def torneos():
    torneos()
def records():
    records()




########################################################################
#MENU PRINCIPAL DEL JUGADOR AQUI SELECCIONA LA OPCION QUE DESEA REALIZAR
########################################################################
#
# def menuJugador():
#     while True:
#         try:
#             print("MENU PRINCIPAL DEL JUGADOR")
#             print("1: Inscribirse a un torneo")
#             print("2: Jugar Partida")
#             print("3: Ver Records")
#             opcion1=int(input("<<<<<Digite una opcion>>>>>\n"))
#             break
#         except ValueError:
#             if opcion1==1:
#                 print(inscribirse_Torneo())
#             elif opcion1==2:
#                 print(jugar())
#             elif opcion1==3:
#                 print(ver_Records())
#
#             else:
#                 break
#
# menuJugador()

##############################################
##FUNCIONES QUE PERTENECEN AL USUARIO JUGADOR#
##############################################
def inscribirse_Torneo():
    inscribirse_Torneo()

def jugar():
    jugar()

def ver_Records():
    ver_Records()

##############################################
###ESTE MENU VA SER EL PRINCIPAL DEL JUEGO####
##############################################
#
def menuPrincipal():
    while True:
        try:
            print("Bienvenido/a al Master Mind-UTN")
            print("1: Login")
            print("2: Registro")
            print("3: Salir")
            opcion= int(input("<<<<<<<<<<<<<<<<<<<<<<<Digite una opcion>>>>>>>>>>>>>>>>>>>>>>>>\n"))
            break
        except ValueError:
            print("Ingresa un numero entero")
    if opcion==1:
        print(login())
    elif opcion==2:
        print(registro())
    elif opcion==3:
        pass
menuPrincipal()
