username=input("Enter your username:")
validate=len(username)
if len(username)>12:
    print("Invalid username")
elif not username.find(" ") == -1:
    print("invalid username")
elif not username.isalpha():
    print("invalid")
else:
    print(username)


