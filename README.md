# Enunciado Parcial POO

## Parte 1

### Pregunta 1 (1 Punto):

Explique en detalle el principio SOLID "Open/Closed" y proporcione un ejemplo de código en Python donde este principio se ha violado y cómo puede corregirlo.

### Pregunta 2 (1 Punto):

Describa el patrón de diseño "Factory". ¿En qué situaciones sería útil este patrón? Proporcione un ejemplo de cómo implementaría este patrón en Python para un problema relacionado con la ingeniería matemática, como la creación de diferentes tipos de funciones matemáticas.

### Pregunta 3 (1 Punto):

Explique el antipatrón "God Object". ¿Por qué es perjudicial este antipatrón y qué problemas puede causar en el desarrollo de software? Proporcione un ejemplo de un "God Object" en un contexto de ingeniería matemática y explique cómo podría refactorizarlo para evitar este antipatrón.

### Pregunta 4 (1 Punto):

Los principios DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid) son fundamentales para escribir código de alta calidad. Proporcione un ejemplo de un fragmento de código Python que viole estos principios. Describa cómo lo refactorizaría para adherirse a los principios DRY y KISS.

### Pregunta 5 (1 Punto):

El patrón de diseño "Observer" permite que un objeto notifique a otros objetos sobre los cambios en su estado. Describa una situación en el contexto de la ingeniería matemática donde este patrón sería útil. Implemente un ejemplo simple de este patrón en Python para ilustrar su respuesta.



### Pregunta Práctica 1: Refactorización de código con Principios SOLID (2,5 Puntos)

Se le proporciona un fragmento de código Python que maneja diferentes tipos de formas geométricas. Actualmente, el código viola el Principio de Responsabilidad Única (SRP) y el Principio Abierto/Cerrado (OCP) de SOLID. Su tarea es refactorizar este código para que se adhiera a estos principios.

```python
class Shape:
    def __init__(self, type):
        self.type = type

class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            if shape.type == "circle":
                radius = 1.0  # Supongamos que el radio es siempre 1 para este ejemplo
                total += 3.14159 * radius * radius
            elif shape.type == "square":
                side = 1.0  # Supongamos que el lado es siempre 1 para este ejemplo
                total += side * side
        return total

shapes = [Shape("circle"), Shape("square")]
calculator = AreaCalculator(shapes)
print(calculator.total_area())
```


## Parte 2

### Pregunta Práctica 2:  Implementación de Patrón de Diseño Estrategia (2,5 Puntos)


Se le pide que implemente este escenario utilizando el patrón de diseño estrategia. Debe proporcionar una estructura que permita cambiar fácilmente el método de integración. Incluya al menos dos métodos específicos (por ejemplo, Trapecio y Simpson) y demuestre cómo se podrían cambiar estos métodos en tiempo de ejecución.






