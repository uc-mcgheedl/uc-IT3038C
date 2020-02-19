
#User prompt and input
word = input("Enter a word: ")

# declared vowels and consonants variables
cons = 0
vow  = 0


for v in word:
    if(v == "a" or v == "e" or v == "A" or v == "E" or v == "i" or v == "o" or v == "I" or v == "O" or v == "u" or v == "U"):
        vow = vow + 1
    else:
        cons = cons + 1

#prints out user's word information
print("The total amount of letters is %s, the # of vowels is %d and the # of consonants is %a" %(len(word), vow, cons))        


