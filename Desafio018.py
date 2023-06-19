print('Faça um programa que leia um angulo qualquer e mostre na tela'
      'o valor do seno, cosseno e tangente desse angulo')

import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin((math.radians(angulo)))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan((math.radians(angulo)))
print('Ângulo de SENO:{:.2f}\nÂngulo de COSSENO:{:.2f}\nÂngulo da TANGENTE:{:.2f}'.format(seno, cosseno, tangente))

#Segunda forma
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo desejado: '))
seno = sin((math.radians(angulo)))
cosseno = cos(math.radians(angulo))
tangente = tan((math.radians(angulo)))
print('Ângulo de SENO:{:.2f}\nÂngulo de COSSENO:{:.2f}\nÂngulo da TANGENTE:{:.2f}'.format(seno, cosseno, tangente))
