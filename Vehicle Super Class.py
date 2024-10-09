class Vehicle:
    def __init__(self, type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle
        
class Auto_Mobile(Vehicle):
    def __init__(self, type_of_vehicle):
        super().__init__(type_of_vehicle)
        self.make = ""
        self.model = ""
        self.year = ""
        self.doors = ""
        self.roof = ""
        
    def showdata(self):
        print("Type: ", self.type_of_vehicle)
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("How Many Doors?: ", self.doors)
        print("Roof Type: ", self.roof)
        
cars = Auto_Mobile("cars")

print("______________________________")
cars.make = input("What is the Make?")
cars.model = input("What is the Model?")
cars.year = input("What is the Year?")
cars.doors = input("How Many Doors? (2 or 4)")
cars.roof = input("What type of roof? (Solid or Sun Roof)")
print("______________________________")

print("______________________________")
print("Vehichle Information")
cars.showdata()

print("______________________________")

        
        