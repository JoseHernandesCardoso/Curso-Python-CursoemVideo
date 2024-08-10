cidade = input('Digite o nome de uma cidade: ').lower()
cidade_spl = cidade.split()
print(f'A o nome da cidade começa com "Santo": {"santo" in cidade_spl[0]}')
