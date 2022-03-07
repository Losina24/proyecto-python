import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado = [] # La inicialización del array tiene que hacerse antes, porque si no se sobreescribe cada vez que se itera el diccionario
    for clave in diccionario:
        for palabra in diccionario[clave]:
            print(palabra[0])
            if palabra[0] < letra:
                #resultado=[]
                resultado.append(palabra)
    return resultado


def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    """ clients_list[nif] = {
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    } """
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
    }

    # El problema estaba en nif: {..., ya que los valores de name, address, phone y email se estaban añadiendo dentro del diccionario nif y no dentro de la propia lista clients_list

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    #for i in range(1,repeticiones+1):
    # Se estaba ejecutando el bucle con un límite superior al número de repeticiones, por lo que se salia del array.
    for i in range(1,repeticiones):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+i] = []
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            lista = combinaciones.get("repeticion" + i);
            combinaciones["repeticion"+i] = lista.append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    
