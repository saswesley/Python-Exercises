
lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Não tem erro')
finally:
    print('executa de qualquer jeito')