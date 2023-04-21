# ManekTech 4PM 21 Apr 23
 
# Data structure
# what is bubble sort
# Make a program for bubble sort

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

mylist = [2,6,8,1,5,8,3,4,9]
bubbleSort(mylist)


