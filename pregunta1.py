# Definir la función de transición δ como un diccionario
transitions = {
    ('q0', 'posicionar'): 'q1',
    ('q1', 'llenar'): 'q2',
    ('q1', 'error_llenado'): 'q0',
    ('q2', 'tapar'): 'q3',
    ('q2', 'error_tapado'): 'q1',
    ('q3', 'etiquetar'): 'q4',
    ('q3', 'error_etiquetado'): 'q2',
    ('q4', 'empaquetar'): 'q5',
    ('q4', 'error_empaquetado'): 'q3',
    ('q5', 'empaquetar'): 'q5'
}
# Estado inicial
initial_state = 'q0'
# Estados finales
final_states = {'q5'}
# Función para procesar una secuencia de entradas
def process_inputs(inputs):
    current_state = initial_state
    print(f"Estado inicial: {current_state}")
    for symbol in inputs:
        print(f"Procesando: {symbol}")
        # Obtener el siguiente estado basado en la entrada
        next_state = transitions.get((current_state, symbol))
        if next_state:
            current_state = next_state
            print(f"Transición a: {current_state}")
        else:
            print(f"Transición no definida para ({current_state}, {symbol})")
            return False
    print(f"Estado final: {current_state}")
    return current_state in final_states
# Ejemplo de cadenas que recibe el sistema
inputs_list = [
    ['posicionar', 'llenar', 'tapar', 'etiquetar', 'empaquetar'],
    ['posicionar', 'llenar', 'tapar', 'error_tapado', 'etiquetar', 'empaquetar'],
    ['posicionar', 'llenar', 'error_llenado', 'posicionar', 'tapar', 'etiquetar', 'empaquetar'],
    ['posicionar', 'llenar', 'tapar', 'etiquetar']
]
for inputs in inputs_list:
    print(f"Procesando la secuencia: {inputs}")
    if process_inputs(inputs):
        print("Secuencia aceptada.")
    else:
        print("Secuencia no aceptada.")
    print()