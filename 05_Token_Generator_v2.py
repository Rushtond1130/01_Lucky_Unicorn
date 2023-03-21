import random

# Main routine

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

# Test loop
for item in range (0,20):
    chosen = random.choice(tokens)

    # Balance adjustment
    if chosen == "unicorn":
        balance += 4

    elif chosen == "donkey":
        balance -= 1

    else:
        balance -= 0.5

    # output
    print("Token: {} , Balance: ${}".format(chosen, balance))
    