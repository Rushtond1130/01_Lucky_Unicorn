# Ask the user if they have played the game before or not.
show_instructions = input ("Have you played this game before? ").lower()

# If the user says yes, the program continues. If the user says no, the instructions are displayed

if show_instructions == "yes":
    print("program continues")


elif show_instructions == "no":
    print("Display instructions")

# Show an error if the question is not properly answered

else:
    print("Please answer yes / no")
    