# -*-coding:latin1-*-
# Testando números de 1 a 100 para retornar somente os números primos
start = 1
end = 100

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)






