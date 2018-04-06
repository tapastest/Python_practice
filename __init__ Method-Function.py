class Account():

    def __init__(self, Ac_name=''):
        self.name = Ac_name
        
    def Account_details(self):
        return self.name

New_obj = Account("tapas")
print(New_obj.Account_details())
    
