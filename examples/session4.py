#OOPS concepts
class Dog:
    #tricks=[]
    def __init__(self,name):
        self.name=name
        self.tricks=[]
    def add_trick(self,trick):
        self.tricks.append(trick)
d=Dog("Fido")
e=Dog("Buddy")
d.add_trick("This is my fido dog")
e.add_trick("This is my Buddy Dog")

Dog.add_trick(d,"This is my Tomy d instance ")
print e.tricks

