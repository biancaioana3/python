class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        return 0.02 * self.balance


class CheckingAccount(Account):
    pass


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self):
        pass

    def calculate_towing_capacity(self):
        pass


class Car(Vehicle):
    def calculate_mileage(self):
        return "Mileage calculation for cars."


class Motorcycle(Vehicle):
    def calculate_mileage(self):
        return "Mileage calculation for motorcycles."


class Truck(Vehicle):
    def calculate_towing_capacity(self):
        return "Towing capacity calculation for trucks."


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def role_specific_method(self):
        pass


class Manager(Employee):
    def role_specific_method(self):
        return "Manager-specific method."


class Engineer(Employee):
    def role_specific_method(self):
        return "Engineer-specific method."


class Salesperson(Employee):
    def role_specific_method(self):
        return "Salesperson-specific method."


class Animal:
    def __init__(self, species):
        self.species = species

    def unique_method(self):
        pass


class Mammal(Animal):
    def unique_method(self):
        return "Mammal-specific method."


class Bird(Animal):
    def unique_method(self):
        return "Bird-specific method."


class Fish(Animal):
    def unique_method(self):
        return "Fish-specific method."


class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} returned successfully.")
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre


class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration


class Magazine(LibraryItem):
    def __init__(self, title, publisher, year):
        super().__init__(title, publisher, year)


circle = Circle(radius=5)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")

rectangle = Rectangle(length=4, width=6)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

triangle = Triangle(side1=3, side2=4, side3=5)
print(f"Triangle Area: {triangle.area()}")
print(f"Triangle Perimeter: {triangle.perimeter()}")

savings_account = SavingsAccount(balance=1000)
savings_account.deposit(500)
print(f"Savings Account Balance: {savings_account.balance}")
savings_account.withdraw(200)
print(f"Savings Account Balance: {savings_account.balance}")
print(f"Savings Account Interest: {savings_account.calculate_interest()}")

car = Car(make="Toyota", model="Camry", year=2020)
print(f"Car Mileage: {car.calculate_mileage()}")

motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2021)
print(f"Motorcycle Mileage: {motorcycle.calculate_mileage()}")

truck = Truck(make="Ford", model="F-150", year=2019)
print(f"Truck Towing Capacity: {truck.calculate_towing_capacity()}")

manager = Manager(salary=80000)
print(f"Manager Salary: {manager.salary}")
print(manager.role_specific_method())

engineer = Engineer(salary=70000)
print(f"Engineer Salary: {engineer.salary}")
print(engineer.role_specific_method())

salesperson = Salesperson(salary=60000)
print(f"Salesperson Salary: {salesperson.salary}")
print(salesperson.role_specific_method())

mammal = Mammal(species="Dog")
print(f"Mammal Species: {mammal.species}")
print(mammal.unique_method())

bird = Bird(species="Parrot")
print(f"Bird Species: {bird.species}")
print(bird.unique_method())

fish = Fish(species="Salmon")
print(f"Fish Species: {fish.species}")
print(fish.unique_method())

book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925, genre="Fiction")
book.check_out()
book.return_item()

dvd = DVD(title="Inception", director="Christopher Nolan", year=2010, duration="2h 28m")
dvd.check_out()

magazine = Magazine(title="National Geographic", publisher="National Geographic Society", year=2023)
magazine.check_out()
magazine.return_item()
