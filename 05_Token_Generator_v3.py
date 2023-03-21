import random

# Main routine
# Tweaked token ammounts 
# Unicorn, Horse, Zebra, Donkey with a ratio of 1:2:4:3
tokens = ["unicorn", "horse", "horse", "zebra", "zebra", "zebra", "zebra", "donkey", "donkey"]
STARTING_BALANCE = 100 

balance = STARTING_BALANCE

# Test loop

for item in range(0,100):
    chosen = random.choice(tokens)

    # Balance adjustment
    if chosen == "unicorn":
        balance += 4

    elif chosen == "donkey":
        balance -= 1

    else:
        balance -= 0.5


print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
