import random

def choose_secret(file):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """

    words = get_file_words(file);
    word = random.choice(words)
    return word.upper()

def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """

    same_position = []
    same_letter = []

    i = 0;
    for x in word:
        j = 0;
        for y in secret:
            if x == y:
                if i == j:
                    same_position.append(i)
                else:
                    same_letter.append(i)
            j = j + 1;
        i = i + 1;

    return same_position, same_letter


def print_word():
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """


def choose_secret_advanced(file):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """

     # Obtener las palabras del fichero
    words = get_file_words(file)

    # Filtrar palabras sin acentos
    filtered_words = filter_accents(words)

    # Obtener 15 sin repeticion
    best_words = get_best_words(filtered_words)

    # Seleccionar aleatoriamente una

def get_file_words(file):
    f = open(file, mode="rt", encoding="utf-8")
    words_in_str = f.read()
    words_in_list = words_in_str.split('\n')
    f.close()

    return words_in_list

def filter_accents(words):
    return list(filter(lambda x: check_accents(x) == True , words))

def check_accents(word):
    for letter in word:
        if letter == 'á' or letter == 'é' or letter == 'í' or letter == 'ó' or letter == 'ú' or letter == '':
            return False;
    return True;

def get_best_words(words):
    pass


def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """


if __name__ == "__main__":
    secret = choose_secret()
    # Debug: esto es para que sepas la palabra que debes adivinar
    print("Palabra a adivinar: "+secret)
    for repeticiones in range(0, 6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words()
        resultado = print_word()
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)
