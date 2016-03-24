class Person(object):
    def __init__(self, first_name, *args):
        self.first_name = first_name
        if len(args) > 0:
            self.last_name = args[0]
        if len(args) > 1:
            self.age = args[1]

p = Person("John", "Adams", 21)
print p.first_name
print p.last_name


class Profile(object):
    def __init__(self, first_name, *args, **kwargs):
        self.first_name = first_name
        if len(args) > 0:
            self.last_name = args[0]
        if len(args) > 1:
            self.age = args[1]
        if kwargs:
            self.last_name = kwargs.get('last_name','')
            self.age = kwargs.get('age', 0)


me = Profile("Harrison", age=21, last_name ="Kamau")
print me.first_name
print me.last_name



# def greet_me(**kwargs):
#     if kwargs is not None:
#         for key, item in kwargs.iteritems():
#             print "{} hey you {}".format(key,item)
#
# print greet_me(name="Harrrison")
