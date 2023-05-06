# LTI MINDTREE
# 4 May 2023 4:20PM

# Q1. What is python and how it is different from other programming language?
# Q2. Python is interpreted or compiled type language?
# Q3. What is django?
# Q4. How memory managed in python?
# Q5. How Exception Handled In Python?

# Q6. Reverse the given string
str = 'LTI Mindtree'

# Method 1
new = str[::-1]
print(new)


# Method 2
new = reversed(str)
print(''.join(new))


# Method 3
new = list(str)
new.reverse()
print(new)
print(''.join(new))


# Method 4
new = ""
for i in str:
    new = i + new
print(new)
