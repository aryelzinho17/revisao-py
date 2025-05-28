#gerar nemros impares de acordo com o numerodigitado pelo usuario
x = 1
contador = 0
quantidade_impares = int(input('digite a quantidade de numeros impares que deseja gerar: '))
while contador < quantidade_impares:
    print(x)
    x += 2
    contador += 1