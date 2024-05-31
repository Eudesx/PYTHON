from random import randint
vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voçê venceu!')
            vitoria += 1
        else:
            print('Voçê perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voçê VENCEU!')
            vitoria += 1
        else:
            print('Voçê PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voçê venceu {vitoria} vezes.')



