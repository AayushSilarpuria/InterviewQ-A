# Q. Write a program to count the Digit, Upper_Case letter and Lower_Case letter.

list1= ["a","b", "c", "d", "A","B","C",1,2,3,4,5 ]

def datatype(list1):
    
     count_upper = 0
     count_lower = 0
     count_digit = 0
     list1 = str(list1)
     for i in list1:
         if i.isdigit():
             count_digit += 1
         if i.isupper():
              count_upper += 1
         if i.islower():
               count_lower += 1

     print(f"The Upper letter, count_lower, count_digit in list are {count_upper}, {count_lower}, {count_digit}.")

datatype(list1)