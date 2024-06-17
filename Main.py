from automata.pda.npda import NPDA

# Definir o NPDA
npda = NPDA(
    states={'q0', 'q1', 'q2', 'q_accept'},
    input_symbols={'0', '1'},
    stack_symbols={'0', '1', '$'},
    transitions={
        'q0': {
            '': {'$': {('q_accept', '$')}},
            '0': {'$': {('q1', '0$')}, '0': {('q1', '00')}, '1': {('q1', '10')}},
            '1': {'$': {('q1', '1$')}, '0': {('q1', '01')}, '1': {('q1', '11')}}
        },
        'q1': {
            '0': {'0': {('q1', '')}, '1': {('q1', '')}},
            '1': {'0': {('q1', '')}, '1': {('q1', '')}},
            '': {'$': {('q2', '$')}}
        },
        'q2': {
            '0': {'0': {('q2', '')}},
            '1': {'1': {('q2', '')}},
            '': {'$': {('q_accept', '$')}}
        }
    },
    initial_state='q0',
    initial_stack_symbol='$',
    final_states={'q_accept'}
)

# Testar o PDA com algumas entradas
entradas = ['0', '1', '00', '11', '010', '101', '0110', '1001']
for entrada in entradas:
    if npda.accepts_input(entrada):
        print(f'A entrada "{entrada}" é um palíndromo.')
    else:
        print(f'A entrada "{entrada}" não é um palíndromo.')