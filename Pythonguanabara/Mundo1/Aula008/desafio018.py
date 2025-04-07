from math import radians, cos, sin, tan

angulo = float(input('Digite um angulo: '))

seno = sin(radians(angulo))

cosseno = cos(radians(angulo))

tangente = tan(radians(angulo))

print('O angulo {} tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
