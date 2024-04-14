from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))

print('''[ m ] - masculino [ f ] - feminino''')
sexo = input('Qual seu sexo? ').strip().upper()

if sexo == 'M':
    print('MASCULINO obrigatorio servir!')
elif sexo == 'F':
    print('FEMININO não é obrigatorio servir!')
else:
    print('RESPOSTA INVALIDA!')


idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voçê já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

