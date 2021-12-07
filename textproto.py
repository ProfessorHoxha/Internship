#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=E0001

#INPUT FORM

#Super Class
class Form(object):
    
#Constructer
    def __init__(self, first_name, last_name, username, organisation_name):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.organisation_name = organisation_name    
           
#methods
    def save_data(self):
        file = open("database.txt", "w")
        file.write(self.describe())
        file.close()
        
    def retreive_data(self):
         file = open("database.txt", "r")
         retreived = file.readlines()
         newlist = []
         for line in retreived:
             newlist.append(line.strip())      
         return newlist
        
    def describe(self):
        details = (f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}\nOrganisation Name: {self.organisation_name}")
        return details
