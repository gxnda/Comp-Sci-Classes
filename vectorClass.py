from math import atan, sqrt

class Vector(object):
    
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def get_x(self) -> float:
        return self.__x

    def set_x(self, x: float) -> None:
        self.__x = x

    def get_y(self) -> float:
        return self.__y

    def set_y(self, y: float) -> None:
        self.__y = y

    def scalar_multiply(self, scalar) -> None:
        self.__x *= scalar
        self.__y *= scalar

    def add(self, otherVector):
        """Adds together the current vector and another vector."""
        newX = self.__x + otherVector.__x
        newY = self.__y + otherVector.__y
        return Vector(newX, newY)

    def dot_product(self, otherVector):
        return Vector(self.__x * otherVector.get_x(), self.__y * otherVector.get_y())

    def get_angle_radians(self) -> float:
        #tan(angle) = opp/adj so angle = arctan(opp/adj)
        return atan(self.__y/self.__x)

    def get_angle_degrees(self) -> float:
        return self.get_angle_radians() * (180/3.14159)
    
    def get_magnitude(self):
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def convex_combination(v1, v2, alpha):
        if alpha < 0 or alpha > 1:
            raise ValueError("Convex Combination must have scalar (alpha) between 0 and 1")
        x = alpha*v1.get_x() + (1-alpha)*v2.get_x()
        y = alpha*v1.get_y() + (1-alpha)*v2.get_y()
        return Vector(x, y)

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"
