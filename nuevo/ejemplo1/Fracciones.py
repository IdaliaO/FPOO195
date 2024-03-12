from math import gcd

class Fracciones:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self._numerador = numerador
        self._denominador = denominador
        self.reducir()

    def reducir(self):
        divisor = gcd(self._numerador, self._denominador)
        self._numerador //= divisor
        self._denominador //= divisor

    def __str__(self):
        return f"{self._numerador}/{self._denominador}"

    def __add__(self, other):
        nuevo_numerador = self._numerador * other._denominador + self._denominador * other._numerador
        nuevo_denominador = self._denominador * other._denominador
        return Fracciones(nuevo_numerador, nuevo_denominador)

    def __sub__(self, other):
        nuevo_numerador = self._numerador * other._denominador - self._denominador * other._numerador
        nuevo_denominador = self._denominador * other._denominador
        return Fracciones(nuevo_numerador, nuevo_denominador)

    def __mul__(self, other):
        nuevo_numerador = self._numerador * other._numerador
        nuevo_denominador = self._denominador * other._denominador
        return Fracciones(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, other):
        nuevo_numerador = self._numerador * other._denominador
        nuevo_denominador = self._denominador * other._numerador
        return Fracciones(nuevo_numerador, nuevo_denominador)
