peso = float(input('Qual o seu peso? (Kg) '))

altura = float(input('Qual e a sua altura? (m) '))

imc = peso / (altura ** 2)

print('O seu IMC e de {:.1f}'.format(imc))

if imc < 18.5:

    print('Voce esta ABAIXO do peso normal')

elif 18.5 <= imc < 25:

    print('PARABENS, voce esta na faixa de PESO NORMAL')

elif 25 <= imc < 30:

    print('Voce esta em SOBREPESO')

elif 30 <= imc < 40:

    print('Voce esta em OBESIDADE')

elif 40 <= imc:

    print('Voce esta em OBESIDADE MORBIDA, cuidado!')
