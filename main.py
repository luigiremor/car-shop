

import json
from model.car import Car
from model.enums.status import CarStatus


def string_to_enum(status_string: str) -> CarStatus:
    try:
        return CarStatus[status_string.upper()]
    except KeyError:
        raise ValueError(
            f"Invalid status: {status_string}. Expected 'new' or 'used'.")


if __name__ == '__main__':
    print('Hello World!')

    car = Car(brand='Ford', model='Fiesta',
              year=2019, price=23000, status=CarStatus.NEW)
    print(car)

    try:
        with open("db/data.json", 'r+') as f:
            data = json.load(f)
            f.close()
    except FileNotFoundError:
        print('File not found')

    for dado in data:
        print(dado)
        dado['status'] = string_to_enum(dado['status'])
        print(Car(**dado))
