velocidade = float(input('Qual a velocidade atual do caro? '))
if velocidade > 80:
    print('MULTADO! Voçê excedeu o limete permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('VoçÊ deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança! ')
