# def add(*args):
#     return sum(args)
#
# print(add(3,5,6))

def calculate(n, **kwargs):
    for key,value in kwargs.items():
        print(kwargs['add'])

calculate(2, add=3, multiply=5)