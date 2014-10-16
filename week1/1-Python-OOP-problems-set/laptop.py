#!/usr/bin/env python3


class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        self.profit = self.final_price - self.stock_price
        print(self.profit)


class Laptop(Product):

    def __init__(self, diskspace, RAM):
        self.diskspace = diskspace
        self.ram = RAM


class Smartphone(Product):
    def __init__(self, display_size, mega_pixels):
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    def __init__(self, name):
        self.store_name = name

    def load_new_products(self, product, count):
        self.new_product = product
        self.product_count = count

    def list_products(self, product_class):



new_product = Product('HP HackBook', 1000, 1243)
new_product.profit()  # 243
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)
store.load_new_products(laptop, 10)

store.list_products(Laptop)  # HP HackBook - 10
