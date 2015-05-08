import csv
import os


class Wishlist:

    def __init__(self):
        pass

    def read_csv(self):
        '''Read in csv file'''
        filename = 'list.txt'
        if not os.path.isfile(filename):
            return []
        rows = csv.DictReader(open(filename))
        items = [row for row in rows]
        return items

    def write_csv(self):
        '''Write out csv file'''
        pass

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
