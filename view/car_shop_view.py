import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controller.car_shop_controlller import CarController
from model.enums.status import CarStatus


class CarView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Car Inventory")
        self.controller = CarController(self)
        self.create_widgets()

    def create_widgets(self):
        self.principal_view = tk.Frame(self)
        self.principal_view.pack(pady=10)

        brand_label = tk.Label(self.principal_view, text="Brand:")
        brand_label.grid(row=0, column=0, padx=5, pady=5)
        self.brand_entry = tk.Entry(self.principal_view)
        self.brand_entry.grid(row=0, column=1, padx=5, pady=5)

        model_label = tk.Label(self.principal_view, text="Model:")
        model_label.grid(row=1, column=0, padx=5, pady=5)
        self.model_entry = tk.Entry(self.principal_view)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)

        year_label = tk.Label(self.principal_view, text="Year:")
        year_label.grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self.principal_view)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        price_label = tk.Label(self.principal_view, text="Price:")
        price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self.principal_view)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        status_label = tk.Label(self.principal_view, text="Status:")
        status_label.grid(row=4, column=0, padx=5, pady=5)
        self.status_combobox = ttk.Combobox(self.principal_view, values=[
                                            status.value for status in CarStatus])
        self.status_combobox.grid(row=4, column=1, padx=5, pady=5)
        self.status_combobox.current(0)

        add_button = tk.Button(
            self.principal_view, text="Add Car", command=self.add_car)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.car_listbox = tk.Listbox(self)
        self.car_listbox.pack(padx=10, pady=10)

        filter_label = tk.Label(self, text="Filter by brand:")
        filter_label.pack(padx=10, pady=10)
        self.filter_entry = tk.Entry(self)
        self.filter_entry.pack(padx=10, pady=10)
        filter_button = tk.Button(
            self, text="Filter", command=self.filter_by_brand)
        filter_button.pack(padx=10, pady=10)

        if self.controller.get_all_cars():
            self.get_all_cars()

    def add_car(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        price = float(self.price_entry.get())
        status = self.status_combobox.get()

        self.controller.add_car(brand, model, year, price, status)
        self.get_all_cars()

    def filter_by_brand(self):
        self.car_listbox.delete(0, tk.END)
        brand = self.filter_entry.get()
        print(brand, 'filter by brand')
        if brand == "":
            return self.get_all_cars()

        cars = self.controller.filter_by_brand(brand)
        self.show_cars(cars)

    def get_all_cars(self):
        self.car_listbox.delete(0, tk.END)
        cars = self.controller.get_all_cars()
        for car in cars:
            self.car_listbox.insert(tk.END, car)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def show_cars(self, cars):
        self.car_listbox.delete(0, tk.END)
        for car in cars:
            print(car, 'show cars')
            self.car_listbox.insert(tk.END, car)
