import random

# Set balance for testing

balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    # Show an increase in number of rounds played
    rounds_played += 1

    print()
    print("***Round #{}***".format(rounds_played))

    chosen_num = random.randint(1,100)

    # Balance adjustment

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance   -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "horse"

        else:
            chosen = "zebra"
        
        balance -= 0.5
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    print()

    if balance <1:
        play_again = "xxx"
        print("Sorry you have run out of money")

    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")


print()
print("Final balance", balance)