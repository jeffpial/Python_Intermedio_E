# Hoja de tarbajo 1

# Problema 1
# color frutas

def colores(intento = 1):
    cadena = input("Ingrese el color de la fruta: ")

    if cadena != "naranja":
        if intento <3 :
            print("no es el color, intentalo de nuevo")
            intento += 1
            colores(intento)
        else:
            print("Perdiste todos tus intentos")
    else:
        print("Ganaste")
colores()



# Problema 2
# Fibonacci
print("")
print("Fibonacci")
numerofinal = int(input("Ingrese el valor final de fibonacci: "))


def fibonacci(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)

print("la serie fibonacci es: ")
print(fibonacci(numerofinal))


# Problema 3
# factorial

print("")

print("factorial")
numerofac = int(input("Ingrese el numero para tomar su factorial: "))
def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)

print("el factorial de ", numerofac, "! es: ")
print(factorial(numerofac))

