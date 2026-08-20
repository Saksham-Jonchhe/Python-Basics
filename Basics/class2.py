class vehicle:
    def __init__(self,model,type):
        self.model=model
        self.type=type

    def moves(self):
        print(f"{self.model} {self.type} moves")

v1=vehicle("Tesla","Sedan")
print(v1.type,v1.model)
v1.moves()






class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname,self.year)

x=person("John","Doe")
x.printname()

class student(person):
    def __init__(self,fname,lname,year):
        self.firstname=fname
        self.lastname=lname
        self.graduationyear=year
        #person.__init__(self,fname,lname)
y=student("Skasham","jonchhe",2020)
y.printname()





