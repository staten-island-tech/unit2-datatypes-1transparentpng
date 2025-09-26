import math

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
            print(f"{haveFriend}, {haveMoney}, {isBanned}, False [!3!]") # I do not have a friend nor the money to go to the theater
        print("-=" * 25)
        print(" ")




# boolean value
movie = True
Homework = False

# integers and floats
integer = 67 # whole numbers only
ee = float(67.02) # numbers with decimals allowed
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
def c2(num):
    if num % 2 == 0:
        print(f"{num} is EVEN!")
    else:
        print(f"{num} is ODD!")
c2(53)


# Challenge 3
bill = int(55)
def c3():
    tipTypes = ["Bad", "Fine", "Good", "Great"]
    tipInput = input("Please, tip us based on how good our service was! Was it Bad, Fine, Good, or Great?")
    tipPercent = 0
    if tipInput in tipTypes:
        if tipInput == "Bad":
            print("We're sorry your service wasnt as good as you anticipated! We hope to improve our service based on your thoughts.")
        elif tipInput == "Fine":
            tipPercent = .15
            print("Thank you for selecting Fine, and giving us a 15% Tip!")
        elif tipInput == "Good":
            tipPercent = .2
            print("Thank you for selecting Good, and giving us a 20% Tip!")
        elif tipInput == "Great":
            tipPercent = .25
            print("Thank you for selecting Great, and giving us a 25% Tip!")
    else:
        print("Invalid answer! Please select from the following: Bad, Fine, Good, Great")
        c3()
    total = (bill * tipPercent) + bill
    print("-=" * 10)
    print("RECEIPT")
    print("-=" * 10)
    print(f"Sub-total: ${bill}")
    print(f"Tip: {tipPercent}%")
    print(" ")
    print(f"Total: ${total}")

# challenge 4
number = int(20)
def c4():
    factors = []
    for i in range(1, number + 1): # loop starts from 1 rather than 0, which would cause zerodivisionerror
        if number % i == 0:
            factors.append(i)
    print(factors)

# challenge 5
number1 = int(55)
number2 = int(30)
def c5SIMPLE():
    print(math.gcd(number1, number2)) # uses the math import's gcd feature, which is really simple

def c5REALLYHARDFORSOMEREASON():
    commonfactors = [] # creates a list which all the found common factors would be put in
    for divisor in range(number1, 0, -1): # loop that counts down from number 1 all the way to 0. number1 is starting number, 0 is end number, -1 is decrement
        if number1 % divisor == 0 and number2 % divisor == 0:
            print(divisor)
            commonfactors.append(divisor) # adds the divisor to the common factors lit if it has a remainder of 0
    print(f"The GCF IS:")
    print(max(commonfactors)) # takes the highest common factor found, AKA the GCF from the list




