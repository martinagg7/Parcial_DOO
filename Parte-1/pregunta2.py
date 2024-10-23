""""
Patrón Factory
--------------
El patrón Factory es una forma de organizar tu código para que, cuando necesites crear algo, no tengas que preocuparte por cómo se crea.
En lugar de que el código directamente cree un objeto de una clase específica, se usa una "fábrica" que se encarga de decidir qué crear

-Casos de uso:
1. Cuando el código cliente no debe conocer los detalles específicos de la creación de objetos.
2. Cuando necesitas flexibilidad para crear diferentes tipos de objetos dependiendo de la situación.

-Ejemplo:
Patrón Factory para derivadas 
Este ejemplo muestra cómo usar el patrón Factory para crear derivadas de diferentes tipos de funciones.
"""

class Derivada:#para x^3
    def calcular(self, x):
        pass

class DerivadaPrimera(Derivada): 
    def calcular(self, x):
        return 3*x**2 
    
class DerivadaSegunda(Derivada):
    def calcular(self, x):
        return 6*x    
    
class DerivadaTercera(Derivada):
    def calcular(self, x):
        return 6    
    
#Factory  derivadas
class DerivadaFactory:
    def crear_derivada(self, tipo_derivada):
        if tipo_derivada == "primera":
            return DerivadaPrimera()
        elif tipo_derivada == "segunda":
            return DerivadaSegunda()
        elif tipo_derivada == "tercera":
            return DerivadaTercera()
        else:
            raise ValueError(f"Tipo de derivada no valido")

if __name__ == "__main__":
    factory = DerivadaFactory()
    derivada_1 = factory.crear_derivada("primera")
    print(f"Primera derivada en x=2: {derivada_1.calcular(2)}")

    derivada_2 = factory.crear_derivada("segunda")
    print(f"Segunda derivada en x=2: {derivada_2.calcular(2)}")