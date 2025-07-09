# Aula sobre tratamentos de erros

#! Fundamentos

# try: #? Comando para tentar um codigo

# except: #? Comando para quando ocorre um erro

# else: #? Comando para quando o codigo funciona (Opcional)

# finally: #? funcao que ira acontecer independente do resultado (opcional)


#@ Pratica

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou!')

except ZeroDivisionError:
    print('Nao e possivel dividir por zero!')

except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados!')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')

else:
    print(f'O resultado e {r:.1f}')

finally:
    print('Volte sempre! Muito obrigado!')