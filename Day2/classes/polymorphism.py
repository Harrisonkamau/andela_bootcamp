'''This is an examle of polymorphism'''
class SchoolMember:
    ''' represents a school member '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "Initalized school member name: {}".format(self.name)

    def tell(self):
        ''' Tell my details '''
        print 'Name: {} Age: {}'.format(self.name, self.age)


class Teacher(SchoolMember):
    ''' Represents a teacher '''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'Initialized teacher Name:{}'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary {:d}'.format(self.salary)


class Student(SchoolMember):
    ''' Represents a student '''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'Initialized student Name: {}'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: {:d}'.format(self.marks)

murungaru = Teacher("Mr. Murungaru", 39, 300000)
print murungaru.tell()

kinuthia = Student("Kinuthia Ndungu", 24, 44000)
print kinuthia.tell()
