import random
import words


def get_wordle_guess(attempt):
    while True:
        guess = input("\nPlease enter your guess - attempt " + str(attempt) + ": ")
        print("")
        if len(guess) != 5:
            print("Five letter words only please.")
        elif guess not in words.WORD_LIST:
            print("Not in word list!")
        else: break
    
    return guess



print("\n\n---------------------------------\n--         My Wordle!          --\n-- Guess the Wordle in 6 tries --\n---------------------------------\n")

opt = input("Would you like to play My Wordle [y|n]? ")
while opt != "y" and opt != "n":
    opt = input("Would you like to play My Wordle [y|n]? ")

if opt == "n":
    print("\n\nNo worries... another time perhaps... :)")
else:
    finished = False
    solvedcount = 0
    unsolvedcount = 0

    while not finished:
        wordle = random.choice(words.WORD_LIST)

        print("\nWordle is:", wordle)

        print("\n-------------\n| - - - - - |")

        correct = []
        used = []
        turn  = 0
        solved = False

        while turn < 6 and not solved:
            turn += 1
            guess = get_wordle_guess(turn)
            pattern = []
            count1 = 0
            count2 = 0

            for index in range(5):
                if guess[index] == wordle[index]:
                    pattern.append('^')
                else: pattern.append('_')

            for index in range(5):
                if guess[index] not in wordle:
                    pattern[index] = '-'
                    if guess[index] not in correct and guess[index] not in used:
                        used.append(guess[index])
    
                elif guess[index] == wordle[index]:
                    pattern[index] = '^'
                    if guess[index] not in correct:
                        correct.append(guess[index])
                    if guess[index] in used:
                        used.remove(guess[index])
                    count1 += 1

                else:
                    countw = 0
                    countp = 0
                    for i in range(5):
                        if wordle[i] == guess[index]:
                            countw += 1
                        if guess[i] == guess[index] and (pattern[i] == '*' or pattern[i] == '^'):
                            countp += 1
                    
                    if countp < countw:
                        pattern[index] = '*'
                        count2 += 1
                    else:
                        pattern[index] = '-'

                    if guess[index] not in correct and guess[index] not in used:
                        used.append(guess[index])
            
            
            print("-------------\n| ", end="")
            for char in guess:
                print(char, end=" ")
            print("|\n| ", end="")
            for char in pattern:
                print(char, end=" ")
            print("|\n|\n| Correct spot(^): " + str(count1))
            print("| Wrong spot(*):   " + str(count2))
            print("|\n| Correct letters:", end=" ")
            for letter in correct:
                print(letter, end=" ")
            print("\n| Used letters:", end=" ")
            for letter in used:
                print(letter, end=" ")
            print("")

            if wordle == guess:
                if turn == 6:
                    print("Phew!", end=" ")
                print("\n\nSolved in " + str(turn) + " tries! Well done!\n")
                solved = True
                solvedcount += 1

        if not solved:
            print("\n\nOh no! Better luck next time!\n\nThe wordle was: " + wordle + "\n")
            unsolvedcount += 1

        opt = input("\nWould you like to play again [y|n]? ")
        while opt != "y" and opt != "n":
            opt = input("Would you like to play again [y|n]? ")

        if opt == "n":
            finished = True

    print("\n\nMy Wordle Summary\n=================\n")
    print("You played " + str(solvedcount + unsolvedcount) + " games:")
    print("  |--> Number of wordles solved:   " + str(solvedcount))
    print("  |--> Number of wordles unsolved: " + str(unsolvedcount))
    
    print("\n\nThanks for playing!")