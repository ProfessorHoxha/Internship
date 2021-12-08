from textproto import Form

#instantialising object
user1 = Form("Gramos", "Hoxha", "grombog", "D&G", "https://www.google.com/search?q=")
user2 = Form("Mark", "Johnson", "Markiplier", "TRMG", "https://www.google.com/search?q=")

user1.save_data()
user2.save_data()
print(user1.retreive_data())

#print(user1.all_links())
#print(user2.all_links())

#https://www.google.com/search?q=Mark+Johnson+trmg

#Prefix + first_name + "+" + last_name "+" organisation_name

'''print(user1.name_and_organisation())
print(user2.name_and_organisation())
print(user1.facebook())
print(user2.facebook())
print(user1.linkedin())
print(user2.linkedin())
print(user1.organisation_and_filetype())
print(user2.organisation_and_filetype())'''

#facebook suffix = Site%3Afacebook.com
#Linkedin suffix = Site%3Alinkedin.com
#Filetype:XLSX suffix = filetype%3Axlsx

#https://www.google.com/search?q=Gramos+Hoxha+Site%3Alinkedin.com
