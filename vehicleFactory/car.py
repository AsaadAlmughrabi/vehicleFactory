
from vehicleFactory.factory import Factory
# from ...vehicleFactory.vehicleFactory.factory import Factory


class Car(Factory):
    

    def __init__(self, model_name, fuel_type, color, number_of_doors=4):
        # super().__init__()
        self._model_name = model_name
        self._fuel_type = super().change_fuel_type(fuel_type)
        self._color = color
        self.change_number_of_doors(number_of_doors)
        Car._total_created += 1

    def change_model_name(self, new_model_name):
        """
        Changes the model name of the car.
        """
        self._model_name = new_model_name
        return new_model_name

    # def change_fuel_type(self, new_fuel_type):
    #     """
    #     Changes the fuel type of the car.
    #     """
    #     valid_fuel_types = ["electric", "petrol", "diesel"]
    #     if new_fuel_type.lower() not in valid_fuel_types:
    #         raise ValueError("Invalid fuel type. Must be electric, petrol, or diesel.")
    #     self._fuel_type = new_fuel_type.lower()
    #     return new_fuel_type

    def change_color(self, new_color):
        """
        Changes the color of the car.
        """
        self._color = new_color
        return new_color

    def change_number_of_doors(self, new_number_of_doors):
        """
        Changes the number of doors of the car.
        """
        if new_number_of_doors not in [2, 4]:
            raise ValueError("Invalid number of doors. Must be 2 or 4.")
        else:
            self._number_of_doors = new_number_of_doors
            return new_number_of_doors

    def __str__(self):
        """
        Returns a string representation of the car.
        """
        return f"Car - Model: {self._model_name}, Fuel Type: {self._fuel_type}, Color: {self._color}, Number of Doors: {self._number_of_doors}"
