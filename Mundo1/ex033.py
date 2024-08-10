n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

# Verificar menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# Verificar maior
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'''O maior número foi digitado foi {maior}
O menor número digitado foi {menor}''')
