class Employee:
    '''
        Add nums
    '''

    def __init__(self, *, name, age, *vars):
        self.name = name
        pass

    def add(self, first_num=2, *, second_num=3):
        return first_num + second_num


l = [1, 2]
A = Employee(name="kas", age=2, l)


print(A.add(3, second_num=6))
