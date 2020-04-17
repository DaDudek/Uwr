from city_cart import CityCart
from transport_cart import TransportCart
from power_station_cart import PowerStationCart
from tax_cart import TaxCart
from cart import Cart
from hidden_cart_reader import HiddenCartReader


class Banker:
    def __init__(self, file):
        self.hidden_carts=[]
        self.file = file
        self.sector = {}  # rozmiar państwa
        self.id_cities = [1, 3, 6, 8, 9, 11, 13, 14, 16, 18, 19, 21, 23, 24, 26, 27, 29, 31, 32, 34, 37, 39]
        self.id_power_station = [12, 28]
        self.id_transport = [5, 15, 25, 35]
        self.id_event = [0, 2, 7, 10, 17, 20, 22, 30, 33, 36, ]
        self.id_hidden = [2, 7, 17, 22, 33, 36]
        self.id_tax = [4,38]
        self.id = {"cities": self.id_cities, "power_stations": self.id_power_station, "transport": self.id_transport,
                   "event": self.id_event, "hidden": self.id_hidden, "tax": self.id_tax}
        self.carts = []

    def make_hidden_carts(self, hidden_carts_file):
        hidden_carts_reader = HiddenCartReader(hidden_carts_file)
        self.hidden_carts = hidden_carts_reader.make_hidden_carts()

    def make_tax_cart(self, line):
        line.strip()
        split_line = line.split(";")
        counter = 0
        for word in split_line:
            if counter == 0:
                coordinate = int(word)
            if counter == 1:
                section = word
                self.sector[word] =[coordinate] if word not in self.sector else self.sector[word] +[coordinate]
            if counter == 2:
                name = word
            if counter == 3:
                amount_of_tax = int(word) * 1000
            counter += 1
        cart = TaxCart(coordinate, name, section, amount_of_tax)
        return cart

    def make_event_cart(self, line):
        line.strip()
        split_line = line.split(";")
        counter = 0
        for word in split_line:
            if counter == 0:
                coordinate = int(word)
            elif counter == 2:
                name = word
            counter += 1

        cart = Cart(coordinate, name,)
        return cart

    def make_city_cart(self, line):
        line.strip()
        split_line = line.split(";")
        counter = 0
        house_counter = 0
        value_with_houses = {}
        for word in split_line:
            if counter == 0:
                coordinate = int(word)
            elif counter == 1:
                section = word
                self.sector[word] = [coordinate] if word not in self.sector else self.sector[word]+[coordinate]
            elif counter == 2:
                name = word
            elif counter == 3:
                cost = int(word) * 1000
            elif counter == 4:
                house_prize = int(word) * 1000
            elif counter == 5:
                hotel_prize = int(word) * 1000
            elif counter == 6:
                mortgage_value = int(word) * 1000
            elif counter in range(7, 12):
                value_with_houses[house_counter] = int(word) * 1000
                house_counter += 1
            elif counter == 12:
                value_with_hotel = int(word) * 1000
            counter += 1

        cart = CityCart(coordinate, name, section, cost, house_prize, hotel_prize, mortgage_value,
                            value_with_houses, value_with_hotel, )
        return cart

    def make_transport_cart(self, line):
        line.strip()
        split_line = line.split(";")
        counter = 0
        house_counter = 0
        value_with_houses = {}
        for word in split_line:
            if counter == 0:
                coordinate = int(word)
            elif counter == 1:
                section = word
                self.sector[word] = [coordinate] if word not in self.sector else self.sector[word] +[coordinate]
            elif counter == 2:
                name = word
            elif counter == 3:
                cost = int(word) * 1000
            elif counter == 6:
                mortgage_value = int(word) * 1000
            elif counter in range(7, 11):
                value_with_houses[house_counter] = int(word) * 1000
                house_counter += 1
            counter += 1
        cart = TransportCart(coordinate, name, section, cost, mortgage_value, value_with_houses, )
        return cart

    def make_power_station_cart(self, line):
        line.strip()
        counter = 0
        split_line = line.split(";")
        for word in split_line:
            if counter == 0:
                coordinate = int(word)
            elif counter == 1:
                section = word
                self.sector[word] = [coordinate] if word not in self.sector else self.sector[word] +[coordinate]
            elif counter == 2:
                name = word
            elif counter == 3:
                cost = int(word) * 1000
            elif counter == 6:
                mortgage_value = int(word) * 1000
            counter += 1

        cart = PowerStationCart(coordinate, name, section, cost, mortgage_value)
        return cart

    def make_all_carts(self):
        counter = -1
        for line in self.file:
            if counter == -1:
                counter += 1
                continue
            elif counter in self.id_event:
                self.carts.append(self.make_event_cart(line))
            elif counter in self.id_tax:
                self.carts.append(self.make_tax_cart(line))
            elif counter in self.id_cities:
                self.carts.append(self.make_city_cart(line))
            elif counter in self.id_transport:
                self.carts.append(self.make_transport_cart(line))
            elif counter in self.id_power_station:
                self.carts.append(self.make_power_station_cart(line))
            counter += 1
        self.make_hidden_carts(open("random_carts.csv"))
