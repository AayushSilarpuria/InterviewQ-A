# Q.1: Write on Decorator program.
def person(n):
    def name(let):
        print("Ayush")
    return name

n = "a,b,c,d"
l = person(n)
print(l)



# Q.2: 
input_arr = [0,1,1,0,1,0]
#output_arr = [0,0,0,1,1,1]


def int_a(input_arr):
    new_z = []
    new_one = []
    for i in input_arr:
        if i == 0:
            new_z.append(i)
        else: 
            new_one.append(i)
    con_list = new_z + new_one
    return con_list

print(int_a(input_arr))
        