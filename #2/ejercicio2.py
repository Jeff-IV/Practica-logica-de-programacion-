
# Funcion sin parametros ni retorno
def function_without_return() -> None:
    """ imprime un texto corto """
    print("Hola entraste a la funcion sin retorno!")
    
    
# Funcion con dos parametros y retorno    
def sum(a: int, b: int) -> int:
    """ Recibe dos enteros y retorna su suma"""
    return a + b


# Funcion can varios parametros
def bisection(f: function, a: int, b: int, tol: float = 1e-10, maxiter: int = 200) -> float:
    """ 
    Calcula la raiz aproximada de una funcion en un intervalo
    
    params: 
    f = funcion en python con f(x)
    a = limite inferior
    b = limite superior

    opcionales:
    tol = tolerancia establecida, por defecto 1e-10
    maxiter = numero maximo de iteraciones para encontrar la aproximacion de la raiz
    """
    def tvi(c: float, d: float) -> bool:
        f_c = f(c)
        f_d = f(d)
        f_c_d = f_c * f_d
        if f_c_d > 0:
            return False
        else:
            return True
        
    
    if tvi(a, b) == False:
        raise Exception("El intervalo no es valido")
        
    for _ in range(maxiter):
        pn = (a + b)/2
        
        if f(pn) > tol:
            return pn
        
        if tvi(a, pn):
            
            b = pn
        else:
            a = pn      
        
        
    raise Exception(f" No convergio en {maxiter} iteraciones. valor: {pn}")
    
    
f = lambda x: x**2 + x - 5
a = 1
b = 2

function_without_return()
print("La suma de a y b es: " + str(sum(a, b)))
print(f"la raiz aproximada de f es: {bisection(f=f, a=a, b=b)}")
        
        
# Funciones ya creadas en el leguanje
length = len(range(1,10)) # Funcion que retorna la longitud de un iterable/contenedor
print("La longitud del iterable es: " + str(length))


# Diferencias entre variable local y global
global_var = "soy global, me tienes disponible en todo el script"

def use_local_var() -> None:
    """ Imprime una variable global y otra local"""
    local_var = "Soy local, solo me tienes disponibke aqui"
    print(local_var)
    print(global_var)

try:
    use_local_var()
    print(local_var)
    
except:
    print("exacto. No puedes imprimirla por fuera")


# Ejercicio extra
def extra(str1: str, str2: str) -> int:
    res = 0
    
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print(str1 + str2)
            continue
            
        else:
            if i % 3 == 0:
                print(str1)
                continue
            
            if i % 5 == 0:
                print(str2)
                continue
        
        res += 1
        print(i)

    return res
            
print(f"el numero se ha impreso: {extra("goku", "naruto")} veces")