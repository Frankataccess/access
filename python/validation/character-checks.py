password=input("Enter password: ")
valid=False
while not valid:
    for i in range(len(password)):
        if (ord(password[i]) in range(48,50)):
            valid=True
    if (not valid):
        password = input("Password must have at least one number: ")
print("Password is valid")