"""
Patrón Observer en el método Newton-Raphson
-------------------------------------------
El patrón Observer puede ser útil en el método Newton Raphson porque es un algoritmo iterativo que mejora una solución paso a paso.
Cada vez que el algoritmo encuentra una mejor aproximación de la raíz de una función, puede notificar automáticamente a otros 
componentes del sistema (como un gráfico o un reporte de errores) para que se actualicen con la nueva solución.

Para el método de Newton Rapshom el observador, valor que se actualiza cada vez que el algoritmo de Newton-Raphson
encuentra una nueva solución.
"""

class NewtonRaphson:
    def __init__(self):
        self.observadores = []  

    
    def add_observador(self, observador):
        self.observadores.append(observador)

    # Cuando encontramos otra raiz
    def notificar_observadores(self, nueva_solucion):
        for observador in self.observadores:
            observador.actualizar(nueva_solucion)

    #Alg N-R
    def aplicar_metodo(self, f, df, x_inicial, iteraciones=5):
        x = x_inicial
        for _ in range(iteraciones):
            x = x - f(x) / df(x)  
            self.notificar_observadores(x)  #


class Raiz:
    def actualizar(self, nueva_solucion):
        print(f"Raiz actualizada con nueva solución: {nueva_solucion}")


if __name__ == "__main__":

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x


    newton = NewtonRaphson()

    # Crear el observador (Gráfico)
    raiz = Raiz()

    # Agregar el observador al algoritmo
    newton.agregar_observador(raiz)

    # Aplicar Newton-Raphson desde x_inicial = 1
    newton.aplicar_metodo(f, df, x_inicial=1)