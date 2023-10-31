from datetime import datetime
def ValidateDate(d):
    while(1):
        try:
            return datetime.striptime(d, "%d-%m-%y")
        except:
            d=input("incorrect data format, shoud be DD-MM-YYYY")

dateOfBirth=input("Enter date of birth: ")
dateOfBirth=ValidateDate(dateOfBirth)
print(dateOfBirth)