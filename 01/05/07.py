class Cart:
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        res = []
        for i in self.goods:
            res.append(f'{i.name}: {i.price}')
        return res


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV('Sony', 100000)
cart.add(tv1)
tv2 = TV('Samsung', 120000)
cart.add(tv2)
table = Table('Stol', 15000)
cart.add(table)
notebook1 = Notebook('ASUS', 150000)
cart.add(notebook1)
notebook2 = Notebook('Samsung', 200000)
cart.add(notebook2)
cup = Cup('O', 1500)
cart.add(cup)
