import random
def barras(weith=90):
    print("-"*weith)
jugar=("sí")
while jugar=="sí":
    #explicación
    print("bienvenido a CODE un juego en el que tienes que adivinar el código generado aleatoriamente,")
    print("donde no se repiten los númeroscuando haces un 'acierto' es que has hacertado el número y")
    print("posicion del número y cuando 'coinciden' es porque has hacertado el núemro pero no la posición")
    barras(weith=90)
    difficult=int(input("¿Qué dificultad quieres? 1=fácil 2=intermedio 3=dificil 4=insano "))
    #dificutad
    if difficult==1:
        cantdig=3
    elif difficult==2:
        cantdig=4
    elif difficult==3:
        cantdig=6
    elif difficult==4:
        cantdig=9
    #genera un número aleatorio
    digitos=("0","1","2","3","4","5","6","7","8","9")
    codigo=""
    for i in range(cantdig):
        elegido= random.choice(digitos)
        while elegido in codigo:
            elegido= random.choice(digitos)
        codigo= codigo + elegido
    #intentas adivinar el número
    print("tienes que adivinar un codigo de", cantdig,"digitos distintos")
    barras(weith=90)
    prop=input("¿Qué codigo propones? ")
    intentos=1

    while prop != codigo:
        intentos= intentos + 1
        aciertos=0
        coinciden=0
        if prop == cantdig:
            continue
        else:
            print ("Inténtalo de nuevo")
        for i in range(cantdig):
            if prop[i]==codigo[i]:
                aciertos = aciertos + 1
            elif prop[i] in codigo:
                coinciden= coinciden + 1
        print("Tu propuesta (", prop,") tiene ", aciertos," aciertos y ", coinciden," coinciden")
        barras(weith=90)
        prop=input("Propone otro código ")
    #fin del juego
    print("felicidades has acertado el codigo en ", intentos," intentos")
    jugar=input("¿Deseas volver a jugar? <sí o no> ")
    barras(weith=90)