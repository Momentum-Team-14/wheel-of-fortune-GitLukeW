import random


def play_game():
    filepath = open("test-word.txt", "r")
    open_file = filepath.read()
    print(open_file)

    words = open_file.split()
    counter = 8

    random_word = random.choice(words)
    print(random_word)

    blank = [" __ "] * len(random_word)

    print(blank)

    random_word_picked = random_word

    letters = list(random_word_picked)
    print(letters)

    # guess = input("pick a letter:")

    user_letters(blank, letters, counter)


def user_letters(blank, letters, counter):
    guess = input("pick a letter:")
    if guess in letters:
        for i in range(len(letters)):
            if guess == letters[i]:
                blank[i] = letters[i]
        print(blank)
        if " __ " not in blank:
            print("You Win!")
            exit()
        if counter > 0:
            user_letters(blank, letters, counter)

    else:
        counter -= 1
        if counter > 0:
            user_letters(blank, letters, counter)
        else:
            print("Game Over")
            exit()


# def guess_counter():
if __name__ == "__main__":
    play_game()
