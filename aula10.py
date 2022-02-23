from datetime import datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H: %M: %S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    data_criada = datetime(2071, 7, 5, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

if __name__ == '__main__':
    trabalhando_com_datetime()