class PERSON:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def showInfo(self):
        print(f"Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))

person = PERSON(first_name, last_name, age)
person.showInfo()



#------------------------ TASK 2 ------------------------#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        perim = self.width + self.height
        return perim * 2
    
    def showInfo(self):
        print(f"Width: {self.width}, Height: {self.height}")

width = float(input("Enter width: "))
height = float(input("Enter height: "))

rectangle = Rectangle(width, height)

rectangle.showInfo()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
