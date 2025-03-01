import os
import random
from diagramas import dibujo
from palabras import diccionario
#--------------------------------------------------------------------------------
def dibujaTablero():
  #Muestra el tablero
    os.system('cls')
    print(dibujo[len(letrasErradas)])
    print("Palabra: ",' '.join(palabra))
    print("Letras erradas: ", ', '.join(letrasErradas))
    print()
#---------------------------------------------------------------------------------
def verificarLetra(adivinar,palabraAAdivinar,letrasErradas,oportunidades):
  if adivinar in palabraAAdivinar:
    for i in range(len(palabraAAdivinar)):
        if adivinar == palabraAAdivinar[i]:
          palabra[i]=adivinar
  else:
    letrasErradas.append(adivinar)
    oportunidades-=1
#---------------------------------------------------------------------------------
def finDeJuego(oportunidades,palabra,palabraAAdivinar):
  os.system('cls')
  if oportunidades==0:
      print(dibujo[len(letrasErradas)])
      print("Perdiste el juego :(")
      return True
  if "".join(palabra) == palabraAAdivinar:
      print("Palabra: ",' '.join(palabra))
      print("¡Perdiste! no me importa que ganaras, aun asi perdiste, viejo feo.")
      return True
  else:
     return False
#----------------------------------------------------------------------------------
def muestraCategorias():
   os.system('cls')
   print("¡Bienvenido al juego del ahorcado!")
   print("Tenemos las siguientes categorias: ")
   for ca in diccionario.keys():
    print("-",ca)
   print()
#----------------------------------------------------------------------------------
def elegirCategoria():
    muestraCategorias()
    while True:
        categoria = input("Dame la categoria que quieras jugar: ")
        if categoria in diccionario.keys():
            palabra = random.choice(diccionario[categoria])
        else:
            print("No existe esa categoria. :(")
            palabra = ""
        if palabra!="":
           break
    
    return palabra
#-----------------------------------------------------------------------------------

palabraAAdivinar=elegirCategoria()
palabra = ["_"]*len(palabraAAdivinar)
#las oportunidades estan dadas por completar el muñeco
oportunidades = len(dibujo)-1
letrasErradas = []

while True:
    #Mostrar Tablero
    dibujaTablero()
    #Solicita la letra
    adivinar = input("Adivinar: ")
    verificarLetra(adivinar,palabraAAdivinar,letrasErradas,oportunidades)
    #Verificar si termino el juego
    if finDeJuego(oportunidades,palabra,palabraAAdivinar):
       break
    
    