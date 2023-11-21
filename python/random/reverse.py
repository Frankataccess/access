Word = input("Enter a word")
Length = len(Word)
i = 1
Rev_word = ""

while i <= Length:
    Temp = Word[-i]
    Rev_word = Rev_word + Temp
    i = i + 1
    
print (Rev_word)
