for i in range(1,20):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i,"Fizz-Buzz")
    elif i % 3 == 0 :
        print(i, "Fizz")
    elif i %  5 == 0 :
         print(i,"Buzz")
    else:
        print(i)


print("The End")
