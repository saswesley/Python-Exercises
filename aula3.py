a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('vc digitou errado. primeiro bimestre: '))

b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('vc digitou errado. segundo bimestre: '))

c = int(input('terceiro bimestre: '))
while c > 10:
    c = int(input('vc digitou errado. terceiro bimestre: '))

d = int(input('Quarto bimestre: '))
while d > 10:
    int(input('vc digitou errado. Quarto bimestre: '))

media = (a + b + c + d ) / 4
print('Sua média ''e {}' .format(media))



# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print ( 'media {}'.format(media))
# else:
#     print("Foi informado alguma nota errada")


# a = int(input("Entre com o primeiro valor: "))
# b = int(input("Entre com o segundo valor: "))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a  == 0 or not resto_b > 0:
#     print('foi digitado um numero par')
# else:
#     print('nenhum numero par foi digitado')


# a = input ('Primeiro valor')
# b = input ('Segundo valor')
# c = input('Terceiro valor')
#
# if a > b and a > c:
#     print('O maior número é {}' .format(a))
# elif b > a and b > c:
#     print('o maior numero é {}' .format(b))
# else:
#     print ('O maior numero é {}' .format(c))
#
# print ('final do programa')

