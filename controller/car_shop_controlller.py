

import json
from model.car import Car

from model.shop import Shop


class CarShopController():

    def __init__(self, shop: Shop) -> None:
        self.__shop: Shop = shop
        self.load_data()

    @property
    def shop(self) -> Shop:
        return self.__shop

    @shop.setter
    def shop(self, shop: Shop) -> None:
        self.__shop = shop

    def add_car(self, car: Car) -> None:
        self.__shop.stock.append(car)
        self.save_data()

    def remove_car(self, car: Car) -> None:
        self.__shop.stock.remove(car)
        self.save_data()

    def update_car(self, car: Car) -> None:
        self.__shop.stock.remove(car)
        self.__shop.stock.append(car)
        self.save_data()

    def search_all_cars_by_brand(self, brand: str) -> list:
        return [car for car in self.__shop.stock if car.brand == brand]

    def save_data(self):
        with open("data.json", 'w') as f:
            json.dump(self.__shop, f)

    def load_data(self):
        try:
            with open("db/data.json", 'r+') as f:
                data = json.load(f)

                self.__shop = data
                f.close()
        except FileNotFoundError:
            pass
