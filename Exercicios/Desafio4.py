#DESAFIO4#
a = input('Escreve algo:')

print('É um número? {}'.format(a.isnumeric()))
print('É uma letra? {}'.format(a.isalpha()))
print('Tem letras e números? {}'.format(a.isalnum()))
print('Está escrito em letras maiusculas? {}'.format(a.isupper()))
print('Está escreito em letras minusculas? {}'.format(a.islower()))
print('É um número decimal? {}'.format(a.isdecimal()))
