class Product(object):
    def __init__(self,price,name,weight,brand,cost):
        self.price=price
        self.name=name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status="for sale"
    def sold(self):
        self.status="sold"
        return self
    def tax_included(self, decimaltax):
        tax=self.price*decimaltax
        new_price=tax+self.price
        print new_price
        return new_price
    def returned(self, stats):
        if stats=="defective":
            self.status="defective"
            self.price=0
        if stats=="box":
            self.status="for sale"
        if stats=="used":
            self.status="used"
            self.price=int(self.price*0.8)
        return self
    def show_info(self):
        print "Price is "+ str(self.price)
        print "Name is "+ str(self.name)
        print "Weight is "+ str(self.weight)
        print "Brand is "+ str(self.brand)
        print "Cost is "+ str(self.cost)
        print "Status is "+ str(self.status)

apple = Product(10,"apple","10lbs","Honeycrisp",.05)
apple.sold()
apple.returned("used")
apple.tax_included(.1)
apple.show_info()
