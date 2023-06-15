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
        self.add_car_frame = tk.Frame(self)
        self.add_car_frame.pack(pady=10)

        brand_label = tk.Label(self.add_car_frame, text="Brand:")
        brand_label.grid(row=0, column=0, padx=5, pady=5)
        self.brand_entry = tk.Entry(self.add_car_frame)
        self.brand_entry.grid(row=0, column=1, padx=5, pady=5)

        model_label = tk.Label(self.add_car_frame, text="Model:")
        model_label.grid(row=1, column=0, padx=5, pady=5)
        self.model_entry = tk.Entry(self.add_car_frame)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)

        year_label = tk.Label(self.add_car_frame, text="Year:")
        year_label.grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self.add_car_frame)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        price_label = tk.Label(self.add_car_frame, text="Price:")
        price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self.add_car_frame)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        status_label = tk.Label(self.add_car_frame, text="Status:")
        status_label.grid(row=4, column=0, padx=5, pady=5)
        self.status_combobox = ttk.Combobox(self.add_car_frame, values=[
                                            status.value for status in CarStatus])
        self.status_combobox.grid(row=4, column=1, padx=5, pady=5)
        self.status_combobox.current(0)

        add_button = tk.Button(
            self.add_car_frame, text="Add Car", command=self.add_car)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.car_listbox = tk.Listbox(self)
        self.car_listbox.pack(padx=10, pady=10)

        get_cars_button = tk.Button(
            self, text="Get All Cars", command=self.get_all_cars)
        get_cars_button.pack(pady=5)

    def add_car(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        price = float(self.price_entry.get())
        status = self.status_combobox.get()

        self.controller.add_car(brand, model, year, price, status)

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
            self.car_listbox.insert(tk.END, car)
