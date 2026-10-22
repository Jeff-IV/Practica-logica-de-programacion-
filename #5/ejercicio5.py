
# Variables por valor
var = 1983

# Las variables por referencia no existen en python de manera nativa, aunque se pueden simular con una clase

# pasar  como valor
new_var = var # aqui se pasa por valor ya que int es un tipo no mutable, los no mutables se pasan por valor 

# pasar por referencia 
lista = [1,2,3,4,5]
new_list = lista # aqui se pasa por referencia ya que una lista es un objeto mutable en python con todo lo que ello conlleva

def func_for_value(no_mut : int) -> None:
    no_mut += 1
    print(f" dentro de la funcion es: {no_mut}")

func_for_value(var)
print(f" fuera de la funcion es {var}")

def func_for_ref(mutable : list) -> None:
    mutable.append(8)
    print(f" dentro de la funcion es {mutable} ")
    
func_for_ref(lista)
print(f" fuera de la funcion es: {lista}")


# Ejercicio extra
def function_exchange_value(var1: int, var2:int) -> tuple[int, int]:
    temp = var1
    var1 = var2
    var2 = temp
    return (var1, var2)

no_mut1 = 1
no_mut2 = 100

new_no_mut1, new_no_mut2 = function_exchange_value(no_mut1, no_mut2)
print(f" variable 1 original: {no_mut1} y la nueva: {new_no_mut1}")
print(f" variable 2 original: {no_mut2} y la nueva: {new_no_mut2}")

# En python no pasa nada ya que por dentro crea una variable var1 local y var2 local, por lo tanto no intercambia el valor de var1 y var2 original
def function_exchange_ref(var1: list, var2: list) -> tuple[list, list]:
    temp = var1
    var1 = var2
    var2 = temp
    
    return (var1, var2)

mut1 = [1,2,3]
mut2 = [11, 12, 13]
new_mut1, new_mut2 = function_exchange_ref(mut1, mut2)
print(f" variable 1 original: {mut1} y la nueva: {new_mut1}")
print(f" variable 2 original: {mut2} y la nueva: {new_mut2}")
