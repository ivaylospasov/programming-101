#!/usr/bin/env python3


class Product(object):

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price,
                 diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store(object):

    income = 0

    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            if product in self.products.keys():
                self.products[product] += count
            else:
                self.products[product] = count

    def list_products(self, product_type):
        for product in self.products.keys():
            if isinstance(product, product_type):
                print(product.name + " - " + str(self.products[product]))

    def sell_product(self, product):
        for product in self.products.keys():
            if self.products[product] > 0:
                Store.income += product.profit()
                self.products[product] -= 1
                return True
        return False

    def total_income(self):
        return Store.income


def main():
    new_product = Product('HP HackBook', 1000, 1243)
    print(new_product.profit())

    store = Store('Laptop.bg')

    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    store.load_new_products(laptop, 10)
    store.list_products(Laptop)

    store.load_new_products(smarthphone, 2)

    print(store.sell_product(smarthphone))
    print(store.sell_product(smarthphone))
    print(store.sell_product(smarthphone))
    print(store.total_income())


if __name__ == '__main__':
    main()
