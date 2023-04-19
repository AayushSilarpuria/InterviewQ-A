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
