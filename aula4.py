a = int(input('Entre com um valor: '))

for num in range (a):
    div = 0
    for x in range(1, num+1):

        resto = num % x
        #print(x, resto)

        if resto == 0:
            div = div + 1
    if div == 2:
        print(num)





# a = int(input('Entre com o número: '))
# div = 0
# for x in range (1, a+1):
#
#     resto = a % x
#     print(x, resto)
#     print (resto)
#     if resto == 0:
#         div = div + 1
# if div == 2:
#     print ('numero {} é primo' .format (a))
# else:
#     print('numero {} não é primo' .format(a))