myFile=open("producyDetauks.txt","a")
pID=input("Enter product ID (Enter done to end): ")
while (pID!="done"):
    pName=("Enter product Name: ")
    price = input("Enter price: ")
    myFile.write(pID+","+pName+","+price+"\n")
    pID=input("Enter product ID (Enter done to end): ")
myFile.close()