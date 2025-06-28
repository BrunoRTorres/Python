from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if 18 <= idade <= 70:
        return ('Obrigatório')
    elif 16 < idade < 18 or idade > 70:
        return ('Opcional')
    else:
        return ('Negado')

nascimento = int(input('Em que ano voce nasceu? '))
print(f'O seu voto foi: {voto(nascimento)}')
