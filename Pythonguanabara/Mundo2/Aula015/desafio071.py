saque = cedula50 = cedula20 = cedula10 = cedula1 = 0

while saque == 0:

    print('=-' * 10 + '=')

    saque = (int(input('Quanto voce quer sacar? R$')))

    print('=-' * 10 + '=')

    resto = saque

    if saque // 50 != 0:

        cedula50 = saque // 50

        resto = saque % 50

        print(f'Voce sacou \033[35m{cedula50}\033[m de \033[032mR$50\033[m.')

    if resto // 20 != 0:

        cedula20 = resto // 20

        resto = resto % 20

        print(f'Voce sacou \033[35m{cedula20}\033[m notas de \033[32mR$20\033[m.')

    if resto // 10 != 0:

        cedula10 = resto // 10

        resto = resto % 10

        print(f'Voce sacou \033[35m{cedula10}\033[m notas de \033[32mR$10\033[m.')

    if resto // 1 != 0:

        cedula1 = resto // 1

        print(f'Voce sacou \033[35m{cedula1}\033[m notas de \033[32mR$1\033[m.')

print('=-' * 10 + '=')

print('\033[32mSaque realizado!\033[m')

print('=-' * 10 + '=')
