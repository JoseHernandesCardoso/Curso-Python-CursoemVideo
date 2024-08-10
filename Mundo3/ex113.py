def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            num = 0
            print('\n\033[0;31mERRO: o usuário preferiu não digitar o número\033[m')
            return num
        except:
            print('\033[0;31mERRO: digite um NÚMERO INTEIRO válido\033[m')
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except KeyboardInterrupt:
            num = 0
            print('\n\033[0;31mERRO: o usuário preferiu não digitar o número\033[m')
            return num
        except:
            print('\033[0;31mERRO: Digite um NÚMERO REAL válido\033[m')
        else:
            return num


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}')
