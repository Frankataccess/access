import pandas as pd

#dataframe
print("Dataframe")
mydataset = {
    'cars' : ["BMW","Volvo","Ford"],
    'passigns': [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

 
#series 
print("\nSeries")
a = [1,7,2]

myseries = pd.Series(a, index = ["x","y","z"])

print(myseries)

#changed series 
print("\nSeries 2")
sales=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sales)

print("\nSeries 3")
calories ={"day1":420,"day2":380,"day3":390}
cal = pd.Series(calories, index = ["day1","day2"])
print(cal)

print("\n Dataframe 2\n")

data = {
    "Calories":[420, 380,390],
    "Duration":[50,40,45]
}

df = pd.DataFrame(data)
print(df)
print("\n loc[0]")
print(df.loc[0])
print("\n loc[[0,1]]")
print(df.loc[[0,1]])

#named index 
print("\n named index")
