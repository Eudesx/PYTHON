from colorama import Fore, init
init(autoreset=True)
print(Fore.RED+'-' * 30)
print(Fore.GREEN+'Sequência de fibonacci')
print(Fore.RED+'-' * 30)
n = int(input('Quantos termos voçê quer mostrar? '))
t1 = 0
t2 = 1
print(Fore.RED+'~' * 30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
