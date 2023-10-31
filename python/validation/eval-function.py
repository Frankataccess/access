num=input("Enter a number: ")
while type(eval(num)) is not int:
    num=input("Please enter an integer: ")
    #continue program
print("num=",num)