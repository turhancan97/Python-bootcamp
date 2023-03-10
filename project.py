import csv
import datetime
import os

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self):
        self.description = "Klasik Pizza"
        self.cost = 15.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class Margarita(Pizza):
    def __init__(self):
        self.description = "Margarita Pizza"
        self.cost = 20.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.cost = 25.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class SadePizza(Pizza):
    def __init__(self):
        self.description = "Sade Pizza"
        self.cost = 10.0

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

class Zeytin(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Zeytin"
        self.cost = 2.0

class Mantarlar(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Mantarlar"
        self.cost = 3.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Keci Peyniri"
        self.cost = 4.0

class Et(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Et"
        self.cost = 5.0

class Sogan(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Soğan"
        self.cost = 1.0

class Misir(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Mısır"
        self.cost = 2.0

def main():
    f = open('Menu.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()


    pizza = None
    while not pizza:
        try:
            choice = int(input("Lütfen bir pizza seçiniz: "))
            if choice == 1:
                pizza = Klasik()
            elif choice == 2:
                pizza = Margarita()
            elif choice == 3:
                pizza = TurkPizza()
            elif choice == 4:
                pizza = SadePizza()
        except ValueError:
            continue

    while True:
        try:
            choice = int(input("Lütfen bir sos seçiniz (0 ile bitirin): "))
            if choice == 0:
                break
            elif choice == 11:
                pizza = Zeytin(pizza)
            elif choice == 12:
                pizza = Mantarlar(pizza)
            elif choice == 13:
                pizza = KeciPeyniri(pizza)
            elif choice == 14:
                pizza = Et(pizza)
            elif choice == 15:
                pizza = Sogan(pizza)
            elif choice == 16:
                pizza = Misir(pizza)
        except ValueError:
            continue

    print("Toplam fiyat:", pizza.get_cost())

    name = input("Lütfen isminizi giriniz: ")
    tc = input("Lütfen TC kimlik numaranızı giriniz: ")
    card_number = input("Lütfen kredi kartı numaranızı giriniz: ")
    card_cvv = input("Lütfen kredi kartı CVV numaranızı giriniz: ")

    now = datetime.datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    with open('Orders_Database.csv', mode='a', newline='') as orders_file:
        fieldnames = ['Pizza', 'Name', 'TC', 'Card Number', 'Order Description', 'Order Time', 'Card CVV']
        writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
        if os.stat("Orders_Database.csv").st_size == 0:
            writer.writerow({'Pizza': fieldnames[0], 'Name': fieldnames[1], 'TC': fieldnames[2], 'Card Number': fieldnames[3], 'Order Description': fieldnames[4], 'Order Time': fieldnames[5], 'Card CVV': fieldnames[6]})
        writer.writerow({'Pizza': pizza.get_description(), 'Name': name, 'TC': tc, 'Card Number': card_number, 'Order Description': pizza.get_description(), 'Order Time': current_time, 'Card CVV': card_cvv})

if __name__ == "__main__":
    main()