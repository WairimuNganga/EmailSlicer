Email_id = input("Enter your email id").strip()

username = Email_id[:Email_id.index('@')]

domain = Email_id[Email_id.index('@')+1:]

print(f"Your username {username} and your domain name is {domain}")