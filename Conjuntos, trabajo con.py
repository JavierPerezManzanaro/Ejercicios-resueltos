verano = set(['acelga', 'apio', 'espinaca', 'repollo', 'lechuga'])
otono = set(['acelga', 'ajo', 'apio', 'cebolla', 'lechuga', 'papa'])
invierno = set(['pimentón', 'acelga', 'ají', 'espinaca', 'lechuga'])
primavera = set (['albahaca', 'acelga', 'cebolla', 'lechuga', 'tomate'])


verano = set(verano)
otono = set(otono)
invierno = set(invierno)
primavera = set(primavera)

todas = verano | otono | invierno | primavera
print(f'¿Cuántas plantas distintas hay? {len(todas)}')

todo_ano = verano & otono & invierno & primavera
print(f'¿Qué plantas se pueden sembrar todo el año? {todo_ano}')

primavera_verano = (verano | primavera) -otono - invierno
print(
    f'¿Qué plantas son exclusivamente de primavera y verano? {primavera_verano}')
