
from model.car import Car


class Shop():

    def __init__(self, stock):
        self.__stock: list(Car) = stock

    def __str__(self):
        return f"{self.stock}"

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock
