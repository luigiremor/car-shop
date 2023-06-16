from db.car_database import CarDatabase
from model.car import Car
from model.enums.car_status import CarStatus


class CarController:
    """
    A classe `CarController` é responsável por intermediar a interação entre a interface gráfica e o banco de dados,
    gerenciando as operações relacionadas aos carros.
    """

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

    def update_car(self, car_id, brand, model, year, price, status):
        car = Car(brand, model, year, price, CarStatus(status))
        self.db.update_car(car_id, car)
        self.view.show_message("Car updated successfully.")

    def delete_car(self, car_id):
        self.db.delete_car(car_id)
        self.view.show_message("Car deleted successfully.")

    def get_mean_price(self):
        return self.db.get_mean_price()
