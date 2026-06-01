import random

words = ["python", "laptop", "mobile", "coding", "gaming"]

word = random.choice(words)
guessed = ["_"] * len(word)

attempts = 6

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)