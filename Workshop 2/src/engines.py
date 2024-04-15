# -------------------------------- Class Engine --------------------------------
class Engine:
    """ This class represents a behavior of a vehicle engine. 
    Constructctor class: 

    parameters:
    -name(str) : descriptcion
    """

    def __init__(self, name: str, type_: str, potency: int, weight: float ):
        self.name = name
        self.type_ = type_
        self.potency = potency
        self.weight = weight