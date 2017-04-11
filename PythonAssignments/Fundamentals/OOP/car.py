class Car(object):
    def __init__(self, name, brand,price, color, mileage, fuel_efficiency):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.mileage = mileage
        self.fuel_efficiency=fuel_efficiency

    def tax(self):
        if self.price > 10000:
            self.tax = self.price * .15
        else:
            self.tax = self.price * .12


    def display_all(self):
        print "Here is the car that fits your specifications: "
        print "Car brand:  " + self.brand
        print "Car price:  " + str(self.price)
        print "Car color:  " + self.color
        print "Car mileage:  " + str(self.mileage)
        print "Car fuel efficiency:  " + self.fuel_efficiency
        print "Car tax:  " + str(self.tax)


car1 = Car( "car1", "Honda", 9999, "Red", 15, "25mpg")
print car1
# # car1.tax()
# # car1.display_all()
mileage = raw_input("Please enter how many miles you want on the car: ")
fuel_efficiency = raw_input("Please enter how many miles/gallon are you looking for: ")
price = raw_input("Please enter how much you want to spend for a car: ")

# car2 = Car( "car2", "Honda", float(price), "Red", fuel_efficiency, mileage)
# car2.tax()
# car2.display_all()
