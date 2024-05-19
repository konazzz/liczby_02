

guessed = False

print("""
Think of a number from 1 to 1000 
and i will guess it in less than 10 attempts
""")

min_1 = 0
max_1 = 1000

while guessed is not True:
    guess = int((max_1 - min_1) / 2) + min_1
    print(f"My guess is: {guess}")
    correct_responses = ('too big', 'too small', 'you guessed')

    response = input("pick 'too big', 'too small' or 'you guessed' ")
    try:
        if response not in correct_responses:
            raise ValueError
    except ValueError:
        print("incorrect response")
        continue

    if response == "you guessed":
        print("i won!")
        guessed = True
    elif response == "too big" and max_1 >= guess:
        max_1 = guess
        continue
    elif response == "too small" and min_1 <= guess:
        min_1 = guess
        continue
    else:
        print("don't cheat")
        continue

# i still need to polish the "dont cheat" part
