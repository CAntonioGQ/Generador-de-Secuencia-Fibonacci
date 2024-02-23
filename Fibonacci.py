#Gastelum Quevedo Cruz Antonio 21041442
#Examen Fibonacci
#La documentación se encuentra en el otro archivo
#Github: https://github.com/CAntonioGQ
def generar_fibonacci(n, primer_elemento):
    fibonacci_list = []
    a, b = 0, 1

    while len(fibonacci_list) < n:
        if a >= primer_elemento:
            fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

def main():
    try:
        cantidad_numeros = int(input("Cuantos numeros de Fibonacci desea? : "))
        primer_elemento = int(input("Cual es el primer numero inicial de la serie que desea? : "))

        fibonacci_list = generar_fibonacci(cantidad_numeros, primer_elemento)

        print("\nImprimir en pantalla:")
        print(fibonacci_list)

    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

if __name__ == "__main__":
    main()
