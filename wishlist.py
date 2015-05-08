#!/usr/bin/env python
import csv
import os


class Wishlist:

    filename = 'items.txt'

    def __init__(self):
        pass

    def read_csv(self):
        '''Read in csv file'''
        if not os.path.isfile(self.filename):
            return []
        with open(self.filename) as csvfile:
            rows = csv.DictReader(csvfile)
            items = [row for row in rows]
            return items

    def write_csv(self, name, quantity, price):
        '''Write out csv file'''
        with open(self.filename, 'a') as csvfile:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow({'name': name, 'quantity': quantity, 'price': price})

    def get_list(self):
        # This function seams redundant to me.
        # Can we just use read_csv()?
        items = self.read_csv()
        return items

    def total_type(self):
        items = self.get_list()
        total = 0
        for item in items:
            total += 1
        return total

    def total_count(self):
        items = self.get_list()
        total = 0
        for item in items:
            total += int(item['quantity'])
        return total

    def total_cost(self):
        items = self.get_list()
        total = 0
        for item in items:
            total += int(item['price']) * int(item['quantity'])
        return total
