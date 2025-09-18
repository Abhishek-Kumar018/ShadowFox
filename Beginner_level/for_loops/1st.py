import random

rolls = int(input("How many times do you want to roll the die? "))
six_count = 0
one_count = 0
two_sixes_in_a_row = 0

previous_roll = None

for _ in range(rolls):
    roll = random.randint(1, 6)
    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1
    if previous_roll == 6 and roll == 6:
        two_sixes_in_a_row += 1
    previous_roll = roll

print(f"\nYou rolled the die {rolls} times.")
print(f"Number of 6s rolled: {six_count}")
print(f"Number of 1s rolled: {one_count}")
print(f"Number of times two 6s appeared in a row: {two_sixes_in_a_row}")
