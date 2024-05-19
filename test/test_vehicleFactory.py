
import pytest
from vehicleFactory.car import Car
from vehicleFactory.motorcycle import Motorcycle
from vehicleFactory.factory import Factory


@pytest.fixture
def car_instance():
    return Car("Toyota", "petrol", "red")

@pytest.fixture
def car_instance_with_four_doors():
    return Car("Honda", "electric", "blue", 4)

@pytest.fixture
def motorcycle_instance():
    return Motorcycle("Harley Davidson", "petrol")  



def test_car_creation(car_instance):
    assert car_instance._model_name == "Toyota"
    assert car_instance._fuel_type == "petrol"
    assert car_instance._color == "red"

def test_car_creation_with_four_doors(car_instance_with_four_doors):
    assert car_instance_with_four_doors._model_name == "Honda"
    assert car_instance_with_four_doors._fuel_type == "electric"
    assert car_instance_with_four_doors._color == "blue"
    assert car_instance_with_four_doors._number_of_doors == 4

def test_motorcycle_creation(motorcycle_instance):
    assert motorcycle_instance._model_name == "Harley Davidson"
    assert motorcycle_instance._fuel_type == "petrol" 
    
def test_car_fuel_type_change(car_instance):
    car_instance.change_fuel_type("diesel")
    assert car_instance._fuel_type == "diesel"


def test_invalid_fuel_type():
    with pytest.raises(ValueError):
        car_instance = Car("Toyota", "banzen", "red")

def test_invalid_number_of_doors():
    with pytest.raises(ValueError):
        car_instance = Car("Honda", "electric", "blue", 3)
        

def test_motorcycle_fuel_type_change():
    motorcycle_instance = Motorcycle("BMW", "electric")
    motorcycle_instance.change_fuel_type("diesel")
    assert motorcycle_instance._fuel_type == "diesel"
