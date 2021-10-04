import math


class Fraction:
    def __init__(self, numerator, denominator) -> None:
        self._validate_input_data(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator
        self._normalize()

    @staticmethod
    def _validate_input_data(numerator, denominator):
        if denominator == 0:
            raise TypeError('Знаменатель не может равняться нулю!')
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError(
                'Числитель и/или знаменатель не может быть не целым числом!')

    def _normalize(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.denominator = self.denominator / gcd
        self.numerator = self.numerator / gcd
        if self.denominator < 0:
            self.denominator = abs(self.denominator)
            if self.numerator < 0:
                self.numerator = abs(self.numerator)
            else:
                self.numerator *= -1

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: 'Fraction') -> 'Fraction':
        pass


f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
