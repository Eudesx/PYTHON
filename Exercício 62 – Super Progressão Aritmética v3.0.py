from colorama import Fore, init
init(autoreset=True)

print(Fore.YELLOW+'Gerador de PA')
print(Fore.RED+'-=' * 10)
primeiro = int(input(Fore.LIGHTMAGENTA_EX+'Primeiro termo: '))
razão = int(input(Fore.LIGHTMAGENTA_EX+'Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voçê quer mostar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
