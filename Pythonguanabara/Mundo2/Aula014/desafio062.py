primeiro = int(input('Primeiro termo: '))

razao =  int(input('Razao: '))

termo = primeiro

cont = 1

total = 0

maistermo = 10
 
while maistermo != 0:

    total = total + maistermo

    while cont <= total:

        print(termo, end=' ')

        termo += razao

        cont += 1
        
    print('')
        
    maistermo = int(input('Quantos termos a mais gostaria de ver? '))
  
