import threading
import os
#import time
import random
from pynput import keyboard

lista = []
lista.append('.------------------------------.')
for i in range(20):
    lista.append('|                              |')
lista.append('.------------------------------.')

#variables globales
x_actual = 0
y_actual = 0


def dibujar():
    os.system('cls')
    for i in lista:
        print(i)
    
        #time.sleep(0.2)

#mi_hilo = threading.Thread(target=dibujar)
#mi_hilo.start()
dibujar()
    
def colocar_cubo(x, y):
    posx = x+1
    posy = (y+1)*2-1
    #nos ubicamos en la fila
    lista_char = list(lista[posx])
    #nos ubicamos en la columna y modificamos
    lista_char[posy]='['
    lista_char[posy+1]=']'
    #unimos la cadena
    nueva_cad = "".join(lista_char)
    lista[posx] = nueva_cad
    

def borrar_cubo(x, y):
    posx = x+1
    posy = (y+1)*2-1
    #nos ubicamos en la fila
    lista_char = list(lista[posx])
    #nos ubicamos en la columna y modificamos
    lista_char[posy]=' '
    lista_char[posy+1]=' '
    #unimos la cadena
    nueva_cad = "".join(lista_char)
    lista[posx] = nueva_cad
    
def cubos_aleatorios():
    while True:
        x = random.randint(0,19)
        y = random.randint(0,14)
        colocar_cubo(x,y)
        #time.sleep(0.3)

def cubos_lluvia():
    while True:
        numero_aleatorio = random.randint(0, 14)
        for i in range(0,20):
            if i == 0:
                colocar_cubo(i, numero_aleatorio)
                #time.sleep(0.5)
            elif i==19: 
                colocar_cubo(i, numero_aleatorio)
                #time.sleep(0.5)
                borrar_cubo(i,numero_aleatorio)
            else: 
                borrar_cubo(i-1,numero_aleatorio)
                colocar_cubo(i, numero_aleatorio)
                #time.sleep(0.5)
                borrar_cubo(i,numero_aleatorio)

def cubo_espiral():
    minx = 0
    maxx = 20
    miny = 0
    maxy = 15

    for i in range(8):
        for x in range(minx,maxx):
            colocar_cubo(x,miny)
            #time.sleep(0.5)
        for y in range(miny+1,maxy):
            colocar_cubo(maxx-1,y)
            #time.sleep(0.5)
        for x in range(maxx-2,minx-1,-1):
            colocar_cubo(x, maxy -1)
            #time.sleep(0.5)
        for y in range(maxy-2,miny,-1):
            colocar_cubo( minx,y)
            #time.sleep(0.5)
        minx+=1
        maxx-=1
        miny+=1
        maxy-=1




posx = random.randint(0,19)
posy = random.randint(0,14)
colocar_cubo(posx,posy)
dibujar()
def detectar_teclas():


    def on_press(key):
        global posx, posy
        if key == keyboard.Key.right:
            if posy != 14:
                borrar_cubo(posx,posy)
                posy+=1
                colocar_cubo(posx,posy)
                
        elif key == keyboard.Key.left:
            if posy != 0:
                borrar_cubo(posx,posy)
                posy-=1
                colocar_cubo(posx,posy)
        elif key == keyboard.Key.up:
            if posx != 0:
                borrar_cubo(posx,posy)
                posx-=1
                colocar_cubo(posx,posy)
        elif key == keyboard.Key.down:
            if posx != 19:
                borrar_cubo(posx,posy)
                posx+=1
                colocar_cubo(posx,posy)
        dibujar()
        

    # Configuramos el listener


    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

mi_hilo2 = threading.Thread(target=detectar_teclas)
mi_hilo2.start()




posix = random.randint(0,19)
posiy = random.randint(0,14)
colocar_cubo(posix,posiy)
dibujar()

while True:
    if posx == posix and posiy == posy:
        posix = random.randint(0,19)
        posiy = random.randint(0,14)
        colocar_cubo(posix,posiy)
        dibujar()
    else:
        pass






    



      

            

