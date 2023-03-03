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
    print("*** How to Play ***")
    print()
    print("The rules go here")
    print()
    return ""

# Main routine 
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program continues")



having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun".format(having_fun)) 