#STAQU || Backend Interview R1 |@17:00 - 18:00 (IST)


mylist = [1,2,3,4,4,6,7,7,8,8,0,-1]
print(mylist[-1:-3])

# Django works on which architectre
# what is drf
# what is python dictionary?
# which date types can be used as key in the dictionary?
# Make a dictionary with tuple as a key.
mydict = {(1,):"Ram", (2,):"Ayush"}
print(type(mydict))
print(mydict)



# print(output) a pair in tuple which sum is 7
mylist = [1,2,3,4,4,6,7,7,8,8,0,-1]
           
res = []
new = []
mylist = [1,2,3,4,4,6,7,7,8,8,0,-1]
for i in mylist:
    for j in mylist:
        if i + j+1 ==7:
            res = (i,j+1)
            a = (tuple(res))
            print(a)

        