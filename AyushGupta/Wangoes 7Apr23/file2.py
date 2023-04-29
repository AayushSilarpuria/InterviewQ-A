# Consider a list with integers, lst=[2,3,1,5,4,3,2,1]
# In the list 2,3, and 1 are duplicates so output should be : [2,3,1]

lst=[2,3,1,5,4,3,2,1]
new = []
for i in lst:
    y = lst.count(i)
    if y>1:
        if i not in new:
            new.append(i)
#new = list(set(new))
print(lst)
print(new)