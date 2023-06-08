 # Q.2: Given a list of integers nums, write a function to ﬁnd the median of nums. 
# The median of a list of integers is the middle value when the list is sorted, 
# or the average of the two middle values if the list has an even number of elements. 

# For example, the median of the list [3, 5, 2, 1, 4] is 3, 
# the median of the list [3, 5, 2, 1, 4, 6] is (3 + 4) / 2 = 3.5 

def func(num):
    num2 = list(set(num))
    print(num2)
    if len(num2) % 2 != 0:
        a = (len(num2)//2)
        print(num2[a])
    
    elif len(num2) % 2 == 0:
        a = (len(num2)//2)
        print((num2[a] + num2[a-1])/2)
    
n1 = [3, 5, 2, 1, 4]
n2 = [3, 5, 2, 1, 4, 6]
func(n1)
func(n2)



print()

def median(n):
    new_nn = list(set(n))
    new_n = len(new_nn)
    if new_n%2 != 0:
        med = new_n//2
        print(new_nn[med])
    else:
        med1 = new_n//2
        print((new_nn[med1] + new_nn[med1-1])/2)

n1 = [3, 5, 2, 1, 4]
n2 = [3, 5, 2, 1, 4, 6]
median(n1)
median(n2)