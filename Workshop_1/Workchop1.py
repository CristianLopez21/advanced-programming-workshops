"""
This file contains the prototype of the new internal platform to define a vehicle catalog, 
based on the requirements given in the first workshop.

Author: Cristian S. Lopez Cadena - Marzo/13/2024
"""

# -------------------------------- Class Engine --------------------------------
class Engine:
    """ This class represents a behavior of a vehicle engine. """

    def __init__(self, name: str, type_: str, potency: int, weight: float ):
        self.name = name
        self.type_ = type_
        self.potency = potency
        self.weight = weight
# -------------------------------- Class Vehicle --------------------------------       
class Vehicle:
    """ This class represents the behavior of an abstract class to define vehicles. """
    def __init__(self, chassis: str, model: str, year: int, engine: Engine):
        if not chassis in ["A","B"]:
            raise ValueError("This chassis in not valid. ")
        self.chassis = chassis
        self.model = model
        self.year = year
        self.engine = engine 
        self.gas_consumption = None

        def calculate_consumption(self):
            """This method is used to calculate the gas comsumption. """
            consumption = ((1.1*self.potency) + (0.2*self.weight) - (0.3 if self.chassis == "A" else 0.5))    
            self.gas_consumption = consumption      

# -------------------------------- Classes of Vehicles --------------------------------    
class Car(Vehicle):
    """This class is a concrete definition for a car. """
    def __init__(self, chassis: str, model: str, year: int, engine: Engine, positions:int, color: str):
        super().__init__(chassis, model, year, engine)
        self.positions = positions
        self.color = color 

class Truck(Vehicle):
    """This class is a concrete definition for a truck. """
    def __init__(self, chassis: str, model: str, year: int, engine: Engine, wheels: str, fuel_type: str, truck_weight: float):
        super().__init__(chassis, model, year, engine)
        self.Numbers_of_wheels = wheels
        self.fuel_type = fuel_type   
        self.truck_weight = truck_weight

class Yacht(Vehicle):
    """This class is a concrete definition for a yacht. """
    def __init__(self, chassis: str, model: str, year: int, engine: Engine, yacht_weight: float, top_speed: float, range_: float):
        super().__init__(chassis, model, year, engine)
        self.yacht_weight = yacht_weight
        self.top_speed = top_speed
        self.range_ = range_
class Motorcicle(Vehicle):
    """This class is a concrete definition for a motorcicle. """
    def __init__(self, chassis: str, model: str, year: int, engine: Engine, Cylinder_capacity:int, type_brakes: str, torque:float):
        super().__init__(chassis, model, year, engine)
        self.Cylinder_capacity = Cylinder_capacity
        self.type_brakes = type_brakes
        self.torque = torque

# -------------------------------- save the objects --------------------------------
enginees = {}
vehicles = []

# -------------------------------- Menu -------------------------------- 
global message 
message ="""
    please choose an option:
    1. Create an engine
    2. Create a Car
    3. Create a Truck
    4. Create a Yacht
    5. Create a Motorcicle
    6. Show all engines 
    7. Show all Vehicles
    8. Exit
""" 
def option_1():
    """This function allows the user to enter the details of an Engine and uses them to create an Engine instance. """
    name = input("Please, write a name to identify the engine:")
    type_motor = input("Please, write the type of engine:")
    potency = int(input("Please, write the potency in a integer value for the engine:"))
    weight = float(input("Please, write the weight in a decimal value for the engine:"))
    new_engine = Engine(name, type_motor, potency, weight)
    enginees[name] = new_engine

def create_vehicle(vehicle_type: str):
    """This function handles user input to create instances of different vehicle types, depending on the type specified."""
    engine = input(f"Please, write the name of the engine for the {vehicle_type}:")
    model = input(f"Please, write the model for the {vehicle_type}:")
    year = int(input(f"Please, write the year for the {vehicle_type}:"))
    chassis = input(f"Please, write the chassis (A or B) for the {vehicle_type}:")
    if vehicle_type == "car":
        color = input(f"Please, write the color of the {vehicle_type}:")
        positions = input(f"Please write the number of seats in an integer value for the {vehicle_type}:")
        vehicles.append( Car(chassis, model, year, engine, positions, color) )

    elif vehicle_type == "truck":
        wheels = input(f"Please write the number of wheel in an integer value for the {vehicle_type}:")
        fuel_type = input(f"Please write the type of fuel the {vehicle_type} uses:")
        truck_weight = input(f"Please write the {vehicle_type} weight in a decimal value:")
        vehicles.append(Truck(chassis, model, year, engine, wheels, fuel_type, truck_weight))
    elif vehicle_type == "yacht":
        yacht_weight = input(f"Please write the {vehicle_type} weight in a decimal value:")
        top_speed = input(f"Please write the {vehicle_type} top speed in a integer value:")
        range_ = input(f"Please write the travel range of the {vehicle_type}")
        vehicles.append(Yacht(chassis, model, year, engine, yacht_weight, top_speed, range_))
    elif vehicle_type == "motorcycle":
        cylinder_capacity = input(f"Please write the {vehicle_type} cylinder capacity in a decimal value:")
        type_brakes = input(f"Please write the {vehicle_type} type brakes have: ")
        torque = input(f"Please write the {vehicle_type} torque have in a decimal value: ")
        vehicles.append(Motorcicle(chassis, model, year, engine, cylinder_capacity, type_brakes, torque))


def menu():
    """This function represents the menu of the application."""
    while True:
        print(message)
        option = int(input("enter an option: "))
        while option != 8:
            if option == 1:
                option_1()
                break
            elif option == 2:
                create_vehicle("car")
                break
            elif option == 3:
                create_vehicle("truck")
                break
            elif option == 4:
                create_vehicle("yatch")
                break
            elif option == 5:
                create_vehicle("motorcycle")
                break
            elif option == 6:
                for engine_name, engine in enginees.items():
                    print(f"Name: {engine_name}, Type: {engine.type_}, Potency: {engine.potency}, Weight: {engine.weight}")
                break
            elif option == 7:
                for vehicle in vehicles:
                    if isinstance(vehicle, Car):
                        print(f"Type: Car, Model: {vehicle.model}, Year: {vehicle.year}, Engine: {vehicle.engine}, Color: {vehicle.color}, Positions: {vehicle.positions}")
                    elif isinstance(vehicle, Truck):
                        print(f"Type: Truck, Model: {vehicle.model}, Year: {vehicle.year}, Engine: {vehicle.engine}, Wheels: {vehicle.Numbers_of_wheels}, Fuel Type: {vehicle.fuel_type}, Truck Weight: {vehicle.truck_weight}")
                    elif isinstance(vehicle, Yacht):
                        print(f"Type: Yacht, Model: {vehicle.model}, Year: {vehicle.year}, Engine: {vehicle.engine}, Yacht Weight: {vehicle.yacht_weight}, Top Speed: {vehicle.top_speed}, Range: {vehicle.range_}")
                    elif isinstance(vehicle, Motorcicle):
                        print(f"Type: Motorcicle, Model: {vehicle.model}, Year: {vehicle.year}, Engine: {vehicle.engine}, Cylinder Capacity: {vehicle.Cylinder_capacity}, Type Brakes: {vehicle.type_brakes}, Torque: {vehicle.torque}")
                break
        if option == 8:
            break
        
if __name__ == "__main__":
    menu()