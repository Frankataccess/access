numbers = (67, 15, 70, 346, 4)

biggest = numbers[0]
second_biggest = numbers[0]

for i in range(1, len(numbers)):
    if biggest < numbers[i]:
        second_biggest = biggest
        biggest = numbers[i]
    elif numbers[i] < biggest and numbers[i] > second_biggest:
        second_biggest = numbers[i]

print("Biggest:", biggest)
print("Second Biggest:", second_biggest)