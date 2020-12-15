class bank:
    #static variables
    #keyword used for effiency memory utilization
    #we can access the static varibale by class name
    bank_name="sbk"
    @staticmethod
    def utility_method():
        print("utility method")


    # @classmethod
    # def change_bank_name(cls):
    #     # cls.bank_name("sbi")

    def create_account(self,accno,person_name,balance,bank_name):
        self.accno=accno
        self.person_name=person_name
        self.balance=balance
        self.bank_name=bank_name

    def deposit(self,amount):
        self.balance+=amount
        print("your account",self.accno, "has been credited with amount", amount, "avaliable bal", self.balance)


    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffient bal in your account", self.accno, "balance",self.balance)
        else:
            self.balance-= amount
            print("your account", self.accno, "has been dedited with amount", amount, "avaliable bal", self.balance)

    # def balance_enq(self):

obj=bank()
obj.create_account(1001,"test",500,"sbl")
obj.deposit(500)
bank.utility_method()
#bank.change_bank_name()