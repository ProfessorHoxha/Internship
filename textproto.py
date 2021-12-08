#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=E0001

#INPUT FORM

#Super Class
class Form(object):
    
#Constructer
    def __init__(self, first_name, last_name, username, organisation_name, prefix):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.organisation_name = organisation_name
        self.prefix = prefix
           
#data_methods
    def save_data(self):
        file = open("database.txt", "a")
        file.write(self.data_organisation())
        file.close()
        
    def retreive_data(self):
         file = open("database.txt", "r")
         retreived = file.readlines()
         newlist = []
         for line in retreived:
             newlist.append(line.strip())
         file.close()
         return newlist

    def data_organisation(self):
        details = (f"\nFirst Name:{self.first_name} Last Name:{self.last_name} Username:{self.username} Organisation Name:{self.organisation_name}\n")
        return details
        
    def describe(self):
        details = (f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}\nOrganisation Name: {self.organisation_name}")
        return details
    
#search_methods 
    def linkedin(self):
        linkedin_suffix = "Site%3Alinkedin.com"
        url = (f"{self.prefix}+{self.first_name}+{self.last_name}+{linkedin_suffix}")
        return url
        
    def facebook(self):
        facebook_suffix = "Site%3Afacebook.com"
        url = (f"{self.prefix}+{self.first_name}+{self.last_name}+{facebook_suffix}")
        return url
    
    def name_and_organisation(self):
        url = (f'{self.prefix}+"{self.first_name}+{self.last_name}"+{self.organisation_name}')
        return url
    
    def organisation_and_filetype(self):
        xlsx_suffix = "filetype%3Axlsx"
        url = (f"{self.prefix}+{self.organisation_name}+{xlsx_suffix}")
        return url
    
    def all_links(self):
        links = (f"{self.linkedin()}\n{self.facebook()}\n{self.name_and_organisation()}\n{self.organisation_and_filetype()}")
        return links
