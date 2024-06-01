from colorama import init, Fore
init(autoreset=True)


print(Fore.BLUE+'=' * 30)
print(Fore.RED+'{:^30}'.format('BANK-RANSOM'))
print(Fore.BLUE+'=' * 30)
valor = int(input('Que valor voçê quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print(Fore.YELLOW+'Volte sempre ao BANK RANSOM bom dia.')
