nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiscúla é {}'.format(nome.upper()))  # Tranforma todo nome em maiúscula
print('Seu nome em minúscula é {}'.format(nome.lower()))  # Tranforma todo nome em minúsculas
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))  # Faz a contagem de números das letras
#print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

