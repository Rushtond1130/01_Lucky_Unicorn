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
    print()
    print("*** How to Play ***")
    print()
    print("The rules go here")
    print()
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

# Main routine 

# Ask the user if they have played before

played_before = yes_no("Have you played the game before? ")

if played_before == "No":
    instructions()

# Ask the user the amount they want to play with
how_much = num_check("How much would you like to play with? $", 0, 10)

print()
print("You will be spending ${}".format(how_much))