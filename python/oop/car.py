class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price=price
        self.fuel=fuel
        self.mileage=mileage
        self.speed=speed
        if self.price > 10000:
            self.tax=0.15
        else:
            self.tax=0.12
        self.display_all()
        
    def display_all(self):
        print "Price: "+ str(self.price) 
        print "Mileage: "+ str(self.mileage)
        print "Speed: "+ str(self.speed)
        print "Fuel: "+ str(self.fuel)
        print "Tax: "+ str(self.tax)
ferrari = Car(1000000, "200mph", "Full", "10mpg")
car2 = Car(1, "10mph", "Full", "100mpg")
car3 = Car(15000, "180mph", "Half tank", "22mpg")
car4 = Car(15000, "180mph", "Half tank", "22mpg")
car5 = Car(15000, "180mph", "Half tank", "22mpg")
car6 = Car(15000, "180mph", "Half tank", "22mpg")

