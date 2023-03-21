import random

# Main routine

STARTING_BALANCE = 100

balance = STARTING_BALANCE

# Test loop

for item in range(0,10):
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

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
