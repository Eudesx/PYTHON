def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuário preferiu não digitar esse número..\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31musuário preferiu não digitar esse número..\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor digitado inteiro foi {n1} e o real foi {n2} ')
