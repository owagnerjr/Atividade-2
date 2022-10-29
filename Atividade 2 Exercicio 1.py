# -*-coding:latin1-*-
from datetime import date
current_date = date.today()
data_nascimento= int(input("Seu ano de nascimento: "))
data_actual = current_date.year
idade =data_actual-data_nascimento
mes = idade * 12
dias = idade * 365

print(idade,"ano(s)")
print(mes,"Meses" )
print (dias,"Dias")
