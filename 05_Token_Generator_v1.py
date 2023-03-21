import random

# Main routine

tokens = ["unicorn", "horse", "zebra", "donkey"]

# Test loop
for item in range (0,20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')
