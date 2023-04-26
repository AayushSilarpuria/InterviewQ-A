# Q.1: Count number of Duplicate item and write it as output.
word = "aeroplane"

dup_word = []

for i in word:
    if word.count(i) > 1:
        count = word.count(i)
        if i not in dup_word:
            dup_word.append(i)
print(f"{i}: {count}")
print(dup_word)


# Q.2: Write SQL Queries:

# emp(emp_id, emp_name, salary, dep_id)
# dep(dep_id, dep_name, loc)

# 1. Write Queries to find employee name who have salary more then 50000.

# select emp_name, salary
# from emp
# where salary > 50000

# 2. Write Queries to find emp_name and their dep_name.

# select emp.emp_name , dep.dep_name
# from emp
# join dep
# where emp.dep_id = emp.dep_id;