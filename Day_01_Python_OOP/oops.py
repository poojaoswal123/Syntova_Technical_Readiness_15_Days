# 1. Class and Object

class MyClass:
    x = 5

p1 = MyClass()

print(p1.x)


# multiple objects

class MyClass:
    x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


# empty class using pass

class Person:
    pass

p1 = Person()


# 2. __init__() Constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Pooja", 22)

print(p1.name)
print(p1.age)


# default values in __init__()

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Pooja")
p2 = Person("Amit", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)


# multiple parameters

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Pooja", 22, "Kolhapur", "India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)


# 3. self

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Pooja", 22)
p1.greet()


# accessing properties using self

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.year, self.brand, self.model)

car1 = Car("Toyota", "Corolla", 2020)

car1.display_info()


# calling one method from another using self

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p1 = Person("Pooja")
p1.welcome()


# 4. Instance Properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Pooja", 22)

print(p1.name)
print(p1.age)


# modifying instance properties

p1.age = 23

print(p1.age)


# adding new properties to an object

p1.city = "Kolhapur"

print(p1.city)


# deleting an instance property

del p1.city

# print(p1.city)


# 5. Instance Methods

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

print(calc.add(5, 3))
print(calc.multiply(4, 7))


# method accessing and modifying properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

    def celebrate_birthday(self):
        self.age += 1
        print("Happy birthday! You are now", self.age)

p1 = Person("Pooja", 22)

print(p1.get_info())

p1.celebrate_birthday()
p1.celebrate_birthday()


# multiple methods

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def show_songs(self):
        print("Playlist:", self.name)

        for song in self.songs:
            print(song)

playlist = Playlist("Favorites")

playlist.add_song("Song 1")
playlist.add_song("Song 2")

playlist.show_songs()

playlist.remove_song("Song 1")

playlist.show_songs()


# 6. Class Variable vs Instance Variable

class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

p1 = Person("Pooja")
p2 = Person("Amit")

print(p1.name)
print(p2.name)

print(p1.species)
print(p2.species)


# modifying class variable

Person.species = "Human Being"

print(p1.species)
print(p2.species)


# 7. Class Methods

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

print(Student.school)

Student.change_school("XYZ School")

print(Student.school)


# 8. Static Methods

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(Calculator.add(5, 3))
print(Calculator.multiply(4, 5))


# 9. __str__() Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Pooja", 22)

print(p1)


# 10. Deleting Objects and Methods

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello")

p1 = Person("Pooja")

del p1

# print(p1)


# deleting a method from a class

class Person:
    def greet(self):
        print("Hello")

del Person.greet

# p1 = Person()
# p1.greet()


# 11. Encapsulation - Public Variable

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Pooja", 85)

s1.display()

print(s1.name)
print(s1.marks)


# 12. Protected Variable

class Employee:
    def __init__(self, salary):
        self._salary = salary

    def show_salary(self):
        print("Salary:", self._salary)

emp = Employee(50000)

emp.show_salary()

print(emp._salary)


# 13. Private Variable

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(10000)

account.show_balance()

# print(account.__balance)


# 14. Getter and Setter

class Person:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

p = Person(25)

print(p.get_age())

p.set_age(30)

print(p.get_age())


# 15. Encapsulation with Validation

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

s = Student("Pooja", 70)

print(s.get_marks())

s.set_marks(95)

print(s.get_marks())


# 16. Private Method

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        return isinstance(num, (int, float))

    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()

calc.add(10)
calc.add(5)

print(calc.result)

# calc.__validate(5)


# 17. Encapsulation - Bank Account

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount(5000)

acc.deposit(1000)
acc.withdraw(2000)

print(acc.get_balance())


# 18. Inheritance

# parent class

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


# child class

class Student(Person):
    def study(self):
        print(self.name, "is studying")

s = Student("Pooja")

s.greet()
s.study()


# 19. Inheritance with Constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Student(Person):
    pass

s = Student("Pooja", 22)

s.show_info()


# 20. Single Inheritance

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


c = Car()

c.start()
c.drive()


# 21. Multilevel Inheritance

class Grandparent:
    def show_grandparent(self):
        print("Grandparent")


class Parent(Grandparent):
    def show_parent(self):
        print("Parent")


class Child(Parent):
    def show_child(self):
        print("Child")


c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()


# 22. Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()


# 23. Multiple Inheritance

class Father:
    def father_skill(self):
        print("Gardening and Driving")


class Mother:
    def mother_skill(self):
        print("Cooking and Painting")


class Child(Father, Mother):
    pass


c = Child()

c.father_skill()
c.mother_skill()


# calling both parent methods explicitly

class Father:
    def skills(self):
        print("Gardening, Driving")


class Mother:
    def skills(self):
        print("Cooking, Painting")


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()

c.skills()


# 24. super()

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show(self):
        super().show()
        print("Course:", self.course)


s = Student("Pooja", "Data Science")

s.show()


# super() with parent method

class Person:
    def show(self):
        print("I am a person")


class Student(Person):
    def show(self):
        super().show()
        print("I am a student")


s = Student()

s.show()


# 25. Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 26. Polymorphism

class Car:
    def move(self):
        print("Drive!")


class Boat:
    def move(self):
        print("Sail!")


class Plane:
    def move(self):
        print("Fly!")


car = Car()
boat = Boat()
plane = Plane()

for vehicle in (car, boat, plane):
    vehicle.move()


# 27. Polymorphism with Inheritance

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Boat(Vehicle):
    def move(self):
        print("Boat is sailing")


class Plane(Vehicle):
    def move(self):
        print("Plane is flying")


vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()


# 28. Polymorphism with Different Objects

class India:
    def capital(self):
        print("New Delhi")


class USA:
    def capital(self):
        print("Washington D.C.")


countries = [India(), USA()]

for country in countries:
    country.capital()


# 29. Duck Typing

class Laptop:
    def code(self):
        print("Coding in Python")


class Mobile:
    def code(self):
        print("Coding in App")


def developer(device):
    device.code()


laptop = Laptop()
mobile = Mobile()

developer(laptop)
developer(mobile)


# 30. Polymorphism with Function

class Bird:
    def fly(self):
        print("Bird can fly")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


birds = [Sparrow(), Ostrich()]

for bird in birds:
    bird.fly()


# 31. Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        print("Area of Circle")


class Square(Shape):
    def area(self):
        print("Area of Square")


shapes = [Circle(), Square()]

for shape in shapes:
    shape.area()


# 32. Abstraction with Real Example

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTime(Employee):
    def calculate_salary(self):
        return 50000


class PartTime(Employee):
    def calculate_salary(self):
        return 20000


class Intern(Employee):
    def calculate_salary(self):
        return 10000


employees = [FullTime(), PartTime(), Intern()]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# 33. isinstance()

class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, object))


# 34. __str__() Special Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


p = Person("Pooja", 22)

print(p)


# 35. __len__() Special Method

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Pooja", "Amit", "Rahul"])

print(len(team))


# 36. __add__() Special Method

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


# 37. Property Decorator

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")


p = Person(22)

print(p.age)

p.age = 25

print(p.age)


# 38. Real-World OOP Example

class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.__balance}"


account = BankAccount("Pooja", 5000)

account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())
print(account)