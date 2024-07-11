def calcular_raiz_cuadrada(numero):

    raiz = numero

    precision = 1e-10 

    while abs(raiz * raiz - numero) > precision:

        raiz = (raiz + numero / raiz) / 2

    return raiz


numero = float(input("Por favor, introduce un número para calcular su raíz cuadrada: "))


raiz_cuadrada = calcular_raiz_cuadrada(numero)


print(f"La raíz cuadrada de {numero} es aproximadamente {raiz_cuadrada}")
