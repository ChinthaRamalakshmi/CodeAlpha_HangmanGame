import random

words = ["python", "apple", "house", "water", "music"]

word = random.choice(words)

guessed = ["_"] * len(word)

chances = 6

print("Welcome to Hangman Game!")

while chances > 0 and "_" in guessed:

    print("\nWord:", " ".join(guessed))

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        chances -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", chances)

if "_" not in guessed:
    print("\nCongratulations! You Win!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)