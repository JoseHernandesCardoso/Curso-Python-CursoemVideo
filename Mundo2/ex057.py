sexo = input('Digite o seu sexo [M/F]: ').upper().strip()[0]
while sexo not in ['M','F']:
    sexo = input('VALOR INVÁLIDO! Por favor, informe o seu sexo [M/F]: ').upper().strip()[0]
print(f'Sexo {sexo} cadastrado com sucesso!')
