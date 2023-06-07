#Q.1: Program to print pyramid of n steps 
#Example 
#i/p n =  5 
#o/p =>  
#     * 
#    *** 
#   ***** 
#  ******* 
# *********


def pattern(n):
    for i in range(n):
        for j in range(i,n):
            print(' ', end= '')
        for j in range(i):
            print('*', end='')
        for j in range(i+1):
            print('*', end='')
        print()

pattern(5)

print()


# Q.2: Program to find all possible pairs with given sum at 0th index. 
#Example 
#i/p = [17,3,10,5,7,8,6,9] here sum is 17 
#o/p => [(10,7),(8,9)] 

n = [17,3,10,5,7,8,6,9]

def sum_lst(n):
    lst_n = []

    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == 17:
                lst_n.append((n[i], n[i+1]))

    return lst_n

print(sum_lst(n))