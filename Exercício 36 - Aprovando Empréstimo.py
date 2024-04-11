print('\033[35m-=\033[m' * 20)
print('\033[31mBEM VINDO AO MINHA CASA MINHA DIVIDA\033[m')
print('\033[35m-=\033[m' * 20)
valorcasa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual seu salário: R$ '))
anos = int(input('Em quantos anos quer pagar? '))
prestação = valorcasa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valorcasa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

