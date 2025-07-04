def maior(* num):
    pos = 0
    for n in num:
        if pos <= 0:
            maior = n
            pos += 1
        if n > maior:
            maior = n
    
    print('=-' * 20 + '=')
    for n in num:
        print(n, end=', ')
    print(f'Ao todo foi informado {len(num)} numeros e o maior e o {maior}.')


maior(1, 2, 3, 4, 5)
maior(4, 1, 6, 8, 9, 4, 3)
maior(4, 66, 31, 868, 12, 945, 101)