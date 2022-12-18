from dataclasses import dataclass


@dataclass()
class Person:
    name: str
    surname: str
    patronymic: str
    age: int

    def __str__(self) -> str:
        return f' name: {self.name} \n surname: {self.surname} \n patronymic: {self.patronymic} \n age: {self.age}'


@dataclass
class Driver(Person):
    experience: int

    def __str__(self) -> str:
        return super().__str__() + f'experience: {self.experience}'


@dataclass()
class Engine:
    power: int
    company: str

    def __str__(self) -> str:
        return f' power: {self.power} \n company: {self.company}'


@dataclass()
class Car:
    car_class: str
    engine: Engine
    driver: Driver
    mark: str
    weight: float

    def start(self) -> None:
        print("Поехали")

    def stop(self) -> None:
        print("Останавливаемся")

    def turn_right(self) -> None:
        print("Поворот направо")

    def turn_left(self) -> None:
        print("Поворот налево")

    def __str__(self) -> str:
        return f' class: {self.car_class} \n engine: {self.engine} \n driver: {self.driver}' \
               f' \n mark: {self.mark} \n weight: {self.weight}'


@dataclass()
class Lorry(Car):
    carrying: int

    def __str__(self) -> str:
        return super().__str__() + f'\n carrying: {self.carrying}'


@dataclass()
class SportCar(Car):
    max_speed: float

    def __str__(self) -> str:
        return super().__str__() + f'\n max_speed: {self.max_speed}'


driver = Driver(name="Marat", surname="Bek", patronymic="asdf", age=22, experience=10)
engine = Engine(power=202, company="Tesla")
car = Car(car_class="Lux", engine=engine, driver=driver, mark="2C", weight=500)
print(driver)
print()
print(engine)
print()
print(car)
car.start()
car.stop()
car.turn_left()
car.turn_right()

lorry = Lorry(car_class="3c", engine=engine, driver=driver, mark="2sdkf", weight=400, carrying=330)
lorry.turn_left()
print(lorry)
sport_car = SportCar(car_class="Lux", engine=engine, driver=driver, mark="2C", weight=500, max_speed=233)
print()
print(sport_car)
sport_car.stop()
