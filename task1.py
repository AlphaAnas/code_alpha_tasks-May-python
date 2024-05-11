import random

def hangman(word_lst, max_attempts=10):
    index = random.randint(0, len(word_lst)-1)
    answer = list(word_lst[index])

    guessed_chars = set()

    attempts_left = max_attempts

    while attempts_left > 0:
       
        for ch in answer:
            if ch in guessed_chars:
                print(ch,end=" ")
            else:
                print("_", end=" ")
        print()
        if all(ch in guessed_chars for ch in answer):
            print("You win!")
            return

        # Get user input
        guess = input("Enter a character: ").lower()

        # Check input validity
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_chars:
            print("You have already guessed that letter.")
            continue

        # Add the guessed letter to the set
        guessed_chars.add(guess)

        # Check if the guess is correct
        if guess in answer:
            print("Correct guess!")
        else:
            print("Wrong guess")
            attempts_left -= 1

    print(f"The word was {''.join(answer)}")
    print("You lose!")

word_lst = ["table", "chair"]
hangman(word_lst)
