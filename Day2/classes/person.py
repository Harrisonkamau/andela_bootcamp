# Person class
class Person(object):
    """docstring for classname"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk_about_yourself(self):
        print "My name is {} and i'm {} years old".format(name=self.name, age=self.age)
# Create an object from a person class
harrison = Person("Harrison", 24)
harrison.talk_about_yourself()
