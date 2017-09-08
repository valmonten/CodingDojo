class Bike(object):
    def __init__(self, price, max_speed):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def display_info(self):
        print "Price is {}, Max speead is {}, and miles are {}".format(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles+=10
        print "Riding"
        return self
    def reverse(self):
        if self.miles>5:
            self.miles-=5
        print "Reversing"
        return self
bike1=Bike(200,"20mph")
bike2=Bike(10000, "60mph")
bike3=Bike(0,"5mph")
bike1.ride().ride().ride().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()