from time import sleep
from colorama import Fore

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    sleep(0.5)
    print(Fore.BLUE+'{} '.format(c), end='-> ')
print('ACABOU!')
