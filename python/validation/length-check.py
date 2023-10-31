password=str(input("Enter password: "))

while len(password)<8:
    password = str(input("Please enter a password with at least 8 characters: "))
    #continue program
print("password=",password)