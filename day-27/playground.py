# def add(*args):
#     return sum(args)
#
# print(add(3,5,6))

def calculate(n, **kwargs):
    for key,value in kwargs.items():
        print(kwargs['add'])

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

my_car = Car(make='Nissan', model='GT-R')
