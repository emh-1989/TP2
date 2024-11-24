class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

# Prueba la clase
rectangulo1 = Rectangulo(4, 7)
print(f"El rectángulo tiene un alto de: {rectangulo1.alto} y un ancho de: {rectangulo1.ancho}")
print(f"El área del rectángulo es: {rectangulo1.area()}")      
print(f"El perímetro del rectángulo es: {rectangulo1.perimetro()}")  
