import random
words = {
    "python": "A popular programming language",
    "apple": "A type of fruit",
    "guitar": "A musical instrument",
    "elephant": "The largest land animal",
    "mountain": "A natural elevation of the earth's surface",
    "bat": "Used by a player to hit the ball in cricket",
    "wicket": "Three stumps together in cricket",
    "bowler": "Person who delivers the ball in cricket",
    "batsman": "Player who tries to score runs",
    "innings": "One team's turn to bat",
    "gloowall": "A wall for protection in Free Fire",
    "grenade": "Throwable weapon causing explosion",
    "booyah": "Victory shout in Free Fire",
    "medkit": "Used to restore health",
    "loot": "Items collected during the game",
}

def hangman():
    word, hint = random.choice(list(words.items()))
    guessed = []
    wrong = 0
    max_wrong = 6
    print("Hey! Welcome to Hangman!")
    print("Hint:", hint)
    while wrong < max_wrong:
        display = " ".join([l if l in guessed else "_" for l in word])
        print("\nWord:", display)
        if "_" not in display:
            print("Congrats! You guessed the correct word:", word)
            break
        guess_input = input("Guess a letter: ").lower()
        if not guess_input.isalpha():
            print("Enter only letters.")
            continue
        if len(guess_input) > 1 and guess_input == word:
            print(f"You have guessed the correct word: {word}")
            break
        elif len(guess_input) > 1 and guess_input != word:
            wrong_guess = False
            for guess in guess_input:
                if guess not in guessed:
                    guessed.append(guess)
                if guess not in word:
                    wrong_guess = True
                    wrong += 1
            if wrong_guess:
                print("You have entered wrong alphabets.")
                print(f"Now you have {max_wrong - wrong} guesses left.")
            else:
                print("You have entered the correct alphabets.")
            continue
        guess = guess_input
        if guess in guessed:
            print("You already tried that letter!")
            continue
        guessed.append(guess)
        if guess in word:
            print(f"You have guessed the correct alphabet: {guess}")
        else:
            print(f"You have guessed the wrong alphabet: {guess}")
            wrong += 1
            print(f"Now you have {max_wrong - wrong} guesses left.")
    else:
        print("Game Over! The word was:", word)

hangman()
