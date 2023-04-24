# Q.1: Difference between mutable and immutable.
# Q.2: Explain why or how string are immutable and list are mutable.

list = [3,5,6,8,0]
def new_list(list):
    print(list)
    
print() 

list_new = id(list)
print(list_new)
print(id(new_list))

print()

x=10
print(id(x))
x= 11
print(id(x))


# Q.3: Write a program to sort list and a dictionary in sequantial manner.
def user_name(lists):
    for i in range(len(lists)):
        

# Q.4: Explain excep
try:
except:

error:
        

dic = {1:'ayu', 2: 'raj'}
try:
    print(dic[1])
except KeyError as e :
    print(e)

print("hello")