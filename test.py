#TEST
sentence = input("Type a sentence, and i'll give you the word count.")
y = sentence.split( )

wrdcount = 0
for i in y:
    wrdcount = wrdcount + 1
print(wrdcount)