# Q.1: Print as an output:
a = ['a','e','b','e','c','a','d','a','c','a','e']
# result = {'a': 4, 'b': 1, 'c': 2, 'd': 1, 'e': 3}

# Method:1
def count_item(ls):
    count_i = {}
    for i in ls:
        if i in count_i:
            count_i[i] += 1
        else:
            count_i[i] = 1
    return count_i

print(count_item(a))

# Method:2

d = {i: a.count(i) for i in a}
print(d)
# Q.2: Find the 2nd highest Salary from Employed Table.
# Q.3: How to change datatype from perticular column of table.
# Q.4: What is list comprehension.

# Q.5: Write a progrma for Generator and Explain Generator.
def sqr(n):
    for i in range(1,n+1):
        yield i*i

a = sqr(3)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# It only iterate 3 times if range is small then asking next output for rest of next it through error.