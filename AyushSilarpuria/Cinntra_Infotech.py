# Q.1: Remove duplicate entries.
list1 = [
    {
        "Name": "Iphone",
        "Price": "100",
        "Weight": 1
    },
    {
        "Name": "Android",
        "Price": "300",
        "Weight": 1
    },
    {
        "Name": "Mac",
        "Price": "400",
        "Weight": 1
    },
    {
        "Name": "Mac",
        "Price": "400",
        "Weight": 1
    }
]

def duplicates(arrayy):

    new_list = []
    for item in arrayy:
        if item not in new_list:
            new_list.append(item)
    return new_list
print(duplicates(list1))


# Q.2: Remove duplicate words fully and print remaining letters:

str = "google"

def non_rep(st):
    
    str1 = ' '
    for i in range(len(st)):
        if st[i] != st[i+1:] or i == len(st):
            str1 += st[i]
    return str1
print(non_rep(str))
