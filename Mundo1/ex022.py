nome = input('Digite um nome completo: ').strip()
nomeu = nome.upper()
nomel = nome.lower()
nome_letras = len(nome.replace(' ', ''))
nome_split = nome.split()
primeiro_letras = len(nome_split[0])
print(f'''O nome {nome}...

Escrito em maiúsculas fica: {nomeu};
Escrito em minusculas fica: {nomel};
Possui {nome_letras} letras;
Possui {primeiro_letras} letras no primeiro nome.''')