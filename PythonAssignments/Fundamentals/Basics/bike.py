class Bike(object):

    def __init__(self,name, price, max_speed, miles):
        self.name= name
        self.price= price
        self.max_speed = max_speed
        self.miles = miles



    def display_info(self):
        print self.name
        print self.price
        print self.max_speed
        print self.miles


    def ride(self):
        self.miles = self.miles + 10
        print "Nice ride! Miles now equal: " + str(self.miles)

    def reverse(self):
        self.miles = self.miles - 5
        print "Reversing!! Miles now equal: " + str(self.miles)

bike1= Bike("bike1" ,5500, 150, 22500)
bike2 = Bike("bike2", 12500, 210, 500)
bike3 = Bike("bike3", 22500, 250, 10)
bike1.display_info()
bike1.ride()
bike1.reverse()
