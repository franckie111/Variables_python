def multiplicar_tres_numeros():
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        n3 = float(input("Ingrese el tercer número: "))

        resultado = n1 * n2 * n3

        print(f"El resultado de la multiplicación es: {resultado:.2f}")
    except ValueError:
        print("Ingrese números válidos.")

# Llama a la función para ejecutar el programa
multiplicar_tres_numeros()
