

guessed = False

print("""
Think of a number from 1 to 1000 
and i will guess it in less than 10 attempts
""")

while guessed is not True:
    min_1 = 0
    max_1 = 1000
    guess = int((max_1 - min_1) / 2) + min_1
    print(f"My guess is: {guess}")

    response = input("pick 'too big', 'too small' or 'you guessed'")

    if response == "you guessed":
        print("i won!")
        guessed = True
    elif response == "too big":
        max_1 = guess
        continue
    elif response == "too small":
        min_1 = guess
        continue

