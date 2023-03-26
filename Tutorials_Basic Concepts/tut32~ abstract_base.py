'''
Abstract base class is class which can impose some rules on the classes which are inherited from an abstract
class. For example, we can construct a abstract base class and inherit class Rectangle and Square from it. This
abstract class will ensure that there is always an area_print function in the inherited classes, if not then we will
receive an error.

'''

# class Rectangle:
#     def __init__(self):
#         self.length = 4
#         self.breadth = 5
#
#     def area_print(self):4
#         return self.length*self.breadth
#
# class Square:
#     def __init__(self):
#         self.length = 4
#     def area_print(self):
#         return self.length*self.length


# use of abstract base class
from abc import ABC,abstractmethod
#abstractmethod mentioned above is a decorator

class Area(ABC):
    @abstractmethod
    def area_print(self):
        return 0

class Rectangle(Area):
    def __init__(self):
        self.length = 4
        self.breadth = 5

    # def area_print(self):
    #     return self.length * self.breadth


class Square(Area):
    def __init__(self):
        self.length = 4

    def area_print(self):
        return self.length * self.length

obj1 = Rectangle()
# print(obj1.area_print())

'''use of an abstract class will ensure that area_print function is available in on the derived classes. In case it 
is missing in a derived class, it will throw an error while creating its instance. We cannot create an object of 
the abstract class'''