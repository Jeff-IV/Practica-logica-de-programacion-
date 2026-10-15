import math

# Ejemplos operadores
a : int = 15
b : int = 1

# Operadores aritmeticos
# Suma y resta
sum : int  = a + b
diff : int = a - b

# Multipicacion y division
mul : int = a * b # El tipo del retorno depende de los tipos que se operen
div : float = a / b # la division retorna un flotante siempre
int_div : int = a // b # la division entera usa la funcion piso para aproximar (elimina la parte decimal basicamente). Aunque cuando uno de los dos es float devuelve un float sin decimales (.0)
res = a % b

# Exponenciacion y logaritmo
exp : int = a ** b # El tipo del retorno depende de los tipos que se operen (aunque si el exponente es negativo siempre retorna un float)
log = math.log(a) 


# Operadores de comparacion
greater_than : bool = a > b
greather_equal_than : bool = a >= b
less_than: bool = a < b
less_equal_than : bool = a <= b


# Operadores logicos
and_ = a and b
or_ = a or b
not_ = not a


# Operadores de pertenencia 
c = [1, 3, 6]
d = [1, 3, 6, 8]
in_ = c in d # a pertenece o esta en b
not_in = c not in d # a no pertenece a b


# Operadores de identidad 
is_ = a is b  # True si refieren el mismo objeto
is_not = a is not b # True si se refieren a objetos distintos


# Operadores de bits 
and_bits = a & b
or_bit = a | b
xor = a ^ b
not_bit = ~a
des_izq = a << b # Desplaza bits a la izquierda
des_der = a >> b # Desplaza bits a la derecha

# Condicional
int_list : list[int] = [1, 2, 3, 4, 5]
if 7 > len(int_list):
    print("entramos al condicional")

    
# bucle for
for number in int_list:
    match number%2:
        case 0:
            print("eres par")
        case 1:
            print("sos impar")

# bucle while
index = 0
while True:
    if index == 3:
        break
    index += 1
    
# Excepciones 

try: 
    raise Exception("Forzando el error") # forzando una excepcion
    #print(funcion_inexistente_suma(a, b)) # forzando una excepcion
    
except:
    print("dio error crack")
    # raise Exception("Portate serio crack")

print("Final bro")

for i in range(10, 51, 2):
    if i % 3 == 0 or i == 16: 
        continue
    print(i)
    
    