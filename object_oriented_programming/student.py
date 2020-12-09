#create a class student consist of attributes rol,name,course,total
#must have methods for setting and printing
class Student:
    def set_student(self,rol,name,course,total):
        #instance variables,set.rol,self.name,..)
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def print_person(self):
        print("rol",self.rol)
        print("name",self.name)
        print("course",self.course)
        print("total",self.total)
obj=Student()
obj.set_student(4,"dhanya","mca",700)
obj.print_person()