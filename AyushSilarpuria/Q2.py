#  Round-2 Interview: 

# Q. Write a program to find maximum sum of Array and consider Sub-Array method for programming.

# Sub-Array: Number cannot be rearrange and array is used as it is manner for sum.

arr = [-2,2,1,-5]
# [-2] [2] [1] 
# [-2,2] [-2,2,1] [2,1] 
def arr_sum(arr):
    n = len(arr)
    max_sum = -10
    for i in range(n):
        arr1 = []
        for j in range(i,n):
            arr1.append(arr[j])
            max_sum = max(sum(arr1), max_sum)
            print("Maximum Sum:", max_sum, "" sum(arr1))
            print()
    return max_sum
print(arr_sum(arr))
        