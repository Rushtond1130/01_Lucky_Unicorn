# ask the user if they ahve played the game before or not
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if tey have pkayed the game before
    show_instructions = input("Have you played this game before? ").lower()
    # If the user says yes, the program continues. If no, show the instructions. If invalid output an error

    if show_instructions == "yes":
        print("Program continues")

    elif show_instructions == "y":
        print("program continues")
    
    elif show_instructions == "no":
        print("Display instructions")

    elif show_instructions == "n":
        print("Display instructions")

    else:
        print("Please answer yes / no")

    print("You chose {}".format(show_instructions))