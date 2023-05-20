print("Welcome to the word puzzle game!\nYou have to guess what the word is and we will give you some hints if you try.\nFor example: If the word you write has some common letters with the word to be guessed and they are in the same place, it will show in UPPERCASE, if the word matches with one of the word to be guessed but is not in the same position it will show in lowercase. If there is no match it won't show anything but underscores '__'\nHave fun!" )

word = "bear"
listWord = []
guess = len(word)
attempts = 0
print(f"Hint: it is an animal", end="")
for i in range(guess):
    if i != guess:
        print(f" _", end="")
        
user_guess = ""
while user_guess != word:
    user_guess = input("\nWhat is your guess? ")
    
    if(user_guess == word):
        break
    listInput = []
    listResult = []
    x=0
    for l in word :
        if(l in user_guess):
            listWord.append((l + " "))
        else:
            listWord.append("_ ")
    
    if len(user_guess) == guess:
        for letter in user_guess:
            if letter in word:
                listInput.append((letter + " "))
            else:
                listInput.append("_ ")
            
            if listInput[x] == listWord[x]:
                listResult.append(listInput[x].upper())
            else:
                listResult.append(listInput[x])
            x+= 1
        for result in listResult:
            print(result,end="")
        attempts += 1
    
    else:
        print("Sorry, the guess must have the same number of letters as the secret word.")
print("Congratulations! You guessed it!")
print(f"It took you {attempts} guesses.")
    



