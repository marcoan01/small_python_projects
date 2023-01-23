import random
import hangman_words
import hangman_art


def check_display(arr):
    for i in arr:
        if i == '_':
            return True
    return False
print(hangman_art.logo)
print("\n")
display = []
repeated_letters = []
lives = 6
chosen_word = random.choice(hangman_words.word_list)
for i in chosen_word:
    display.append("_")
print(display)
print("\n")
decision = check_display(display)

while decision:
    print(hangman_art.stages[lives])
    guess = input("Select a letter that you would like to guess\n ").lower()
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        lives = lives - 1
        print("Incorrect letter\n")
        print("_________________")
    if lives == 0:
        print("Game over!! :(")
        print(hangman_art.stages[lives])
        quit()
    print(display)
    decision = check_display(display)

print("You won!! You guessed all the letters!!")

