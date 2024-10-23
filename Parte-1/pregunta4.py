"""""
Principios DRY y KISS
---------------------
1. DRY : No repitas código innecesariamente. Si algo se repite, debes abstraerlo en una función o estructura reutilizable.
   
2.KISS (: Mantén el código simple y directo. No añadas complejidad innecesaria y soluciona los problemas de la manera más sencilla posible.
"""

# Ejemplo que NO CUMPLE DRY y KISS
def saludar_espanol(nombre):
    print(f"Hola {nombre}")

def saludar_ingles(nombre):
    print(f"Hello {nombre}")

def saludar_frances(nombre):
    print(f"Bonjour {nombre}")

#Aplicamos DRY and KISS    
def saludar(nombre, idioma):
    if idioma == "espanol":
            print(f"Hola {nombre}")
    elif idioma == "ingles":
            print(f"Hello {nombre}")
    elif idioma == "frances":
            print(f"Bonjour {nombre}")
    else:
        print("Idioma no soportado")

    print(saludos.get(idioma, "Idioma no soportado"))

saludar("Martina", "espanol")  # Hola Martina
saludar("JoE", "ingles")      # Hello John
