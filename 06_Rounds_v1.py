# Set balance for testing

balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    # Show an increase in number of rounds played
    rounds_played += 1

    print()
    print("*** Round #{}***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance <1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

    
print()
print("Final balance", balance)