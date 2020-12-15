class Parent:
    def phone(self):
        print("have nokia")
        #self.__laptop()
    def __laptop(self):#private method
        print("i have lap")
class Child(Parent):
    # pass
    def bike(self):
        print("i have duke")
    def changebikenum(self,num):
        self.bike_num=num
    def printnum(self):
        print(self.bike_num)
ch=Child()
ch.phone()
ch.bike()
ch.changebikenum(800)
ch.printnum()