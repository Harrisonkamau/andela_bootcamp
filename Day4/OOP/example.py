# animal_count = 0

class Animal(object):
    animal_count = 0
    def __init__(self, name):
        self.name = name
    # global animal_count - TUsed when the variable is defined outside the parent class
        Animal.animal_count += 1
        # self.animal_count += 1
        self.id = Animal.animal_count

    def eat(self):
        print "Yeah, I eat:)"

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.legs = 4

    def walk(self):
        return "I walk with {0} legs".format(self.legs)

my_cat = Cat("Wafula")
print my_cat.eat()
print my_cat.walk()
print my_cat.id, ",ID#", my_cat.id

another_cat = Cat("pussy")
