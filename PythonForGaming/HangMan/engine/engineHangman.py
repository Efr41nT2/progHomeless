import random
import os
from engine.palabras import lista_palabras


class HangMan:
    def obtenerPalabra(self):
        word = random.choice(lista_palabras)
        return word.upper()

    def jugar(self, palabra):
        palabra_completada = '_' * len(palabra)
        adivinado = False
        letra_adivinada = []
        palabra_adivinada = []
        intentos = 6
        print('Bienvenidos al ahorcado criollo en su versión 0.1 destruction')
        print(self.dibujar(intentos))
        print(palabra_completada)
        print('\n')
        while not adivinado and intentos > 0:
            adivinar = input('Ingrese una palabra o letra para adivinar: ').upper()
            clear = lambda: os.system('clear') #on Linux System
            clear()
            if len(adivinar) == 1 and adivinar.isalpha():
                if adivinar in letra_adivinada:
                    print('ya adivinaste la letra', adivinar)
                elif adivinar not in palabra:
                    print(adivinar, 'no esta en la palabra.')
                    intentos -= 1
                    letra_adivinada.append(adivinar)
                else:
                    print('Buen Trabajo', adivinar, "esta en la palabra")
                    letra_adivinada.append(adivinar)
                    pal_com_lista = list(palabra_completada)
                    indices = [i for i, letra in enumerate(palabra) if letra == adivinar]
                    for index in indices:
                        pal_com_lista[index] = adivinar
                        palabra_completada = "".join(pal_com_lista)
                    if "_" not in palabra_completada:
                        adivinado = True
            elif len(adivinar) == len(palabra) and adivinar.isalpha():
                if adivinar in palabra_adivinada:
                    print('ya adivinaste la palabra', adivinar)
                elif adivinar != palabra:
                    print(adivinar, "no es la palabra")
                    intentos -= 1
                    palabra_adivinada.append(adivinar)
                else:
                    adivinado = True
                    palabra_completada = palabra
            else:
                print('no es una suposición válida.')
            print(self.dibujar(intentos))
            print(palabra_completada)
            print('\n')
        if adivinado:
            print('felicidades mija, adivinaste la palabra, eres todo un main singed')
        else:
            print('lo siento kakaroto, te quedaste sin intento. la palabra fue ' + palabra + ' quisas adivines la próxima')

    def dibujar(self, intentos):
        # motrar el dibujo clasico del juego
        etapas = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
        ]
        return etapas[intentos]
