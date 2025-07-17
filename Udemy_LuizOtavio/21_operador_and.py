# Operadores logicos
# and (e) or (ou) not (nao)
# and - todas as concicoes precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor 
# Sao considerados falsy 
# 0 0.0 '' False
# Tambem existe o tipo None que e 
# usado para representar um nao valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

# if True:
#   ...
senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')