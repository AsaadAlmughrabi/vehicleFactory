def main():
#     from car import Car
#     from motorcycle import Motorcycle
    from vehicleFactory.car import Car
    from vehicleFactory.motorcycle import Motorcycle
   
    car1 = Car("Toyota", "petrol", "red")
    car2 = Car("Honda", "electric", "blue", 4)
    motorcycle1 = Motorcycle("Harley Davidson", "petrol")

    print(car1)
    print(car2)
    print(motorcycle1)

    Car.print_total_created()
    Motorcycle.print_total_created()


if __name__ == "__main__":
    main()