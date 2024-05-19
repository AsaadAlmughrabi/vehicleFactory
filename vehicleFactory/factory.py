from abc import ABC, abstractmethod


class Factory(ABC):
    """
    Abstract base class for creating vehicles.
    """

    _total_created = 0

    @abstractmethod
    def __init__(self):
        """
        Abstract initializer method for creating a new instance of a vehicle.
        """

        

    @classmethod
    def print_total_created(cls):
        """
        Prints the total number of vehicles created.
        """

        print(f"Total {cls.__name__}s created:", cls._total_created)

    @abstractmethod
    def __str__(self):
        """
        Abstract method to represent the vehicle as a string.
        """
        pass
    
    
    def change_fuel_type(self, new_fuel_type):
        """
        Changes the fuel type .
        """
        valid_fuel_types = ["electric", "petrol", "diesel"]
        if new_fuel_type.lower() not in valid_fuel_types:
            raise ValueError("Invalid fuel type. Must be electric, petrol, or diesel.")
        self._fuel_type = new_fuel_type.lower()
        return new_fuel_type



