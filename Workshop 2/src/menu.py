from engines import Engine
from vehicles import Car, Truck, Yacht, Motorcicle

class Main_menu: 
    """This class is a entry for menu"""
    def __init__(self):
        self.enginees = {}
        self.vehicles = []
        self.message_manager = """
        Please, choose an option:
        1. Create an engine
        2. Create a car
        3. Create a truck
        4. Create a yatch
        5. Create a motorcycle
        6. Show all engines
        7. Show all vehicles
        8. Exit
        """
        self.message_user = """
        Please, choose an option:
        1. Show all vehicles
        2. Exit
        """

    def create_engine(self):
        """This function allows the user to enter the details of an Engine and uses them to create an Engine instance. """
        name = input("Please, write a name to identify the engine:")
        type_motor = input("Please, write the type of engine:")
        potency = int(input("Please, write the potency in a integer value for the engine:"))
        weight = float(input("Please, write the weight in a decimal value for the engine:"))
        new_engine = Engine(name, type_motor, potency, weight)
        self.enginees[name] = new_engine

    def create_vehicle(self, vehicle_type: str):
        """This function handles user input to create instances of different vehicle types, depending on the type specified."""
        engine = input(f"Please, write the name of the engine for the {vehicle_type}:")
        model = input(f"Please, write the model for the {vehicle_type}:")
        year = int(input(f"Please, write the year for the {vehicle_type}:"))
        chassis = input(f"Please, write the chassis (A or B) for the {vehicle_type}:")
        if vehicle_type == "car":
            color = input(f"Please, write the color of the {vehicle_type}:")
            positions = input(f"Please write the number of seats in an integer value for the {vehicle_type}:")
            self.vehicles.append( Car(chassis, model, year, engine, positions, color) )

        elif vehicle_type == "truck":
            wheels = input(f"Please write the number of wheel in an integer value for the {vehicle_type}:")
            fuel_type = input(f"Please write the type of fuel the {vehicle_type} uses:")
            truck_weight = input(f"Please write the {vehicle_type} weight in a decimal value:")
            self.vehicles.append(Truck(chassis, model, year, engine, wheels, fuel_type, truck_weight))
        elif vehicle_type == "yacht":
            yacht_weight = input(f"Please write the {vehicle_type} weight in a decimal value:")
            top_speed = input(f"Please write the {vehicle_type} top speed in a integer value:")
            range_ = input(f"Please write the travel range of the {vehicle_type}")
            self.vehicles.append(Yacht(chassis, model, year, engine, yacht_weight, top_speed, range_))
        elif vehicle_type == "motorcycle":
            cylinder_capacity = input(f"Please write the {vehicle_type} cylinder capacity in a decimal value:")
            type_brakes = input(f"Please write the {vehicle_type} type brakes have: ")
            torque = input(f"Please write the {vehicle_type} torque have in a decimal value: ")
            self.vehicles.append(Motorcicle(chassis, model, year, engine, cylinder_capacity, type_brakes, torque))

    def show_engines(self):
        """This method show all available engines"""
        for engine_name, engine in self.enginees.items():
            print(f"Name: {engine_name}, Type: {engine.type_}, Potency: {engine.potency}, Weight: {engine.weight}")
            break