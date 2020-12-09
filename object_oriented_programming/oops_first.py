#class classname
class Person:
    #initializing attributes
    def set_person(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_person(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
#refrenece_name=class()
obj=Person()
obj.set_person("ajay",25,"gender")
obj.print_person()

obj1=Person()
obj1.set_person("sanjay",35,"gender")
obj1.print_person()
