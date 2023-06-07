# Akamai
# sunovaa tech
# 1. Generator vs iterator

# 2. how to find if a function is generator or not
import inspect
def foo():
    return "foo"
def bar():
    yield "bar"

print(inspect.isgeneratorfunction(foo))
print(inspect.isgeneratorfunction(bar))

# isclass, ismodule, isfunction, inspect.getmro(c) {To see class hierarchy.}
# 3. SQL: Employee(name, salary). find min salary

# 4. Class method vs static method vs instance method

    # Instance methods need a class instance and can access the instance through self . 
    # Class methods don't need a class instance. 
    # They can't access the instance ( self ) but they have access to the class itself via cls . 
    # Static methods don't have access to cls or self .

# 5. When you use GET method for getting API;  explain the flow when the request get to the server.

import requests

response = requests.get("https://www.boredapi.com/api/activity")
print(response.status_code)
# 200 means Success.
print(response.json())
print()

import json

def jprint(obj):
    text = json.dumps(obj, sort_keys =True, indent= 4)
    print(text)

jprint(response.json())
print()

action = response.json()['activity']
jprint(action)

print()

# 6.diff between tuple and list

# 7. Which can be used as a key in dictionary- tuple or list.

# 8. Find how many seconds it will take to run this function through generator

import timeit

start = timeit.default_timer()

def func():
    print("Hello")
func()

stop = timeit.default_timer()
print("Time:", stop - start)

# Already provided questions
# 1.       What is a list and tuples?

# 2.       How do you dictionary Tuples and List?

# 3.       How to migrate a list?

# 4.       How to migrate data in Django?

# 5.       Project explanation with Django?

# 6.       Explain Viewed files?

# 7.       What is the middle layer? Explain.

# 8.       Coding – find the strong number

# 9.       Projects and Roles and responsibilities of Current projects?

# 10.   What are Methods?

# 11.   How will you run a project in Django?

# 12.   What are routines?

# 13.   How to create views ?

# 14.   What is the communication between Model file and Viewed file?


# Some more questions
# Back end API when you call the browser what happens ?
# How do you update the column you want to add in the database?
# What do you mean by list ?
# What do you mean by pearl staes ?
# What is a static method?
# What are the project you have done with python and what is your responsibility in the project ?

