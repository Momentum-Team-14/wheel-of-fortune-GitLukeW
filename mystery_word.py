import random


def play_game():
    filepath = open("test-word.txt", "r")
    open_file = filepath.read()
    print("Welcome to myster_word")
    words = open_file.split()
    random_word = random.choice(words)
    blank = [" _ "] * len(random_word)
    print(blank)
    random_word_picked = random_word
    letters = list(random_word_picked)
    counter = 8
    letters_guessed = []
    user_letters(blank, letters, counter, letters_guessed)


def user_letters(blank, letters, counter, letters_guessed):
    while counter > 0:
        print("You have", counter, "guesses left")
        print("You have guessed", letters_guessed)

        guess = input("pick a letter:")
        if len(guess) > 1:
            print("Only one letter at a time please")
        elif guess in letters:
            for i in range(len(letters)):
                if guess == letters[i]:
                    blank[i] = letters[i]
                    letters_guessed.append(guess)
            print(blank)
            if " _ " not in blank:
                print("You Win! The word was", "".join(letters))
                exit()
            if counter > 0:
                user_letters(blank, letters, counter, letters_guessed)

        else:
            counter -= 1
            if counter > 0:
                letters_guessed.append(guess)
                print(blank)
                user_letters(blank, letters, counter, letters_guessed)
            else:
                print("Game Over. The correct word was", "".join(letters))
                exit()


# def guess_counter():
if __name__ == "__main__":
    play_game()
