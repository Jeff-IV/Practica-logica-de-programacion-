# To do strings

string = "CANINO"

# recorrer una cadena
for char in string:
    print(char)
    
# pasar a mayusculas y minusculas
string_upper = string.upper()
string_lower = string.lower()
string_capitalized = string.capitalize() #primera mayuscula luego minuscula
ExampeOfThis = string.title()


# Accediendo por indice
string[4]

# Concatenacion
string2 = "FELINO"
concat = string + string2

# subcadena usando slicing
new_string = string[:2]

# Longitud de una cadena
length = len(string)

# remplazo
new_string = string.replace("CAN", "DOG")

# repeticion 
repetido = "ja" * 5

# verificacion
esta = "FEL" in string2

# conteo de apariciones
conteo = string.count("CAN")

# verificacion inicio y fin
start_with = string.startswith("CAN")
end_with = string.endswith("NO")

# Division
lista_substrings = string.split("N") # separa en substring cada que encuentra un N

# Union
listaa = ["hola", "jose", "manuel"]
new_str = " ".join(listaa) # agrupa la lista en un string con el separador que le entrguemos

# Particion
correo = "josejuan@dominio.com"
particion = correo.partition("@") # retorna ("josejuan", "@", "dominio.com")


# Ejercicio extra
# Palindromo
palabra = "sometemos"
def palindromo(word: str) -> bool: # O(n) para el slicing
    """
    Verifica si un string es palindromo
    
    Params:
    word = palabra a verificar
    Return:
    True si es palindromo
    False si no es palindromo
    """
    word = word.lower()
    word_back = word[-1::-1]
    if word == word_back:
        return True
    else:
        return False
    
if palindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")



# Anagrama    
def anagrama(word1: str, word2: str) -> bool: # O(n**2) mal algoritmo D: no es eficiente
    lista_binaria = [1] * len(word2)
    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return False    
    
    for i in range(len(word1)):
        for j in range(len(word1)): # word1 y word2 tienen la misma longitud
            # busca la letra en la otra palabra y que no haya sido "usada"
            if word1[i] == word2[j] and lista_binaria[j] == 1: 
                lista_binaria[j] = 0
                break
            
            # Si llega al final y la letra no coincide entonces no puede ser un anagrama
            if j == len(word2)-1:
                return False
        
    return True


palabra1 = "rammo"
palabra2 = "amor"

if anagrama(palabra1, palabra2):
    print(f"{palabra1} es un anagrama de {palabra2}")
else:
    print(f"{palabra1} NO es un anagrama de {palabra2}")




# Isograma
def isograma(word1: str) -> bool: #O(n)
    
    apariciones = {}
    
    # Armamos el diccionario y las apariciones de cada letra
    for i in word1:
        if i not in apariciones.keys():
            apariciones[i] = 1
            base = apariciones[i]

        else:
            apariciones[i] += 1
            base = apariciones[i]
            
    # Revisamos que cada llave tenga el mismo valor
    for i in apariciones.keys():
        print(i)
        if base != apariciones[i]:
            return False
        
    return True
    
    
palabra_isograma = "localoca"

if isograma(palabra_isograma):
    print(f"{palabra_isograma} es un isograma!")
else:
    print(f"{palabra_isograma} NO es un isograma")