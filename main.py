from textproto import Form

#instantialising object
user1 = Form("Gramos", "Hoxha", "grombog", "D&G")

user1.save_data()
print(user1.retreive_data())