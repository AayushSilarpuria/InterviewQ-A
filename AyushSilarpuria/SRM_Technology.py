# Write a class student with attributes as name and id:
class Students:
     
    def __init__(self,name,id):
        self.name = name
        self.id = id
      
     
    def stud(self):
        print("My name is ",self.name) 
        print("My ID is ", self.id)

d = Students("Ayush", 21)
d.stud()



# Write code to open Excel file then read it:

with open("file1.xlsx", mode='r') as pd:
    print(pd.read())

with open("file.xlsx", mode='w') as pd:
    pd.write("Hello World!")