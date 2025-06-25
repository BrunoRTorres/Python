from time import sleep

def contador(a, b, c):
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += c
        print()
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont -= c
        print()

contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
avanco = int(input('Pulando quantas casas: '))

contador(inicio, fim, avanco)