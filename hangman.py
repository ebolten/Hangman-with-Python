from random import randint

words = ["clock", "blocks", "chess", "austria"]
allowed_wrong_guesses = 5

# print welcome message
def welcome_user():
    print("Welcome to Hangman!")

# get word from game array
def get_game_word(words):
    return words[randint(0, len(words)-1)]

# get the user's letter guess
def get_user_guess():
    letter = input("Guess a Letter: ")
    if (len(letter) > 1):
        print("Please enter one letter.")
        return get_user_guess()
    return letter

# get the user's letter guess
def get_play_again():
    play_again = input("Would you like to play again (y or n)?: ")
    if (play_again != "y") and (play_again != "n"):
        print("Please enter y or n.")
        return get_play_again()
    return play_again

# begin the game
def begin_game(words, allowed_wrong_guesses):
    welcome_user()
    game_word = get_game_word(words)
    guess_arr = []
    wrong_guesses = 0
    
    # generate the words guesses array
    # will be full of underscores for non-guessed values
    for i in range(len(game_word)):
        guess_arr.append("_")
    
    # allow user to continue guessing until they've guessed the word or ran out of guesses
    while wrong_guesses < allowed_wrong_guesses:
        user_guess = get_user_guess()
        if user_guess in game_word:
            for i in range(len(game_word)):
                if game_word[i] == user_guess:
                    guess_arr[i] = user_guess
            print("You've guessed a letter!")
            print(guess_arr)
            if not "_" in guess_arr:
                print("You've guessed the word! The word was {}.".format(game_word))
                break
        else:
            wrong_guesses += 1
            print("That letter is not in the word! You have {} wrong guesses left.".format(allowed_wrong_guesses - wrong_guesses))
    
    # prompt user to select if they'd like to play again or quit
    play_again = get_play_again()
    if play_again == "y":
        return begin_game(words, allowed_wrong_guesses)
    else:
        print("Thank you for playing!")
        return

begin_game(words, allowed_wrong_guesses)