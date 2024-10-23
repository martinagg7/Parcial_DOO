""""
Antipatrón "God Object"
-----------------------
Un "God Object" es una clase que tiene demasiadas responsabilidades. 
Esto es problemático porque hace que la clase sea difícil de mantener, probar y modificar, 

Problemas que causa:
- Dificultad para mantener y extender el código.
- Pruebas unitarias complejas.

"""
#Ejemplo de una clase Calculadora que hace demasiadas funciones
class Calculadora:
    def area_circulo(self, radio):
        return 3.14 * radio**2

    def area_rectangulo(self, largo, ancho):
        return largo * ancho

    def perimetro_circulo(self, radio):
        return 2 * 3.14 * radio

    def perimetro_rectangulo(self, largo, ancho):
        return 2 * (largo + ancho)

#Tras aplicar este principio y dividir la clase  
#AREAS 
class CalculadoraArea:
    def area_circulo(self, radio):
        return 3.14 * radio**2

    def area_rectangulo(self, largo, ancho):
        return largo * ancho
#PERIMETRO
class CalculadoraPerimetro:
    def perimetro_circulo(self, radio):
        return 2 * 3.14 * radio

    def perimetro_rectangulo(self, largo, ancho):
        return 2 * (largo + ancho)
