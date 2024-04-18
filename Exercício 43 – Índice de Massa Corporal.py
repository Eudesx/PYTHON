peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voçê está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, voçê está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Voçê está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Voçê esta em OBESIDADE!')
elif imc >= 40:
    print('Voçê está em OBESIDADE MÓRBIDA, cuidado!')


