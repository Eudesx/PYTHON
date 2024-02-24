dig = input('Digite algo: ')

print('Ele é alfanúmerico? ', end='')
print(dig.isalnum())

print('Ele e númerico? ', end='')
print(dig.isnumeric())

print('Ele está em ninúscula? ', end='')
print(dig.islower())

print('Eles são todos caracteres ascii? ', end='')
print(dig.isascii())

print('Ela está só em letras do alfabeto? ', end='')
print(dig.isalpha())

print('Eles são todos númeroas decimais ?', end='')
print(dig.isdecimal())

print('Todos os caracteres são digitos? ', end='')
print(dig.isdigit())

print('O tipo primitivo desse valor é? ', end='')
print(type(dig))

print('E somente espaços? ', end='')
print(dig.isspace())

print('Ele está capitalizado? ', dig.istitle())

