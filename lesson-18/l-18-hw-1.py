class Rectangle:
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return self.side_a * 2 + self.side_b * 2

    def get_area(self):
        return self.side_a * self.side_b

    def rectangle_description(self):
        perimeter = self.get_perimeter()
        area = self.get_area()
        print('Сторона а равна %s' % self.side_a)
        print('Сторона б равна %s' % self.side_b)
        print('Периметр прямоугольника равен %s' % perimeter)
        print('Площадь прямоугольника равна %s' % area)


rectangle = Rectangle(4, 5)
rectangle2 = Rectangle(2, 55)

rectangle.rectangle_description()
rectangle2.rectangle_description()
