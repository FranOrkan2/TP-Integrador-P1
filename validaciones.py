
def pedir_texto(mensaje):
    while True:    
        try:
            nombre = input(mensaje).strip().title()
            if not nombre:
                raise ValueError("Campo vacio")
            
            if not all(palabra.isalpha() for palabra in nombre.split()): 
                raise ValueError("Caracter invalido en el nombre")
            
            return nombre
        except ValueError as e:
            print(f"Error: {e}")

def pedir_entero(mensaje):
    while True:
        try:
            valor= int(input(mensaje))
            if valor < 0: raise ValueError("El numero debe ser positivo")
            return valor
        except ValueError as e:
            print(f"Error: {e}")