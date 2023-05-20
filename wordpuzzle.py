#print("Welcome to the word puzzle game!\nYou have to guess what the word is and we will give you some hints if you try.\nFor example: If the word you write has some common letters with the word to be guessed and they are in the same place, it will show in UPPERCASE, if the word matches with one of the word to be guessed but is not in the same position it will show in lowercase. If there is no match it won't show anything but underscores '__'\nHave fun!" )

#HOLA VANEGAS
word = "bear"
guess = len(word)
print(f"Hint: it is an animal", end="")
for i in range(guess):
    if i != guess:
        print(f" _", end="")

user_guess = input("\nWhat is your guess? ")
first_letter = user_guess[0]
second_letter = user_guess[1]
third_letter = user_guess[2]
fourth_letter = user_guess[3]
# fifth_letter = user_guess[4]
# sixth_letter = user_guess[5]
# seventh_letter = user_guess[6]
# eighth_letter = user_guess[7]
# nineth_letter = user_guess[8]
# tenth_letter = user_guess[9]
# eleventh_letter = user_guess[10]

for i in word:
    if i == first_letter.lower():
        print(f"{i}", end="")
    
    # elif i != first_letter.lower():
    #     print(" _", end="")

    # elif i == second_letter.lower():
    #     print(f"{i}", end="")
    
    # elif i != second_letter.lower():
    #     print(" _", end="")

    # elif i == third_letter.lower():
    #     print(f"{i}", end="")
    
    # elif i != third_letter.lower():
    #     print(" _", end="")

    # elif i == fourth_letter.lower():
    #     print(f"{i}", end="")
    
    # elif i != fourth_letter.lower():
    #     print(" _", end="")

for i in word:
    if i == second_letter.lower():
        print(f"{i}", end="")
        if i!= second_letter.lower():
            print(" _")

for i in word:
    if i == third_letter.lower():
        print(f"{i}", end="")
        if i!= third_letter.lower():
            print(" _")

for i in word:
    if i == fourth_letter.lower():
        print(f"{i}", end="")
        if i!= fourth_letter.lower():
            print(" _")
