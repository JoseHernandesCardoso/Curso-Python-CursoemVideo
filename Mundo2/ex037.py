print('-=-' * 20)
num = int(input('digite um número inteiro: '))
print('-=-' * 20)
print('''Converter para...
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opc = int(input('Digite o valor da sua opção: '))
print('-=-' * 20)

if opc == 1:
    valor = str(bin(num))[2:]
    tipo = 'binário'
elif opc == 2:
    valor = str(oct(num))[2:]
    tipo = 'octal'
elif opc == 3:
    valor = str(hex(num))[2:]
    tipo = 'hexadecimal'

print(f'\033[32mO valor {num} convertido de decimal para {tipo} é de {valor}.\033[m')
