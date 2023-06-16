
from model.enums.car_status import CarStatus


class Car:
    """
    A classe `Car` representa um carro com várias propriedades, como marca, modelo, ano, preço e status.
    Essa classe possui getters e setters para todas as propriedades, garantindo encapsulamento e controle
    sobre o acesso aos atributos privados.
    """

    def __init__(self, brand: str, model: str, year: int, price: float, status: CarStatus):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__status: CarStatus = status

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} {self.price} {self.status.name}"

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: CarStatus):
        self.__status = status.value
