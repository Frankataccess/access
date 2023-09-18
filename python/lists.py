names = ["John","Bob","Mosh","Sam","Mary"]
names[0]= "Jon"
print(names[0:3])
print(names)

#list methods
numbers = [1,2,3,4,5]
numbers.insert(0,-1)
numbers.remove(3)
print(numbers)
print(-1 in numbers)
print(len(numbers))

#tuples

numbers = (1,2,3,3)
print(numbers.count(3))
