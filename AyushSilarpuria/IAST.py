# Q.1: Sort the array without using sort method.
arr1 = [2, 1, 5, 7, 3, 4]
def sort(arr):
    new_arr = []
    for i in arr:
        #while i not in new_arr:
        if i not in new_arr:
            
            new_arr.append()
        elif 






# define a function to perform the sorting
def sort_arr(arr):
    # iterate through the list and compare adjacent elements
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                # swap their positions if necessary
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # return the sorted list
    return arr

# call the function and print the sorted list
sorted_arr = sort_arr(arr1)
print(sorted_arr)





# Q.2:
d = {'k1':'v1', 'k2':'v2'}
print(d.items())
print(d.keys())
print(d.values())

d1 = str(d.keys())
d2 = str(d.values())
# key K1 - value V1
# key K2 - value V2
print(f" Key {d1[0]} - Value {d2[0]}")
print(f" Key {d1[1]} - Value {d2[1]}")

input = "IAST is a automotive Company"
# output = "Company automotive a is IAST”

str = input.split()
#for let in str:
new_list = str[::-1]
print(new_list)