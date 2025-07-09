def leiaInt(msg):
        while True:
                try:
                    valor = int(input(msg))
                except (ValueError, TypeError):
                    print('ERRO: por favor, digite um numero inteiro valido.')
                    continue
                except (KeyboardInterrupt):
                      print('Usuario preferiu nao digitar esse numero')
                      return 0
                else:
                      return valor


def leiaFloat(msg):
      while True:
            try:
                valor = float(input(msg))
            except (ValueError, TypeError):
                print('ERRO: por favor, digite um numero real.')
                continue
            except (KeyboardInterrupt):
                  print('Usuario preferiu nao digitar esse numero')
                  return 0
            else:
                  return valor


numInt = leiaInt('Digite um valor inteiro: ')
numReal = leiaFloat('Digite um numero real: ')
print(f'O numero inteiro foi {numInt}, e o numero real foi {numReal}')
