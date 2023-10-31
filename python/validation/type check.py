num=input("Enter a number: ")
while (1):
    try:
        #convert the input value to integer
        int(num)
        break
    except:
        #this statement is executed when num is not an integer 
        num=input("Please enter a valid integer: ")
        #program continues 
print("num=",num)