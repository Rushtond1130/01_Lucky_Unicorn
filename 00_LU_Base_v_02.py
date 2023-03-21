import random

# Functions 
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response

        else:
            print("Please answer yes / no")

def instructions():
    # Is there a different way to code this instructions function? Having this many print statements feels wrong.
    
    print()
    print("Choose a starting ammount (minimum $1, maximum $10)")
    print("Then press <Enter> to play. You will get either a horse, a zebra, a donky or a unicorn")
    print("It costs $1 per round.  Depending on your prize you might win some of the money back")
    print()
    print("Here's the payout ammounts...")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Horse: $0.50 (balance decreces by $0.50")
    print("Zebra: $0.50 (balance decreces by $0.50")
    print("Donkey: $0.00 (balance decreces by $1")
    print()
    print("Can you aboid the donkeys, get the unicorns and walk home with the money???")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead of pressing <Enter>")
    return ""
 
def num_check(question, low, high):

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask question
            response = int(input(question))

            # Show user the ammount input
            if low < response <= high:
                return response

            # output error when response is invalid
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):
    
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine 

statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

# Ask the user if they have played before

played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    print()
    statement_generator("How to play", "*")
    print(instructions())

statement_generator("Let's get Started", "-")

# Ask the user the amount they want to play with
how_much = num_check("How much would you like to play with? $", 0, 10)


balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()

while play_again == "":

    # Show an increase in number of rounds played
    rounds_played += 1

    print()
    statement_generator("Round #{}".format(rounds_played) ,".")
    print()

    chosen_num = random.randint(1,100)

    # Balance adjustment

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4
    
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance   -= 1


    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        else:
            chosen = "zebra"
            prize_decoration = "Z"
        
        balance -= 0.5

    outcome = "you got a {}. Your balance is " \
        "${:.2f}".format(chosen, balance)
            
    statement_generator(outcome, prize_decoration)

    if balance <1:
        play_again = "xxx"
        print()
        statement_generator("Sorry you have run out of money", "V")

        

    else:
        print()
        play_again = input("Press Enter to play again or 'xxx' to quit ")


print()
statement_generator("Results", "=")
print("Final balance $",balance)
print("Thank you for playing")

