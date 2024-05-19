from  vehicleFactory.factory  import Factory



class Motorcycle(Factory):
    

    def __init__(self, model_name, fuel_type, number_of_wheels=2):
        # super().__init__()
        self._model_name = model_name
        self._fuel_type = super().change_fuel_type(fuel_type)
        self._number_of_wheels = number_of_wheels
        Motorcycle._total_created += 1

    def change_model_name(self, new_model_name):
        """
        Changes the model name of the motorcycle.
        """
        self._model_name = new_model_name

    # def change_fuel_type(self, new_fuel_type):
    #     """
    #     Changes the fuel type .
    #     """
    #     valid_fuel_types = ["electric", "petrol", "diesel"]
    #     if new_fuel_type.lower() not in valid_fuel_types:
    #         raise ValueError("Invalid fuel type. Must be electric, petrol, or diesel.")
    #     self._fuel_type = new_fuel_type.lower()
    #     return new_fuel_type

    def __str__(self):
        """
        Returns a string representation of the motorCycle.
        """
        return f"Motorcycle - Model: {self._model_name}, Fuel Type: {self._fuel_type}, Number of Wheels: {self._number_of_wheels}"
