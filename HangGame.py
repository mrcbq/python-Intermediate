import os
import random

def run():
    words = []
    # os.system('cls')
    print('Welcome to the Hang Man Gam3\nTry to find the secret word')
    word = input('Stroke an letter and press Enter\n\n\n')
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    print(words)








if __name__ == '__main__':
    run()