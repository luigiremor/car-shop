import sqlite3


class CarDatabase:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                brand TEXT,
                model TEXT,
                year INTEGER,
                price REAL,
                status TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_car(self, car):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cars VALUES (?, ?, ?, ?, ?)
        """, (car.brand, car.model, car.year, car.price, car.status.value))
        conn.commit()
        conn.close()

    def filter_by_brand(self, brand):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE brand LIKE ?",
                       (f"%{brand}%",))
        rows = cursor.fetchall()
        conn.close()
        return rows

    # def update_car(self, car_id, car):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute("""
    #         UPDATE cars SET brand = ?, model = ?, year = ?, price = ?, status = ? WHERE rowid = ?
    #     """, (car.brand, car.model, car.year, car.price, car.status.value, car_id))
    #     conn.commit()
    #     conn.close()

    # def delete_car(self, car_id):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM cars WHERE rowid = ?", (car_id,))
    #     conn.commit()
    #     conn.close()

    def get_all_cars(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars")
        rows = cursor.fetchall()
        conn.close()
        return rows
