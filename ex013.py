salario = float(input('Qual seu salário atual R$?'))
novo = salario + (salario * 15 / 100)
print('Seu salário atual é {} mais com os 15% de aumento vai para {}'.format(salario, novo))

quantidade_de_filho = int(input('Quantos filhos voçê tem?'))

if quantidade_de_filho > 0:
    salario_final = novo + (novo * 5 / 100)
    print('Seu novo salario com o acressimo de {} filho(s) sera de {:.2f}'.format(quantidade_de_filho, salario_final))


