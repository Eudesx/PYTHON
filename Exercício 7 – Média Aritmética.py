nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A media do aluno e {:.1f}'.format(media))

if media < 5.0:
    print('REPROVADO')
if media >= 5.00:
    print('APROVADO')

# {:.1f} Arredonda para cima de acordo com as regras algébricas
