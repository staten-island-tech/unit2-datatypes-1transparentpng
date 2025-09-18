# test
haveFriend = True
haveMoney = False
def truthtabletest():
    print("Have Friend? | Have Money? | Go Movies?")
    print("-=" * 10)
    if haveFriend and haveMoney:
        print("True, True, True")
    elif haveFriend == False and haveMoney == True:
        print (f"")
# boolean value
movie = True
Homework = True

if Homework and movie == True:
    print("I'd like to go to the movies, but I must do my homework!")
elif Homework == True:
    print("Doing homework!")
elif movie == True:
    print("Heading to the movies!")
else:
    print("Got nothing to do..")

# integers and floats
integer = 67 # whole numbers only
float = float(67.02) # numbers with decimals allowed
# floats can have decimals, integers cant



# Challenge 1 (make a script that counts the words of a sentence)

sentence = input("Type a sentence, and i'll give you the word count.")
y = sentence.split( ) # Splits the string into a list of words. Since were splitting all other letters from a space, it essentially creates a list of words.
wrdcount = 0
for i in y: # For every word in the list, the variable wrdcount increases by 1 from 0.
    wrdcount = wrdcount + 1 
print(f"There are {wrdcount} words in that!") # prints the total amount of words :D


# Challenge 2
