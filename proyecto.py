
tablero=[['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

opciones=['X','O']
jugadores=dict(jugador1="",jugador2="")

def opcionJugador():
    jugador1=""
    while jugador1 not in opciones:
        jugador1=input("Escoja una opcion X o O\n")
        jugador1=jugador1.upper()
        if jugador1 not in opciones:
            print("Opcion invalidad")
        elif jugador1 == 'X':
            jugadores.update({"jugador1":"X","jugador2":"O"})
        else:
            jugadores.update({"jugador1":"O","jugador2":"X"})

def show():
    for x in range(3):
        for y in range(3):
            print(tablero[x][y],"|", end='\n' if y == 2 else '')
        
def empate():
    empate=True
    for x in range(3):
        for y in range(3):
            if tablero[x][y] == ".":
                empate&=False
    return empate

def ganador(jugador):
    empate=False
    opcion=jugadores.get(jugador)
    if opcion == tablero[0][0] and opcion == tablero[1][0] and opcion == tablero[2][0]:
        empate=True
    elif opcion == tablero[0][2] and opcion == tablero[1][2] and opcion == tablero[2][2]:
        empate=True
    elif opcion == tablero[0][1] and opcion == tablero[1][1] and opcion == tablero[2][1]:
        empate=True
    elif opcion == tablero[0][0] and opcion == tablero[0][1] and opcion == tablero[0][2]:
        empate=True
    elif opcion == tablero[1][0] and opcion == tablero[1][1] and opcion == tablero[1][2]:
        empate=True
    elif opcion == tablero[2][0] and opcion == tablero[2][1] and opcion == tablero[2][2]:
        empate=True
    elif opcion == tablero[0][0] and opcion == tablero[1][1] and opcion == tablero[2][2]:
        empate=True
    elif opcion == tablero[0][2] and opcion == tablero[1][1] and opcion == tablero[2][0]:
        empate=True
    return empate

def ingresoPosicion(jugadorName):
    valor1=input("\n"+jugadorName+": Indique la fila en donde sea poner un "+jugadores.get(jugadorName)+"\n")    
    valor2=input("\n"+jugadorName+": Indique la columna en donde sea poner un "+jugadores.get(jugadorName)+"\n")    
    return valor1,valor2

def decorador1(valoresfilacolumnavalor):
    def deco1(fila,columna,valor):
        if fila.isnumeric():
          fila=int(fila)
        if columna.isnumeric():
          columna=int(columna)
        if fila not in [0,1,2]:
            print("**La fila ingresada '"+fila+"' es invalida debe ser [0,1,2]**")
        elif columna not in [0,1,2]:
            print("**La columna ingresada '"+columna+"' es invalida debe ser [0,1,2]**")
        else:
            return valoresfilacolumnavalor(fila,columna,valor)
        return False
    return deco1

@decorador1
def asignarValor(fila,columna,valor):
    if tablero[fila][columna]== '.':
        tablero[fila][columna]=valor
    else:
        return False
    return True

def jugadorInicial():
    for k,v in jugadores.items():
        if v == opciones[0]:
            return k
    print("no se logro encontrar opcion")
def changeJugador(jugadorActual):
    for k,v in jugadores.items():
        if not k == jugadorActual:
            return k

salir=False
opcionJugador()
jugador=jugadorInicial()
while salir==False:
    show()
    fila,columna=ingresoPosicion(jugador)
    if not asignarValor(fila, columna, jugadores.get(jugador)):
        print("Opcion invalida, \n vuelva a intentarlo")
    else:
        salir=empate() or ganador(jugador)   
        jugador=changeJugador(jugador)

show()
print("El resultado es","empate" if empate() else "GANADOR "+jugador )





