# Quest Global
# 29 Apr 23 10AM

# Q1. What is multithreading and multiprocessing? Explain with the help of real world examples.
# Q2. How memory managed in python?
# Q3. Explain Docker?
# Q4. Why we use docker if python already has virtulization?
# Q5. What is multiple inheritance and abstract method?
#     Use Example of shape, square, triangle class. 

# Q6. Reverse the list without using any built-in methods:
list1 = [45, 41, 3, 21, 16, 89, 5]
print(list1)
for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)


