import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from controller.car_controlller import CarController
from model.enums.car_status import CarStatus


class AddCarWindow(tk.Toplevel):
    """
    A classe `AddCarWindow` é uma janela de diálogo utilizada para adicionar um novo carro.
    Ela herda da classe `tk.Toplevel` do Tkinter, que fornece uma janela separada do aplicativo principal.
    """

    def __init__(self, parent, add_callback):
        super().__init__(parent)
        self.title("Add Car")
        self.add_callback = add_callback
        self.create_widgets()

    def create_widgets(self):
        brand_label = tk.Label(self, text="Brand:")
        brand_label.grid(row=0, column=0, padx=5, pady=5)
        self.brand_entry = tk.Entry(self)
        self.brand_entry.grid(row=0, column=1, padx=5, pady=5)

        model_label = tk.Label(self, text="Model:")
        model_label.grid(row=1, column=0, padx=5, pady=5)
        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)

        year_label = tk.Label(self, text="Year:")
        year_label.grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        price_label = tk.Label(self, text="Price:")
        price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        status_label = tk.Label(self, text="Status:")
        status_label.grid(row=4, column=0, padx=5, pady=5)
        self.status_combobox = ttk.Combobox(self, values=[
            status.value for status in CarStatus])
        self.status_combobox.grid(row=4, column=1, padx=5, pady=5)
        self.status_combobox.current(0)

        add_button = tk.Button(self, text="Add Car", command=self.add_car)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def add_car(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        price = float(self.price_entry.get())
        status = self.status_combobox.get()

        if brand and model and year and price:
            self.add_callback(brand, model, year, price, status)
            self.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
