import os
import random

def run():
    os.system('cls')
    words = [] # lista para recibir las palabras secretas
    print('Welcome to the Hang Man Gam3\nTry to find the secret word\n') # Presentacion inicial del juego
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f: # Apertura del archivo de texto en modo de solo lectura
        for line in f: # Se va a leer cada linea x separado para poder eliminar los saltos de linea y espacios
            words.append(line.strip()) # Se agrega cada linea sin espacios o saltos de linea a la lista words[]
    secret = random.sample(words, k=1) # Se escoge solo una palabra secreta dentro del listao de palabras disponible
    secret = secret[0] # Se castea la plabra de una lista a un string, ya que se requiere solamente la palabra
    changes = secret.maketrans('áéíóúAEIOU', 'aeiouaeiou') # Se realiza la devolucion del string sin mayusculas o tildes, 
    # print(changes) #  Lo use para visualizar la salida del metodo maketrans, el cual es un objeto que sirve para hacer una transformacion del texto 
    secret = secret.translate(changes) # Realiza el cambio en el string secret segun la transformacion realizada con el metodo maketrans()
    # secret = enumerate(secret) # Enumerate() devuelve el indice y el valor en un objeto iterable
    # secret = dict(secret) # creo un diccionario con el indice y el valor de la palabra secreta
    pos = ['_'for i in range(len(secret))] # Lista para recoger las posiciones iguales entre la palabra digitada por el usuario y la palabra secreta
    lifes = len(secret)
    while lifes > 0:
        print('Remain Lifes are ', lifes)
        word = input('Stroke an letter and press Enter: ')
        word = word.translate(changes) #Le quito las mayusculas o tildes a la plabra digitada por el usuario

        for key in range(len(secret)): #recorro la palabra secreta para verificar si la letra introducida por el usuario esta en la palabra.
            if secret[key] == word:
                pos[key] = word #Si la letra esta en la palabra la alimento en la posicion en la que esta.

        print(''.join(pos))

        lifes -= 1
        print(secret)

        # print(word)




if __name__ == '__main__':
    run()