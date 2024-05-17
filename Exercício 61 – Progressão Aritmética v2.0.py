from colorama import Fore, init
init(autoreset=True)

print(Fore.YELLOW+'Gerador de PA')
print(Fore.RED+'-=' * 10)
primeiro = int(input(Fore.LIGHTMAGENTA_EX+'Primeiro termo: '))
razão = int(input(Fore.LIGHTMAGENTA_EX+'Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')


