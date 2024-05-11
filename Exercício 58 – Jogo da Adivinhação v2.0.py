from random import randint
from colorama import Fore, init
computador = randint(0, 10)
print(Fore.BLUE+'''Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que voçê conseque adivinhar qual foi? ''')
init(autoreset=True)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input(Fore.LIGHTMAGENTA_EX+'Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} palpites'.format(palpites))
