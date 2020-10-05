class Person(object):
    def __init__(self, name):
        self.name = name


class Citizen(object):
    def __init__(self, cit):
        self.citizen = cit


class Student(Person, Citizen):
    def __init__(self, name, myclass, cit):
        # super().__init__(name)
        Person.__init__(self, name)
        Citizen.__init__(self, cit)
        self.myclass = myclass


c = Student("ka", 'class6', 'Indian')
print(c.__dict__)
