myFile = open("BookDetails.txt","r")
for row in myFile:
    field=row.split(",")
    ISBN = field[0]
    title = field[1]
    author = field[2]
    price = float(field[6])
    if (price<15):
        print(ISBN,title,author,price)
myFile.close()

myFile=open("BookDetails.txt","r")
print(myFile.read(3))
print(myFile.read(12))
print(myFile.read())