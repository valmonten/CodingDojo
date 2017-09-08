class Animal(object):
    def __init__(self,name,health):
        self.name=name
        self.health=health
        print self.name
        print self.health
    def walk(self):
        self.health-=1
        print self.name + " walked"
        return self
    def run(self):
        self.health-=5
        print self.name +" ran"

        return self
    def display_health(self):
        print self.health
        return self
Betsy = Animal("Betsy",1000)
Betsy.run()
Betsy.run()
Betsy.walk()
Betsy.walk()
Betsy.walk()
Betsy.display_health()

class Dragon(Animal):
    def __init__(self, name):
        self.health = 170
        self.name=name
    def fly(self):
        self.health-=10
        return self
    def display_health(self):
        print str(self.health) + " I am a Dragon"
        return self
class Dog(Animal):
    def __init__(self, name):
        self.health= 150
        self.name=name
    def pet(self):
        self.health+=5
        return self
Cookie = Dog("Cookie")
Cookie.walk()
Cookie.walk()
Cookie.walk()
Cookie.run()
Cookie.run()
Cookie.pet()
Cookie.display_health()

Drogon = Dragon("Drogon")
Drogon.fly()
Drogon.display_health()
Drogon.fly()
Drogon.display_health()

class Horse(Animal):
    def ride(self):
        self.health-=10
        print self.health
        return self

Epona = Horse("Epona", 1000)
Epona.ride()
Epona.display_health()        
