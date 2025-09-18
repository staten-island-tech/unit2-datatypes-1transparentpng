# test
haveFriend = True
haveMoney = True
isBanned = True
def truthtabletest():
    print(" ")
    print("Have Friend? | Have Money? | Is Banned? | Go Movies?")
    print("-=" * 25)
    if haveFriend or haveMoney:
        if not isBanned:
            print(f"{haveFriend}, {haveMoney}, {isBanned}, True [!1!]") # I have a friend OR the money to go to the theater
        elif isBanned:
            print(f"{haveFriend}, {haveMoney}, {isBanned}, False [!2!]") # I am banned from the theater
        elif not haveFriend or haveMoney:
            print(f"{haveFriend}, {haveMoney}, {isBanned}, False [!3!]") # I do not have a friend or the money to go to the theater
        print("-=" * 25)
        print(" ")
truthtabletest()





# boolean value
movie = True
Homework = True

def yadayada():
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

def c1():
    sentence = input("Type a sentence, and i'll give you the word count.")
    y = sentence.split( ) # Splits the string into a list of words. Since were splitting all other letters from a space, it essentially creates a list of words.
    wrdcount = 0
    for i in y: # For every word in the list, the variable wrdcount increases by 1 from 0.
        wrdcount = wrdcount + 1 
    print(f"There are {wrdcount} words in that!") # prints the total amount of words :D


# Challenge 2
