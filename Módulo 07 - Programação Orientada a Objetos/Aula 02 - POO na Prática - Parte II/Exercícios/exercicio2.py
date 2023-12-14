import math

class FormaGeometrica:
    def __init__(self):
        pass

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

circulo = Circulo(raio=5)
retangulo = Retangulo(comprimento=4, largura=6)
triangulo = Triangulo(lado1=3, lado2=4, lado3=5)

print("Círculo:")
print(f"Área: {circulo.calcular_area()}")
print(f"Perímetro: {circulo.calcular_perimetro()}")

print("\nRetângulo:")
print(f"Área: {retangulo.calcular_area()}")
print(f"Perímetro: {retangulo.calcular_perimetro()}")

print("\nTriângulo:")
print(f"Área: {triangulo.calcular_area()}")
print(f"Perímetro: {triangulo.calcular_perimetro()}")