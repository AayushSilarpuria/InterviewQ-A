# Do all below question by Normal way and by list comprehension
# Q.1=>  
Input1 = ['1','0','2','1','2', '0'] 
# Output = ["callback","appointment","lost","callback","lost"]

# In List format:
def place(list1):

    new_list = []
    for n in list1:
        if n == '0':
            new_list.append("appointment")
        elif n == '1':
            new_list.append("callback")
        elif n == '2':
            new_list.append("lost")
    
    return new_list

print(place(Input1))

# In Dictionary format:

dictno = {'0': "appointment", '1': "callback", '2': "lost"}

 # Method:1 
output = []
for item in Input1:
    output.append(dictno[item])
print(output)

 # Method:2
output = [ dictno[item] for item in Input1 ]
print(output)
        

# Q.2=> 
Input2 = "aaabbccccdddaaaeeefff" 
# Output = "a3b2c4d3a3e3f3"

def int_str(str2):

    string = ""
    count = 1
    for n in range(len(str2)):
        if n == len(str2)-1 or str2[n] != str2[n+1] :
            string += str2[n] + str(count)
            count = 1

        else:
            count += 1
    return string

print(int_str(Input2))