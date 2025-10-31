
#? primeiro exercicio

# numero = input('Digite um numero inteiro: ')

# try:
#     numero_int = int(numero)
#     par = numero_int % 2 == 0
#     impar = numero_int % 2 == 1
    
#     if par:
#         print(f'O numero {numero} e par')
    
#     if impar:
#         print(f'O numero {numero} e impar')
# except:
#     print('Nao foi digitado um numero inteiro')

#? Segundo exercicio

# horas = input('Digite as horas: ')

# try:
#     horas_int = int(horas)
#     bom_dia = horas_int >= 0 and horas_int <= 11
#     boa_tarde = horas_int >= 12 and horas_int <= 17
#     boa_noite = horas_int >= 18 and horas_int <= 23
    
#     if bom_dia:
#         print('Bom dia')
    
#     if boa_tarde:
#         print('Boa tarde')
    
#     if boa_noite:
#         print('Boa noite')
# except:
#     print('Horario informado nao e numero inteiro')

#? Terceiro exercicio

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome e muito grande')
else:
    print('Digite mais de uma letra')