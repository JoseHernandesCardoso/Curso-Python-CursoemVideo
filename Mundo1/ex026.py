frase = input('Digite uma frase: ').lower().strip()
print(f'''A frase possui {frase.count("a")} letras A
O primeiro A aparece na posição {frase.find("a") + 1}
O ultimo A aparece na posição {frase.rfind("a") + 1}''')
