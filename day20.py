from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        if self.radius < 0:
            raise ValueError("Radius cannot be nagative")
        return 3.14 * self.radius ** 2
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    circle = Circle(radius)
    circle_area = circle.area()
    print(f"The area of the circle with radius {radius} is {circle_area:.2f}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
