def leiaInt(msg):
    while True:
        r = input(msg).strip()
        if r.isnumeric():
            return r
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
