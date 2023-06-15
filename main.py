

from model.car import Car
from model.enums.status import CarStatus


if __name__ == '__main__':
    print('Hello World!')

    car = Car(brand='Ford', model='Fiesta',
              year=2019, price=23000, status=CarStatus.NEW)
    print(car)
