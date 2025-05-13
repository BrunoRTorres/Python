soma = 0

cont = 0

for c in range(1, 501, 2):
    
    if c % 3 == 0:
        
        soma += c

        cont += 1

print('A soma entre os {} numeros impares divisiveis por 3 e {}'.format(cont, soma))
