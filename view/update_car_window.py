import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from model.enums.status import CarStatus


class UpdateCarWindow(tk.Toplevel):
    def __init__(self, parent, car_data, update_callback):
        super().__init__(parent)
        self.title("Update Car")
        self.car_data = car_data
        self.update_callback = update_callback
        self.create_widgets()

    def create_widgets(self):
        brand_label = tk.Label(self, text="Brand:")
        brand_label.grid(row=0, column=0, padx=5, pady=5)
        self.brand_entry = tk.Entry(self)
        self.brand_entry.grid(row=0, column=1, padx=5, pady=5)
        self.brand_entry.insert(tk.END, self.car_data[0])

        model_label = tk.Label(self, text="Model:")
        model_label.grid(row=1, column=0, padx=5, pady=5)
        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=1, column=1, padx=5, pady=5)
        self.model_entry.insert(tk.END, self.car_data[1])

        year_label = tk.Label(self, text="Year:")
        year_label.grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)
        self.year_entry.insert(tk.END, self.car_data[2])

        price_label = tk.Label(self, text="Price:")
        price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)
        self.price_entry.insert(tk.END, self.car_data[3])

        status_label = tk.Label(self, text="Status:")
        status_label.grid(row=4, column=0, padx=5, pady=5)
        self.status_combobox = ttk.Combobox(self, values=[
            status.value for status in CarStatus])
        self.status_combobox.grid(row=4, column=1, padx=5, pady=5)
        self.status_combobox.set(self.car_data[4])

        update_button = tk.Button(
            self, text="Update Car", command=self.update_car)
        update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def update_car(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        price = float(self.price_entry.get())
        status = self.status_combobox.get()

        if brand and model and year and price:
            self.update_callback(brand, model, year, price, status)
            self.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
