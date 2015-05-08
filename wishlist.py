class Wishlist:
    def __init__(self):
        pass

    def read_csv(self):
        # add real logic to read list from CSV file.
        # csv dict reader
        return [{"name":"keyboard", "quantity":2, "price":110},
                {"name":"mouse", "quantity":3, "price":10}]

    def write_csv(self):
        pass
    
    def get_list(self):
        items = self.read_csv()
        return items

    def total_count(self):
        items = self.get_list()
        total = 0
        for item in items:
            total += item['quantity']
        return total
    
    def total_cost(self):
        items = self.get_list()
        total = 0
        for item in items:
            total += item['price'] * item['quantity']
        return total
    

    

    
    
    


    
