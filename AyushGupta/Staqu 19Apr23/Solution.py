mylist = [1,2,3,4,4,6,7,7,8,8,0,-1]
# print(output) a pair in tuple which sum is 7

# This is I did in the interview.
"""
res = []
new = []
mylist = [1,2,3,4,4,6,7,7,8,8,0,-1]
for i in mylist:
    for j in mylist:
        if i + j+1 ==7:
            res = (i,j+1)
            a = (list(res))
            print(a)
"""

# Acutal solution
mylist = [1, 2, 3, 4, 4, 6, 7, 7, 8, 8, 0, -1]

output = []
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i] + mylist[j] == 7:
            output.append((mylist[i], mylist[j]))
print(output)
print(list(set(output)))  # If you donot want duplicate pairs.
