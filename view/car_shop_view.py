import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controller.car_shop_controlller import CarController
from model.enums.status import CarStatus
from view.add_car_window import AddCarWindow


class CarView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Car Inventory")
        self.controller = CarController(self)
        self.create_widgets()

    def create_widgets(self):
        self.principal_view = tk.Frame(self)
        self.principal_view.pack(pady=10)

        add_button = tk.Button(
            self.principal_view, text="Add Car", command=self.open_add_car_window)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.car_treeview = ttk.Treeview(self, columns=(
            "brand", "model", "year", "price", "status"))
        self.car_treeview.pack(padx=10, pady=10)

        self.car_treeview.heading("brand", text="Brand")
        self.car_treeview.heading("model", text="Model")
        self.car_treeview.heading("year", text="Year")
        self.car_treeview.heading("price", text="Price")
        self.car_treeview.heading("status", text="Status")

        self.car_treeview.column("brand", width=100)
        self.car_treeview.column("model", width=100)
        self.car_treeview.column("year", width=50)
        self.car_treeview.column("price", width=80)
        self.car_treeview.column("status", width=80)

        filter_label = tk.Label(self, text="Filter by brand:")
        filter_label.pack(padx=10, pady=10)
        self.filter_entry = tk.Entry(self)
        self.filter_entry.pack(padx=10, pady=10)
        filter_button = tk.Button(
            self, text="Filter", command=self.filter_by_brand)
        filter_button.pack(padx=10, pady=10)

        if self.controller.get_all_cars():
            self.get_all_cars()

    def open_add_car_window(self):
        add_car_window = AddCarWindow(self, self.add_car)
        add_car_window.grab_set()

    def add_car(self, brand, model, year, price, status):
        self.controller.add_car(brand, model, year, price, status)
        self.get_all_cars()

    def filter_by_brand(self):
        self.car_treeview.delete(*self.car_treeview.get_children())
        brand = self.filter_entry.get()
        if brand == "":
            return self.get_all_cars()

        cars = self.controller.filter_by_brand(brand)
        self.show_cars(cars)

    def get_all_cars(self):
        self.car_treeview.delete(*self.car_treeview.get_children())
        cars = self.controller.get_all_cars()
        for car in cars:
            self.car_treeview.insert("", tk.END, values=car)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def show_cars(self, cars):
        self.car_treeview.delete(*self.car_treeview.get_children())
        for car in cars:
            self.car_treeview.insert("", tk.END, values=car)
