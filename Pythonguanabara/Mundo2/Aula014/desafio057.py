sexo = ''

sexo = str(input('informe seu sexo: [M/F]  ')).upper().strip()

while sexo not in 'MFmf' or sexo == '':
    
    sexo = str(input('Dado invalido! informe seu sexo: [M/F]  ')).upper().strip()

print('Dados confirmado!')
