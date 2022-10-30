# -*-coding:latin1-*-
# -*-coding:latin1-*-
a = float(input('Digite o Primeiro Numero: '))
b = float(input('Digite o Segundo  Numero: '))
c = float(input('Digite o Terceiro Numero: '))

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor numero digitado foi {menor}")