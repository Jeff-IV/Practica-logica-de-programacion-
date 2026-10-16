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
    """ Anade un contacto a la Agenda """
    agenda.append((name, number))
    print("contacto agregado.")
    
    
def busqueda(name: str) -> int | bool:
    """ Busca un contacto en la agenda por su nombre 
    (si hay dos contactos con el mismo nombre retorna el primer contacto en la agenda)"""
    for element in agenda:
        if element[0] == name:
            return element[1]
        
    return False


def actualizacion(old_name: str, new_name: str, new_number: int) -> bool:
    """ Actualiza un contacto de la agenda
    PARAMS: 
    old_name = Nombre del contacto a actualizar
    new_name = Nombre actualizado
    new_number = telefono actualizado
    
    RETURNS:
    True si se pudo actualizar
    False si no se pudo actualizar
    """
    for element in agenda:
        if element[0] == old_name:
            element = (new_name, new_number)
            return True
    
    return False


# Aqui va el de ordenamiento
def ordeamiento() -> None:
    """ Ordena la agenda segun numeros telefonicos """
    agenda.sort(key=lambda x: x[1])

    
# Aqui va el de borrado
def borrado(tel: int) -> bool:
    """ Elimina un contacto de la agenda segun el numero de telefono """
    for index, element in enumerate(agenda):
        if element[1] == tel:
            agenda.pop(index)
            return True
        
    return False


def verificar_numero(number: int) -> bool:
    """ 
    Verifica que un numero de telefono cumpla con los requisitos.
    
    Params:
    number = Numero de telefono
    
    Returns:
    True en caso que cumpla
    False e.o.c
    """
    if len(str(number)) != 10:
        print("Numero no valido.")
        return False
    
    return True


def mostrar_contactos() -> None:
    """ Muestra en consola el nombre y numero de todos los contactos en la Agenda """
    for contacto in agenda:
        print(f"Nombre: {contacto[0]} numero: {contacto[1]}")
        
        



while True:
    print("################### AGENDA ####################")
    print("""   Digite una opcion:
          1. Add new contact
          2. Update contact
          3. Delete contact
          4. Search contact
          5. Sort contacts
          6. Show contacts
          7. Salir
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
            tel = int(input("numero del contacto a eliminar: "))
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
            ordeamiento()
            print("La lista fue ordena con exito.")
            
        
        case 6:
            mostrar_contactos()
            
        case 7:
            print("Gracias por usar la agenda Jefito, cerrando...")
            break
        