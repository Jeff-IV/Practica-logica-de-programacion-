# Estructuras de datos 

list_ = [1,2,3,4] 
dict_ = {"key": "value", "key2": "value2"} # no permite claves duplicadas
tuple_ = (1, 2) # no es mutable
set_ = {1,2,3,4} # no permite duplicados y no tiene orden

# Insercion
list_.append(4) # al final
dict_["key3"] = "value3"
new_tuple = tuple_ + (3,) # truco para "insertar" en una tupla
set_.add(5) # al final


# Borrado
list_.pop(-1) # elimina el ultimo elemento
dict_.pop("key3") # elimina una tupla clave valor segun la clave
list_temp = list(new_tuple) # convertimos a lista y eliminamos su ultimo elemento
list_temp.pop(-1) #eliminamos su ultimo elemento
new_tuple = tuple(list_temp) # volvemos a convertirla en tupla
set_.pop() # al no tener orden elimina un elemento al azar


# Actualizacion
cambio = (1, 5)
cambio_dict = ("key1", "value11")

# Este caso se puede usar como base para las demas estructuras...
for element in list_:
    if element == cambio[0]:
        list_.remove(element)
        list_.append(cambio[1])
        break

# Cambiando el valor a una clave especifica
dict_[cambio_dict[0]] = cambio_dict[1]


# Ordenacion
list_.sort()
sorted(list_)
sorted(new_tuple)
# El diccionario y el set no se pueden ordenar


# Ejercicio extra
agenda = []

def insercion(name: str, number: int) -> None:
    agenda.append((name, number))
    print("contacto agregado.")
    
    
def busqueda(name: str) -> int | bool:
    for element in agenda:
        if element[0] == name:
            return element[1]
        
    return False


def actualizacion(old_name: str, new_name: str, new_number: int) -> bool:
    for element in agenda:
        if element[0] == old_name:
            element = (new_name, new_number)
            return True
    
    return False


# Aqui va el de ordenamiento


    
# Aqui va el de borrado
def borrado(name: str) -> bool:
    for index, element in enumerate(agenda):
        if element[0] == name:
            agenda.pop(index)
            return True
        
    return False


def verificar_numero(number: int) -> bool:
    if len(str(number)) != 10:
        print("Numero no valido.")
        return False
    
    return True

while True:
    print("################### AGENDA ####################")
    print("""   Digite una opcion:
          1. Add new contact
          2. Update contact
          3. Delete contact
          4. Search contact
          5. Salir
          """)
    user_option = int(input())
    

    
    match user_option:
        case 1:
            name = input("Nombre: ")
            number = int(input("Numero: "))
            if verificar_numero(number):
                insercion(name, number)
            else:
                break
            
        case 2:
            old_name = input("Nombre antiguo: ")
            name = input("Nuevo nombre: ")
            number = int(input("nuevo numero: "))
            if verificar_numero(number):
                if actualizacion(old_name, name, number):
                    print("Contacto actualizado")
            else:
                break
            
        case 3:
            name = input("nombre contacto a eliminar: ")
            if borrado(name):
                print("Contacto borrado de manera exitosa")
            else:
                print("no se pudo borrar el contacto porque no existe")
        
        case 4:
            name = input("Nombre contacto a buscar: ")
            number = busqueda(name)
            if number is False:
                print(f"El contacto {name} no existe")
            else:
                print(f"Su numero es {number}")
            
        case 5:
            print("Gracias por usar la agenda Jefito, cerrando...")
            break
        