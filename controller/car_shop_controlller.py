from db.database import CarDatabase
from model.car import Car
from model.enums.status import CarStatus


class CarController:
    def __init__(self, view):
        self.view = view
        self.db = CarDatabase("car_inventory.db")
        self.db.create_table()

    def add_car(self, brand, model, year, price, status):
        car = Car(brand, model, year, price, CarStatus(status))
        self.db.insert_car(car)
        self.view.show_message("Car added successfully.")

    def get_all_cars(self):
        return self.db.get_all_cars()

    def filter_by_brand(self, brand):
        return self.db.filter_by_brand(brand)
