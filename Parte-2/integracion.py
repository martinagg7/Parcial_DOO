
""""
Definimos una interfaz común (Integral):
   - Todos los métodos de integración (Trapecio y Simpson) deben seguir esta interfaz y proporcionar su propia implementación del método calcular.

2. Creamos clases para cada método de integración:
   - MetodoTrapecio: Implementa la regla del Trapecio para integrar una función.
   - MetodoSimpson: Implementa la regla de Simpson para integrar una función.

3. Creamos una clase CalculadoraIntegracion:
   - Esta clase recibe una estrategia de integración (ya sea Trapecio o Simpson) y permite calcular la integral utilizando la estrategia elegida.
   - También permite cambiar el método de integración en tiempo de ejecución con cambiar_metodo.
"""


# Interfaz común para los métodos de integración
class Integral:
    def calcular(self, f, *args): #ponemos args porque los argumentos que le vamos a pasar cambian en función del método
        pass

class MetodoTrapecio(Integral):
    def calcular(self, f, x0, x1):
        h = x1 - x0
        return h / 2 * (f(x0) + f(x1))    

class MetodoSimpson(Integral):
    def calcular(self, f, x0, x1, x2):
        h = (x2 - x0) / 2
        return h / 3 * (f(x0) + 4 * f(x1) + f(x2))
    

#Calculador de integrales
class Calculadora_Integrales:
    def __init__(self, metodo):
        self.metodo = metodo

    def cambiar_metodo(self, metodo):
        self.metodo = metodo

    def calcular_integral(self, f, *args):
        return self.metodo.calcular(f, *args)

if __name__ == "__main__":
 
    def f(x):
        return x**2+5  


    calculadora = Calculadora_Integrales(MetodoTrapecio())
    integral_trapecio = calculadora.calcular_integral(f, 0, 1)  
    print(f" La integral con método del Trapecio: {integral_trapecio}")
    calculadora.cambiar_metodo(MetodoSimpson())
    integral_simpson = calculadora.calcular_integral(f, 0, 0.5, 1)  # Integrar usando 3 puntos (0, 0.5, 1)
    print(f"La integral con método de Simpson: {integral_simpson}")    