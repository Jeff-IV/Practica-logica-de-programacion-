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


