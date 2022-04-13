Email_id = input("Enter your email id").strip()

Username = Email_id[:Email_id.index('@')]

Domain = Email_id[Email_id.index('@')+1:]

print(f"Your username {Username} and your domain name is {Domain}")