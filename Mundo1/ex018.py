from math import cos, sin, tan, radians

angulo = int(input('Digite um ângulo: '))
radianos = radians(angulo)

sin = sin(radianos)
cos = cos(radianos)
tan = tan(radianos)

print(f'O seno de {angulo} é {sin:.2f} \nO cosseno de {angulo} é {cos:.2f} \nA tangente de {angulo} é {tan:.2f}')
