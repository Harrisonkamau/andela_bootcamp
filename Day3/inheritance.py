class Parent(object):
    def parent_method(self):
        print "parent method"

    def shared_method(self):
        print "shared method"

# Inheritance in play
class Child(Parent):
    def parent_method(self, output_string):
        print "child method {}".format(output_string)

child = Child()
child.parent_method()
