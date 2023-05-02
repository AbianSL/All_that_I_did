import textwrap
from fun import *
#importar todo lo que tiene el otro archivo
opf="si"
na=0
while opf=="si":
    op1=1
    while op1==1:
        na=0
        print("1) ¿Cuál es el protagonista de Tate no yusha?")
        re1=input()
        if re1=="naofumi":
            ve()
            #funciones que estan en el otro archivo y sirven para decir si has acertado ve() o fallado fa()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            na=na+1
            if na>5:
                print ("estás cometiendo muchos fallos, un consejo... empieza por N y termina por I")
                print ("tienes", fallos,"fallos")
                print()
            elif na>10:
                print ("Te voy a dar otro consejito, Empieza por Nao y termina por umi")
                print ("tienes", fallos,"fallos")
                print()
            elif ma>15:
                print("lo siento has fallado demasiado, tienes",fallos,"fallos y la respuesta es naofumi")
            else:
                print ("tienes",fallos,"fallos")
                print()
        #primera pregunta y sistema de como preguntar :3
    while op1==1:
        na=0
        print("2) ¿De que videojuego es Arthas?")
        re2=input()
        if re2=="WOW" or "World Of Warcraft":
            #la posibilidad de tener varias opciones para acertar
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if na>5:
                print ("estás cometiendo muchos fallos, un consejo... es el mundo de Warcraft")
                print ("tienes", fallos,"fallos")
                print()
            elif na>10:
                print ("Te voy a dar otra pista, Empieza por world y termina por craft")
                print ("tienes", fallos,"fallos")
                print()
            elif ma>15:
                print("lo siento has fallado demasiado, tienes",fallos,"fallos y la respuesta es WOW o World Of Warcraft")
            else:

                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("3) ¿Quién es el capitán de los muguiwara en one piece?")
        re3=input()
        if re3=="luffy":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if na>15:
                print ("tienes", fallos,"fallos")
                print()
            elif na>10:
                print ("Te voy a dar otro consejito, se comio la fruta del diablo que te hace goma")
                print ("tienes", fallos,"fallos")
                print()
            elif ma>15:
                print("lo siento has fallado demasiado, tienes",fallos,"fallos y la respuesta es Luffy")
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por L y tiene doble F")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("4) ¿Cómo se llama el protagonista de One punch Man?")
        re4=input()
        if re4=="saitama":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<20:
                print ("tienes", fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por S y termina por A")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("5) ¿Cómo se llama el dragon que se invoca con 7 bolas en Dragon Ball?")
        re5=input()
        if re5=="shenlong":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<25:
                print ("tienes", fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por SH y tiene doble ONG")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("6) ¿Cómo se llama el famoso detective de Londres en el siglo XIX del relato de Sidney Paget?")
        re6=input()
        if re6=="Sherlock" or "sherlock holmes":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<30:
                print ("tienes", fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por SH y tiene doble CK")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("7) ¿Cómo se llama el juego que creó Markus Persson más conocido como Notch?")
        re7=input()
        if re7=="minecraft":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<35:
                print ("tienes", fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por SH y tiene doble ONG")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("8) ¿Cómo se llama el actor del Joker en la nueva película 'JOKER'?")
        re8=input()
        if re8=="Joaquin Phoenix" or "Phoenix":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<35:
                print ("tienes", fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por SH y tiene doble ONG")
                print ("tienes",fallos,"fallos")
                print() 
    while op1==1:
        print("9) ¿En qué época está ambientado el primer juego de Assasin Creed?")
        re9=input()
        if re9=="Edad media" or "la edad media":
            ve()
            aciertos=aciertos + 1
            print ("tienes",aciertos,"aciertos")
            print()
            break
        else:
            fa()
            fallos=fallos + 1
            if fallos<35:
                print (fallos,"fallos")
                print()
            else:
                print ("estás cometiendo muchos fallos, un consejo... empieza por SH y tiene doble ONG")
                print ("tienes",fallos,"fallos")
                print() 
    #me encanta hacer estas tonteras
    print("y por último... la pregunta más dificil")
    time.sleep(2)
    print("¿Te gustan los gatos los gatos?")
    re10=input()
    if re10=="si" or "sí":
        print("vale... ahora procederemos a calcular su resultados")
    else:
        print("vale... ahora procederemos a calcular su resultados") 
    ti()
    print("tienes",aciertos,"aciertos")
    time.sleep(1)
    print("y tienes",fallos,"fallos")
    time.sleep(2)
    print("Aquí acaba esta version de Canatar, ¿Quieres volver a jugar?")
    print("<Sí o No>")
    opf=input()