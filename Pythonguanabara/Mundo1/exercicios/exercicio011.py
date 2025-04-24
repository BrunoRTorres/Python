largura = float(input('Digite a largura da parede: '))

altura = float(input('Digite a altura da parede: '))

area = largura * altura

tinta = area / 2

print('Sua parede tem a dimensao de {}x{} e sua area e de {}m²'.format(largura, altura, area))

print('Para pintar essa parede, voce precisara de {:.2f}L de tinta'.format(tinta))
