import engines as Engine
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
        self.calculate_consumption = calculate_consumption() 

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
