print("Welcome to the word puzzle game!\nYou have to guess what the word is and we will give you some hints if you try.\nFor example: If the word you write has some common letters with the word to be guessed and they are in the same place, it will show in UPPERCASE, if the word matches with one of the word to be guessed but is not in the same position it will show in lowercase. If there is no match it won't show anything but underscores '__'\nHave fun!" )
#Word to guess
word = "bear"
#Create a list to save the word letter by letter
listWord = []
guess = len(word)
#Counter of attempts to guess word
attempts = 0
#Introduction of game
print(f"Hint: it is an animal", end="")
#Show underscore according the size of the word
for i in range(guess):
    if i != guess:
        print(f" _", end="")
        
#While loop to keep the game until guess
user_guess = ""
while user_guess != word:
    #Prompt user to guess
    user_guess = input("\nWhat is your guess? ")
    #If guess, finish the game
    if(user_guess == word):
        break
    #Create two list to save the input user letter by letter
    #Create a list to compare the input user against the word to guess
    listInput = []
    listResult = []
    #Create a counter to iterate
    x=0
    
    #for loop to save the input
    for l in word :
        if(l in user_guess):
            listWord.append((l + " "))
        else:
            listWord.append("_ ")
    #If the input size is equal to the word to guess
    if len(user_guess) == guess:
        #Save the input user
        for letter in user_guess:
            if letter in word:
                listInput.append((letter + " "))
            else:
                listInput.append("_ ")
            #Compare the input against the word and if its matches transform to upper case
            if listInput[x] == listWord[x]:
                listResult.append(listInput[x].upper())
            else:
                listResult.append(listInput[x])
             #incremente iteration
            x+= 1
        #Show the result of comparasion
        for result in listResult:
            print(result,end="")
        #Incremente the variable attempts until guees the whole word
        attempts += 1
    #If input size is different to word size
    else:
        print("Sorry, the guess must have the same number of letters as the secret word.")
#END GAME
print("Congratulations! You guessed it!")
print(f"It took you {attempts} guesses.")
    



