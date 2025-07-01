
# Task 1: Hangman Game 🎯
import random

word_bank = ["music", "apple", "train", "house", "light"]
secret_word = random.choice(word_bank)
progress = ["_"] * len(secret_word)
chances = 6

print("🔠 Let's play Hangman!")

while chances > 0 and "_" in progress:
    print("Current:", " ".join(progress))
    user_guess = input("Guess a letter: ").lower()

    if user_guess in secret_word:
        for idx in range(len(secret_word)):
            if secret_word[idx] == user_guess:
                progress[idx] = user_guess
        print("Nice one! ✅")
    else:
        chances -= 1
        print(f"Oops! Wrong letter. {chances} attempts left. ❌")

if "_" not in progress:
    print(f"🎉 Congrats! You figured it out: {secret_word}")
else:
    print(f"Game over. The word was: {secret_word}")
