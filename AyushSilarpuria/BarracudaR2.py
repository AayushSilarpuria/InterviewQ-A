# Q.1: Difference between mutable and immutable.
# Q.2: Explain why or how string are immutable and list are mutable.

list1 = [3,5,6,8,0]
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
 
 # List sorting:

list1 = [3,5,6,8,0]
def user_name(lists):
    
    for i in range(len(lists)):
        for j in range(len(lists)-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    print(lists)

user_name(list1)
        
print()

 # Dictionary Sorting in list format:

list1 = [
    {
        "Id": 3,
        "Name": "Iphone",
        "Price": "100",
        "Weight": 1
    },
    {
        "Id": 2,
        "Name": "Android",
        "Price": "300",
        "Weight": 1
    },
    {
        "Id": 7,  
        "Name": "Mac",
        "Price": "400",
        "Weight": 1
    },
    {
        "Id": 1,
        "Name": "Mac",
        "Price": "400",
        "Weight": 1
    }
]

def dic_sort(new_li):
    for i in new_li:
        sorted_list = sorted(new_li, key = lambda x: x['Id'])
    return sorted_list

print(dic_sort(list1))

print()

    # Another method without sorted 

def dic_sort(new_li):
    for i in range(len(new_li)):
        for j in range(len(new_li)-i-1):
            if new_li[j]['Id'] > new_li[j+1]['Id']:
                new_li[j], new_li[j+1] = new_li[j+1], new_li[j]
    print(new_li)

dic_sort(list1)

print()


# Q.4: Explain exception handling:

# try:
#     # Some Code...!
# except:
#     # Optional Block
#     # Handling of exception 
# else:
#     # Some code...
#     # excepte if no exception
# finally:        
#     # Some code...


# Q.5: With example explain exception handling.

d = {1:'ayu', 2: 'raj'}

try:
    print(d[1])
except KeyError as e :
    print(e)

print("hello")