import csv
import os
from flask import flash


class Wishlist:

    filename = 'items.txt'

    def __init__(self):
        pass

    def read_csv(self):
        '''Read in csv file'''
        if not os.path.isfile(self.filename):
            return []
        with open(self.filename, 'r') as csvfile:
            rows = csv.DictReader(csvfile)
            items = [row for row in rows]
            return items

    def write_csv(self, items):
        '''Write out csv file'''
        with open(self.filename, 'w+') as csvfile:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in items:
                try:
                    writer.writerow(item)
                except:
                    flash('Item not added!')
            
            flash('Item added :-)')


    def get_list(self):
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
