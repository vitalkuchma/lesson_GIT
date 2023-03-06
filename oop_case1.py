class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


t1 = Table(1.5, 1.8, 2.75)
t2 = DeskTable(0.8, 0.6, 0.9)
print(t2.square())


# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.
class Car:
    def __init__(self, brand, model, color, prise):
        self.brand = brand
        self.model = model
        self.color = color
        self.prise = prise


class CarShowroom(Car):
    def car_list(self):
        for car in sell_list:
            return self.brand, self.prise

    def car_sale(self):
        pass


a1 = CarShowroom('Mazda', 'sedan', 'red', 50000)
a2 = CarShowroom('BMW', 'roadster', 'yellow', 70000)
a3 = CarShowroom('Peugeot', 'suv', 'white', 35000)
a4 = CarShowroom('Volvo', 'suv', 'black', 75000)

sell_list = [a1, a2, a4]

print(sell_list)



