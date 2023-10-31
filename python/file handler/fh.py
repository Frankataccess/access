myFile = open("BookDetails.txt","r")

for row in myFile:
    field=row.split(",")

    print(field[0],field[1],field[2],field[3],field[4],field[5],field[6],end="")

myFile.close()