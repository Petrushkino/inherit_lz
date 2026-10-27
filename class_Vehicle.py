class Vehicle:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        
    def info(self) -> None:
        print(f"Транспортное средство: {self.brand} {self.model}, Год выпуска: {self.year}")
        
class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, max_speed: float, 
                 engine_capacity: float, rotation_speed: float, pe: float) -> None:
        super().__init__(brand, model, year)
        
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed
        self.pe = pe
        
    def engine_power_calc(self) -> float:
        # P = (V * n * pe) / 120
        power = (self.engine_capacity * self.rotation_speed * self.pe) / 120
        return power
        
    def info(self) -> None:
        super().info()
        print(f"Тип топлива: {self.fuel_type}")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Объем двигателя: {self.engine_capacity} л")
        print(f"Скорость вращения: {self.rotation_speed} об/мин")
        print(f"Эффективное давление (pe): {self.pe} МПа")
        print(f"Расчетная мощность двигателя: {self.engine_power_calc()} кВт")