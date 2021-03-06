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
            if len(x) != len(y):
                raise ValueError("La longitud de las palabras es distinta");
            if x == y:
                if i == j:
                    same_position.append(i)
                else:
                    same_letter.append(i)
            j = j + 1;
        i = i + 1;

    return same_position, same_letter


def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    if str(type(same_letter)) != '<class \'list\'>' or str(type(same_letter_position)) != '<class \'list\'>':
        raise ValueError("No son listas");
            
    if len(same_letter_position) > len(word):
        raise ValueError("La longitud es mayor")
    
    if len(same_letter) > len(word):
        raise ValueError("La longitud es mayor")

    transformed_list = [];
    for letter in word:
        transformed_list.append("-");
    
    for i in same_letter_position:
        if i < 0:
            raise ValueError("Es negativo")
        transformed_list[i] = word[i].upper();
    
    for i in same_letter:
        if i < 0:
            raise ValueError("Es negativo")
        transformed_list[i] = word[i].lower();

    transformed = "" 
    for l in transformed_list: 
        transformed += l 
    return str(transformed)

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

    if len(words) < 15:
        raise ValueError("No hay palabras suficientes");
    
    # Filtrar palabras sin acentos
    filtered_words = filter_accents(words)

    # Obtener 15 sin repeticion
    selected = get_best_words(filtered_words)

    # Seleccionar aleatoriamente una
    secret = random.choice(selected).upper()

    return selected, secret

def get_file_words(file):
    f = open(file, mode="rt", encoding="utf-8")
    words_in_str = f.read()

    if len(words_in_str) == 0:
        raise ValueError("No hay palabras");

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
    res = [];
    filtered_words = list(filter(lambda x: len(x) == 5, words));
    while len(res) < 15:
        random_word = random.choice(filtered_words);
        if res.count(random_word) == 0:
            res.append(random_word);
    return res;

def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    while 1:
        word = input("Introduce una palabra: ").lower()
        print(selected)

        if selected.count(word) != 0:
            return word.upper();

if __name__ == "__main__":
    #secret = choose_secret('palabras_reduced.txt')
    try:
        selected, secret = choose_secret_advanced('palabras_extended.txt')

        # Debug: esto es para que sepas la palabra que debes adivinar
        print("Palabra a adivinar: "+secret)
        for repeticiones in range(0, 6):
            word = check_valid_word(selected)
            same_position, same_letter = compare_words(word, secret)
            resultado = print_word(word, same_position, same_letter)
            print(resultado)

            if word == secret:
                print("HAS GANADO!!")
                exit()
        print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)
    except BaseException as e:
        print(e)
