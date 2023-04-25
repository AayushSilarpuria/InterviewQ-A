# Acuity Knowledge partner  25 Apr 23

# 1. Write fibonacci series using generator upto 10 numbers. 
# 2. Write a function calculate, which given a string like "4+1*1+1"
    # return the result of the formula in the string 
# 3. Write multiple decorator a any specific function.
# 4. Write union and intersection of set1 and set2.
# 6. Write dictionary comprehension. 
# 7. How do you process json 
# 8. Convert this dictionary in string.
# 9. Send data of mydict into a file in json format. 
mydict = {'a': 1,
          'b': 2, 
          'c': 3, 
          'd': 4,
          'e': 5,}


# 5. Write a list comprehension for a given list in which even number get squared and odd number gets cube.
lst = [1,4,6,2,-1,11,9]
output = [1, 16, 36, 4, -1, 1331, 729]
# Solution
y = [x**2 if x%2==0 else x**3 for x in lst]
print(y)
