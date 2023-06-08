# Q.1: Create Class and add a and b.
# a = Vector(1, 2)
# b = Vector(3, 4)
# when I print c i should get Vector(4,6)

######################

# class A:
        
#     def b(self, num1, num2, num3, num4):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3 
#         self.num4 = num4
#         self.adding1 = num1+num3 
#         self.adding2 = num2+num4
        
        
# s = A(1,2,3,4)
# s.adding1()
# s.adding2()

########################


# Q.2: Create a Generator.

def a(func):
    for i in range(func):
        yield i*i

b= a(4)   
print(next(b))
print(next(b))
print(next(b))

print()

# Q.3: Create a Decorator.

def dec(func):
    def greet():
        print("*****")
        func()
        print("*****")
    return greet()

@dec
def hello():
    print("Hello!")