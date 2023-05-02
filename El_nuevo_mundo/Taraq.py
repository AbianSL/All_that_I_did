import random
import textwrap
import time
import sys
from funciones import *

opf="si"
while opf=="si":
    print("???-Hola, las siguientes opciones que vas a elegir no se podrán cambiar durante el juego")
    pint_lineadis(width=75)
    time.sleep (5)
    print ("||ELIGE UNA RESPUESTA||")
    print("-¿Quién eres? [1]")
    print("-¿Qué quieres? [2]")
    opone=int(input())
    if opone==1:
        print("???-Soy un indigente que quiere hacerte algunas preguntas")
        time.sleep (4)
        print("-Pero ¿Dónde estoy?")
        time.sleep (2)
        print("???-Estás en una sala especial para hacerte unas preguntas, ya sabrás donde estarás en el futuro")
        time.sleep (9)
        print("-¿Por qué quieres hacerme preguntas?")
        time.sleep (5)
        print("YO-Porque eso voy a hacer")
        time.sleep (3)
        print("YO-asi que escucha bien las preguntas")
        time.sleep (5)
        print("- ...")
        time.sleep (2)
    elif opone==2:
        print("???-Yo quiero preguntarte algunas cosas")
        time.sleep (3)
        print("-¿Cómo qué?")
        time.sleep (1)
        print("???-Como Quien eres")
        time.sleep (1)
        print("-¿En serio que eso es una pregunta?")
        time.sleep (3)
        print("???-sí")
        time.sleep (1)
        print("-entonces te pregunto lo mismo que tú quieres preguntarme ¿Quién eres?")
        time.sleep (5)
        print("???-Soy un indigente que quiere hacerte algunas preguntas")
        time.sleep (4)
        print("-¿Por que quieres hacerme preguntas?")
        time.sleep (3)
        print("???-Porque quiero hacerte preguntas")
        time.sleep (3)
        print("-¿¿Qué??")
        time.sleep (1)
        print ("???-Perdón a veces se me va la cabeza...")
        time.sleep (4)
        print("???-Quiero hacerte preguntas para conocernos, ah si, te lo voy adelantando")
        time.sleep (5)
        print("???-Me puedes llamar YO")
        time.sleep (3)
        print("-¿¿YO?? ¿Qué clase de nombre es ese?")
        time.sleep (3)
        print("YO-Un nombre, ahora soy yo quien te hace las preguntas,¿vale?")
        time.sleep (4)
        print("-Vale...")
        time.sleep (1)
    else:
        print ("-¿¿¿Queeeee???")
        Errores=1
    #elección de sexo 
    opSex="no"
    while opSex=="no":
        print ("YO-¿Eres chico o chica?")
        sex=input()
        if sex=="chico":
            print ("YO-¿Estás seguro?")
            opSex=input()
            pint_lineadis(width=75)
        elif sex=="chica":
            print ("YO-¿Estás segura?")
            opSex=input()
            pint_lineadis(width=75)
        else:
            pint_lineadis(width=75)
    if sex=="chico":
        #elección del nombre    
        op2="no"
        while op2=="no":
            print("¿cómo te llamas? ")
            nombre=input()
            print ("¿estás seguro de que así te llamas? ")
            op2=input()
            if op2=="no":
                print()
            else:
                print("Apartir de ahora te llamarás "+nombre)
        #elección de la clase
        pint_lineadis(width=75)
        print("YO- Estamos en un mundo donde existen varias clases y tambien diversas razas")
        time.sleep(6)
        print("YO- Existen tres clases: magos, arqueros, y guerreros")
        pint_lineadis(width=75)
        time.sleep(5)
        op3="no"
        while op3=="no":
            print ("YO- Escoge entre una de estas tres clases ")
            clase=input()
            if clase=="mago":
                print("Los magos tienen unos poderes increibles e inteligencia, una sabia desición")
            elif clase=="arquero":
                print("Los arqueros son agiles y con habilidades fantástitcas para el desplazamiento, una sabia desición")
            elif clase=="guerrero":
                print("Los guerreros son fuertes y resistentes, una sabia desición")
            else:
                print("vuelve a intentarlo")
                op3="no"
            time.sleep (3)
            print ("¿estás seguro de escoger esta clase? ")
            op3=input()
            if op3=="no":
                print()
            else:
                pint_lineadis(width=75)
    elif sex=="chica":
        #elección del nombre 
        op2="no"
        while op2=="no":
            print("¿cómo te llamas? ")
            nombre=input()
            print ("¿estás segura de que así te llamas? ")
            op2=input()
            if op2=="no":
                print()
            else:
                print("Apartir de ahora te llamarás "+nombre)
                time.sleep (2)
        #elección de la clase
        pint_lineadis(width=75)
        print("YO- Estamos en un mundo donde existen varias clases y tambien diversas razas")
        time.sleep(6)
        print("YO- Existen tres clases: magas, arqueras, y guerreras")
        time.sleep(5)
        pint_lineadis(width=75)
        op3="no"
        while op3=="no":
            print ("YO- Escoge entre una de estas tres ")
            clase=input()
            if clase=="maga":
                print("Las magas tienen unos poderes increibles e inteligencia, una sabia desición")
            elif clase=="arquera":
                print("Las arqueras son agiles y con habilidades fantástitcas para el desplazamiento, una sabia desición")
            elif clase=="guerrera":
                print("Las guerreras son fuertes y resistentes, una sabia desición")
            else:
                print("vuelve a intentarlo")
                op3="no"
                Errores=Errores+1
            time.sleep (3)
            print ("¿estás segura de escoger esta clase? ")
            
            op3=input()
            if op3=="no":
                pint_lineadis(width=75)
            else:
                pint_lineadis(width=75)
    else:
        print("se ha producido un error... esto en teoria no debería pasar...")
        Errores= Errores+1
    print ("YO-¿Qué raza quieres ser?")
    print ("YO- hay nueve razas en total")







    print("¿quieres volver a jugar? <sí o no> ")
    opf=input()
    pint_lineadis(width=75)
  