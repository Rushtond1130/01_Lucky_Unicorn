# ask the user if they ahve played the game before or not
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if tey have pkayed the game before
    show_instructions = input("Have you played this game before? ").lower()
    # If the user says yes, the program continues. If no, show the instructions. If invalid output an error

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "Yes"
        print("Program continues")
        print()

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "No"
        print("Display instructions")
        print()


    else:
        print("Please answer yes / no")
        print()

    print("You chose {}".format(show_instructions))