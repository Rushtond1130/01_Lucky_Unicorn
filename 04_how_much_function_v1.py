# Functions
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
how_much = num_check("How much would you like to play with? $", 0, 10)

# Tell the user what they are spending
print("You will be spending ${}".format(how_much))