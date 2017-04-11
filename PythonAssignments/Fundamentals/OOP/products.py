class Product(object):
    def __init__(self, price, item, weight, brand, cost, status):
        self.price = price
        self.item = item
        self.weight= weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"

    def add_tax(self):
        tax = .075
        self.tax=self.price +  self.price * tax
        print self.tax

    def Return(self, reason):
        if reason == "unopened":
            self.status = "for sale"
        elif reason == "damaged":
            self.price = 0
        else:
            self.price= self.price * .8
            self.status = "for sale"

    def display_all

product1 = Product(2.75, "soap", "32oz.", "Coast", 1.75, "for sale")
product2= Product(3, "tothpaste", "12oz.", "Crest", 2.25, "for sale")
product3 = Priduct(4, "brush", "14oz.", "elle brush", 3, "for sale")
print product1.add_tax()
