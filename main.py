from class_Vehicle import Car

def main() -> None:
    my_car = Car(brand = "Toyota", model = "Camry", year = 2023,
        fuel_type = "Бензин", max_speed = 220.0, engine_capacity = 2.5,
        rotation_speed = 6000.0, pe = 0.9)
    my_car.info()

if __name__ == "__main__":
    main()