def imprimir_cuenta_regresiva(valor: int) -> None:
    """Imprime una cuenta regresiva desde `valor` hasta 0 usando recursión."""
    # 1. Caso base
    if valor < 0:
        return
    
    # 2. Trabajo actual + Caso recursivo
    print(valor)
    imprimir_cuenta_regresiva(valor - 1)


imprimir_cuenta_regresiva(10)

# Ejercicio extra
def factorial(fact: int) -> int:
    # caso base
    if fact == 0:
        return 1
    
    
    
    return fact * factorial(fact-1)

print(factorial(5))


def fibonacci(number_fib : int) -> int: # esto es o(2**n) mucho mas recomendado de manera iterativa
    
    # caso base
    if number_fib <= 0:
        return 0
    
    if number_fib == 1:
        return 1
    
    return fibonacci(number_fib - 1) + fibonacci(number_fib - 2)


print(fibonacci(40))

def fibonacci_iterativo(number_fib: int) -> int: # O(n) algoritmo y O(1) en memoria
    
    if number_fib <= 0:
        return 0

    a, b = 0, 1
    
    for _ in range(number_fib-1):
        a, b = b, a + b
        
    return b

print(fibonacci_iterativo(40))