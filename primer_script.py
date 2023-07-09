import threading
import os
import random
import time
from pynput import keyboard

lista = []
lista.append('.------------------------------.')
for i in range(20):
    lista.append('|                              |')
lista.append('.------------------------------.')

#VARIABLE GLOBALES
posx = random.randint(0,19)
posy = random.randint(0,14)

x_comida = 0
y_comida = 0

keyUp = True
keyDown = True
keyLeft = True
keyRight = True

gusano = []
cola = []

def dibujar():
    os.system('cls')

    if len(gusano) == 0:
        pass
    else:
        
        for ix, iy in gusano:
            posx = ix+1
            posy = (iy+1)*2-1
            lista_char = list(lista[posx])
            lista_char[posy]='['
            lista_char[posy+1]=']'
            nueva_cad = "".join(lista_char)
            lista[posx] = nueva_cad
            pass
        
    for i in lista:
        print(i)
    print(posx,'\t',x_comida)
    print(posy,'\t',y_comida)
    print(gusano)
    print('cola:',cola)

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
    gusano.append([x,y])
    

def borrar_cubo(x, y):
    global cola
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
    cola = gusano.pop(0)

def cubos_aleatorios():
    #while True:
    global x_comida, y_comida
    x_comida = random.randint(0,19)
    y_comida = random.randint(0,14)
    colocar_cubo(x_comida,y_comida)
    dibujar()
    #time.sleep(10)

def comprobar_si_comio():
    global posx, posy
    global gusano
    if posx == x_comida and posy == y_comida:
        gusano.insert(0,cola)
        
    




def on_press(key):
    global posx, posy
    global keyUp
    global keyDown 
    global keyLeft 
    global keyRight 
    if key == keyboard.Key.right and keyRight == True:
        if posy != 14:
            borrar_cubo(posx,posy)
            posy+=1
            colocar_cubo(posx,posy)
            keyRight = False
            comprobar_si_comio()
            
            dibujar()
            
    elif key == keyboard.Key.left and keyLeft == True:
        if posy != 0:
            borrar_cubo(posx,posy)
            posy-=1
            colocar_cubo(posx,posy)
            keyLeft = False
            comprobar_si_comio()
            dibujar()
    elif key == keyboard.Key.up and keyUp == True:
        if posx != 0:
            borrar_cubo(posx,posy)
            posx-=1
            colocar_cubo(posx,posy)
            keyUp = False
            comprobar_si_comio()
            dibujar()
    elif key == keyboard.Key.down and keyDown == True:
        if posx != 19:
            borrar_cubo(posx,posy)
            posx+=1
            colocar_cubo(posx,posy)
            keyDown = False
            comprobar_si_comio()
            dibujar()
    
    
def on_release(key):
    global keyUp
    global keyDown 
    global keyLeft 
    global keyRight 
    try:
        if key == keyboard.Key.up:
            keyUp = True
        elif key == keyboard.Key.down:
            keyDown = True
        elif key == keyboard.Key.left:
            keyLeft = True
        elif key == keyboard.Key.right:
            keyRight = True
        if key == keyboard.Key.esc:
            # Si se presiona la tecla Esc, se detiene el programa
            return False
    except AttributeError:
        pass    

# Configuramos el listener

colocar_cubo(posx,posy)
dibujar()
cubos_aleatorios()
#mi_hilo = threading.Thread(target=cubos_aleatorios)
#mi_hilo.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print('Hola mundo')




