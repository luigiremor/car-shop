import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controller.car_controlller import CarController

from model.enums.car_status import CarStatus
from view.add_car_window import AddCarWindow
from view.update_car_window import UpdateCarWindow


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

        update_button = tk.Button(
            self.principal_view, text="Update Car", command=self.open_update_car_window)
        update_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        delete_button = tk.Button(
            self.principal_view, text="Delete Car", command=self.delete_car)
        delete_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.car_treeview = ttk.Treeview(self, columns=(
            "id", "brand", "model", "year", "price", "status"))
        self.car_treeview['show'] = 'headings'
        self.car_treeview.pack()

        self.car_treeview.heading("id", text="ID")
        self.car_treeview.heading("brand", text="Brand")
        self.car_treeview.heading("model", text="Model")
        self.car_treeview.heading("year", text="Year")
        self.car_treeview.heading("price", text="Price")
        self.car_treeview.heading("status", text="Status")

        self.car_treeview.column("id")
        self.car_treeview.column("brand")
        self.car_treeview.column("model")
        self.car_treeview.column("year")
        self.car_treeview.column("price")
        self.car_treeview.column("status")

        self.value_mean = tk.StringVar()
        self.update_mean_price()
        mean_label = tk.Label(self, textvariable=self.value_mean)
        mean_label.pack(padx=10, pady=10)

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

    def open_update_car_window(self):
        selected_item = self.car_treeview.focus()
        if selected_item:
            car_data = self.car_treeview.item(selected_item)["values"]
            update_car_window = UpdateCarWindow(
                self, car_data, self.update_car)
            update_car_window.grab_set()
        else:
            messagebox.showerror("Error", "No car selected.")

    def add_car(self, brand, model, year, price, status):
        self.controller.add_car(brand, model, year, price, status)
        self.get_all_cars()
        self.update_mean_price()

    def update_car(self, car_id, brand, model, year, price, status):
        selected_item = self.car_treeview.focus()
        if selected_item:
            self.controller.update_car(
                car_id, brand, model, year, price, status)
            self.get_all_cars()
            self.update_mean_price()
        else:
            messagebox.showerror("Error", "No car selected.")

    def delete_car(self):
        selected_item = self.car_treeview.focus()
        if selected_item:
            car_id = self.car_treeview.item(selected_item)["values"][0]
            self.controller.delete_car(car_id)
            self.get_all_cars()
            self.update_mean_price()
        else:
            messagebox.showerror("Error", "No car selected.")

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

    def update_mean_price(self):
        mean_price = self.controller.get_mean_price()
        if mean_price is None:
            mean_price = 0
        self.value_mean.set(f"Mean price: {mean_price:.2f}")
