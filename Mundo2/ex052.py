primo = True
n = int(input('Digite um valor: '))
for c in range(2, n):
    if n % c == 0 and n != c:
        primo = False
if n == 1:
    print('O número digitado NÃO É primo')
elif primo:
    print('O número digitado É primo')
else:
    print('O número digitado NÃO É primo')
