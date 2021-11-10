import random
from words import palabras
import string

def valid(palabras):
    palabra = random.choice(palabras) #se elige una palabra al azar
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def hangman():
    palabra = valid(palabras) #word
    letras = set(palabra) #letras en la palabra #word_letters
    alfabeto = set(string.ascii_uppercase) #alphabeth
    utilizadas = set() #letras adivinadas #used_letters

    vidas = 7

    #obteniendo ingresos de usuario
    while len(letras) > 0 and vidas >0:
        #letras utilizadas
        #' '.join.(['a','b', 'cd']) --> 'a,b,cd'
        print('Tienes', vidas, 'vidas restantes. Haz utilizado estas letras: ',' '.join(utilizadas))

        #palabra actual
        lista = [letra if letra in utilizadas else '-' for letra in palabra]
        print('Palabra actual: ', ' '.join(lista))

        ingresadas = input('Adivine una letra: ').upper() 
        if ingresadas in alfabeto - utilizadas:
            utilizadas.add(ingresadas)
            if ingresadas in letras:
                letras.remove(ingresadas)

            else:
                vidas = vidas - 1 #se quita una vida si no esta la letra
                print('Letra equivocada.')

        elif ingresadas in utilizadas:
            print('Ya utilzaste esa letra. Intenta de nuevo.')

        else:
            print('Ingresaste una letra equivocada. Intenta de nuevo.')

    #cuando letras == 0 or vidas == 0
    if vidas == 0:
        print('Perdiste, lo siento. La palabra era', palabra )
    else:
        print('Adivinaste la palabra', palabra, '!!')

hangman()
#ingreso = input('Escribe algo: ')