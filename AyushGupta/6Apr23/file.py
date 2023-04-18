"""
6 april interview
Accolite Digital India Private Limited
Vedika 8309102594
sriram.r@accolitedigital.com

1. If we write tables in models.py then makemigrations then migrate.
what will happen if we hit the command migrate after deleting the table.

2. middleware in django

3. output
t = (2,3,)
t[2] = 4
print(t)   #TypeError: 'tuple' object does not support item assignment


4. output
t = [2,3]
t[2] = 4
print(t)   #IndexError: list assignment index out of range


6. Decorator 
input : 
def display(name):
    print(name)

output:
******
name
******

7. 
input :  AAAAERCCEETTTAA
output:  A4E1R1C2E2T3A2
"""
# 5. output
t = (2,3)
t = t*2
print(t)   #(2, 3, 2, 3)




"""
Answer of Q2: How does Middleware work? 🤔
When a user makes a request from your application, a WSGI handler is instantiated, which handles the following things:

Imports project's settings.py file and Django exception classes.
Loads all the middleware classes which are written in MIDDLEWARE tuple located in settings.py file
Builds list of methods which handle processing of request, view, response & exception.
Loops through the request methods in order.
Resolves the requested URL
Loops through each of the view processing methods
Calls the view function
Processes exception methods (if any)
Loops through each of the response methods in the reverse order from request middleware.
Builds a return value and makes a call to the callback function.
"""