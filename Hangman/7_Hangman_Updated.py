import random

from Hangman_updated_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_updated_art import logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"you have already guessed{guess} in {display}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if the user is wrong.
    if guess not in chosen_word:
        print(f"You have guessed {guess} that is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if the user has all the letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_updated_art import stages
    print(stages[lives])
