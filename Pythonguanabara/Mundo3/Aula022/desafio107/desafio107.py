import moeda

valor = float(input('Digite um valor: R$'))

print(f'Com um aumento de 50%, temos R${moeda.aumentar(valor, 50)}')
print(f'O dobro de R${valor}, temos R${moeda.dobro(valor)}')
print(f'A metade de R${valor}, temos R${moeda.metade(valor)}')
