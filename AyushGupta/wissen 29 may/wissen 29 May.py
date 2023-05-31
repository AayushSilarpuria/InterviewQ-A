# Wissen Technology private limited
# 29 may

# 1. What is the Output:
# class A:
#     def fun(a,b):
#         return a+b

# class B(A):
#     def fun(p,q,r):
#         return p+q/r

# b1= B()
# b1.fun(10,20)

# b1.fun(10,20,30)


# 2. Print the sum of the square of the odd numbers of the list.
mylist = [1, 2, 3, 4, 5, 6, 7]
print(mylist)

new = []
for i in mylist:
    if i % 2:
        new.append(i)

new_res = [x**2 for x in new]
print(new_res)
print(sum(new_res))


# 3.
# Input:
l1 = [1, [2, 3, [4, 5]]]
# Output: l1 = [1,2,3,4,5]


# 4. What is chmod()


# 5. display the author names with more than 10 books
# select author from tabelname
# where books>10


# 6. Print the pair whose difference is k
# num = [1,2,3,4,5,6,7,8]
# k=2
# for i in num:
#     for j in num:
#         if i-j == k:
#             print(i,j)


# 7. Print the largest even length word.
sample = "Be not afraid of greatness some are born great some achieve greatness and some have greatness thrust upon them"


# 8. Take input from user and print how many unique numbers are there
# num = input("enter a number: ")
# print(num)

# res = ''
# for i in num:
#     if i not in res:
#         res = res + i
#     #print(i)
# print(res)
# print(len(res))
