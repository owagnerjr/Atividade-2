# -*-coding:latin1-*-
a = float(input('Digite o Primeiro lado: '))
b = float(input('Digite o Segundo  lado: '))
c = float(input('Digite o Terceiro lado: '))

# Testando para verificar se é um triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Os 3 lados informados nao formam um triangulo')
    print(a,b,c)
elif (a == b) and (a == c):
    base = float(input('Entre com o valor da b: '))
    altura = float(input('Entre com o valor de h '))
    Area_do_Triangulo = (base * altura) * (0.5)
    print("O valor da area do Triangulo e " + "", Area_do_Triangulo)

elif (a == b) or (a == c) or (b == c):
    base = float(input('Entre com o valor da b: '))
    altura = float(input('Entre com o valor de h '))
    Area_do_Triangulo = (base * altura) * (0.5)
    print("O valor da area do Triangulo e " + "", Area_do_Triangulo)

else:
    base = float(input('Entre com o valor da b: '))
    altura = float(input('Entre com o valor de h '))
    Area_do_Triangulo = (base * altura) * (0.5)
    print("O valor da area do Triangulo e " + "", Area_do_Triangulo)


