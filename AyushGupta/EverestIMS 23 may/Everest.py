# 1. Abstraction
from abc import ABC, abstractclassmethod


class My(ABC):

    def year(self, age):
        self.age = age
        age = 75


class Father(My):

    def __init__(self, age):
        self.age = age

    def year(self):
        print('Age is', self.age, 'years old.')


obj = Father(44)
obj.year()


obj2 = My()
print(obj.age)

# 2. List methods

mylist = [4, 6, 7]
mylist.insert(0, 88)
print(mylist)

mylist[0] = 99
print(mylist)

mylist.insert(5, 'A')
print(mylist)


# mylist.remove('B')
print(mylist)

mylist.pop()
print()


# 3. decorator function
def greet(fx):
    def mfx(*args):
        print("************")
        print('Good Morning')
        fx()
        print("************")
    return mfx


@greet
def name(a=5, n=7):
    print(f'Sum of {a} and {n} is {a+n}')
    print("Ayush Gupta")


# call the function
name()


@greet
def func():
    print("Hi")


func()

# 5. show name using emailid in sql
