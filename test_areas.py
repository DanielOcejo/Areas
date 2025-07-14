from main import calcular_area_cuadrado, calcular_area_circulo, calcular_area_triangulo
import math

# Pruebas cuadrado
assert calcular_area_cuadrado(4) == 16
assert calcular_area_cuadrado(-2) is None

# Pruebas círculo
assert round(calcular_area_circulo(3), 2) == round(math.pi * 9, 2)
assert calcular_area_circulo(0) is None

# Pruebas triángulo
assert calcular_area_triangulo(6, 4) == 12.0
assert calcular_area_triangulo(-3, 5) is None

print("Todas las pruebas pasaron correctamente.")
