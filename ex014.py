c = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9 * c) / 5) + 32
print('A temperatura de {}°C corresponde a {} °Fahrenheit!'.format(c, fahrenheit))

if fahrenheit > 100:
    print('Pegando fogo!')
else:
    print('Esta suave! :)')

