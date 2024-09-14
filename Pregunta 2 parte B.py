estado_inicial = 'q0'
estados_finales = {'q0', 'q3', 'q4', 'q5'}
#TRANSICIONES
transiciones = {
    'q0': {'1': 'q0', '22': 'q1', '0': 'q3'},
    'q1': {'1': 'q1', '22': 'q2'},
    'q2': {'0': 'q2', '1': 'q3', '333': 'q5'},
    'q3': {'0': 'q4', '1': 'q0', '22': 'q3'},
    'q4': {'1': 'q3', '22': 'q4', '333': 'q5'},
    'q5': {'333': 'q5'}
}

def procesar_simbolo(estado, simbolo):
    if simbolo in transiciones[estado]:
        return transiciones[estado][simbolo]
    else:
        return estado  

def dividir_entrada(entrada):
    simbolos_validos = ['1', '22', '333', '0']
    i = 0
    entrada_dividida = []
    
    while i < len(entrada):
        simbolo_valido = False
        for simbolo in simbolos_validos:
            if entrada[i:i+len(simbolo)] == simbolo:
                entrada_dividida.append(simbolo)
                i += len(simbolo)
                simbolo_valido = True
                break
        if not simbolo_valido:
            print(f"Símbolo inválido encontrado: {entrada[i]}")
            return None  
    return entrada_dividida

def ejecutar_automata(entrada):
    global estado_inicial
    estado_inicial = 'q0'
    recorrido = [estado_inicial]

    entradas = dividir_entrada(entrada)
    
    if entradas is None:  #SIMBOLO INVALIDO
        print("contiene símbolos inválidos")
        return -1
    # Procesar cada símbolo
    for simbolo in entradas:
        estado_inicial = procesar_simbolo(estado_inicial, simbolo)
        recorrido.append(estado_inicial)
    
    # Verificar si terminó en un estado final
    if estado_inicial in estados_finales:
        print("La cadena es aceptada.")
    else:
        print("La cadena no es aceptada.")
        return -1
    
    return recorrido

cadena_entrada = '122022333' 
recorrido = ejecutar_automata(cadena_entrada)

if recorrido != -1:
    print(f"Recorrido: {recorrido}")
