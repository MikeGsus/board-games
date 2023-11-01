# - Game setup: The game of hangman is for two or more players, comprising a selecting player and one or more guessing players.
# - Word selection: The selecting player selects a word that the guessing players will try to guess.
### The selected word is traditionally represented as a series of underscores for each letter in the word.
### The selecting player also draws a scaffold to hold the hangman illustration.
# - Guessing: The guessing players attempt to guess the word by selecting letters one at a time.
# - Feedback: The selecting player indicates whether each guessed letter appears in the word.
### If the letter appears, then the selecting player replaces each underscore with the letter as it appears in the word.
### If the letter doesn’t appear, then the selecting player writes the letter in a list of guessed letters. Then, they draw the next piece of the hanged man. To draw the hanged man, they begin with the head, then the torso, the arms, and the legs for a total of six parts.
# - Winning conditions: The selecting player wins if the hanged man drawing is complete after six incorrect guesses, in which case the game is over. The guessing players win if they guess the word.
### If the guess is right, the game is over, and the guessing players win.
### If the guess is wrong, the game continues.

# Imports
import getpass
import os


# Variables
guessing_player = []
guessed_letters = []
failled_letters = []
is_winner = False
active_player = 0


# Functions
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def print_body(fails):
    if fails == 1:
        print("|       O")
    elif fails == 2:
        print("|       O")
        print("|       |")
    elif fails == 3:
        print("|       O")
        print("|      /|")
    elif fails == 4:
        print("|       O")
        print("|      /|\\")
    elif fails == 5:
        print("|       O")
        print("|      /|\\")
        print("|      /")
    elif fails == 6:
        print("|       O")
        print("|      /|\\")
        print("|      / \\")



def replacement_word(underscore, word):
    for i in range(len(word)):
        if word[i] in guessed_letters:
            underscore = underscore[:i] + word[i] + underscore[i+1:]
    return underscore



def board(word):
    underscore = "_" * len(word)
    fails = len(failled_letters)
    print("_________")
    print("|       |")
    print("|       |")
    print_body(fails)
    for _ in range(5 - fails): print("|")
    print("|")
    print("|")
    print(f"|{replacement_word(underscore, word)}")
    print(f"Word: {len(word)} letters")
    print(f"Used letter: {sorted([*guessed_letters, *failled_letters])}")



def asking_for_letter():
    letter_to_guess = ""
    while letter_to_guess == "":
        try:
            letter_to_guess = input("Letter: ").upper()
            assert len(letter_to_guess) == 1, "You need to enter only a letter."
            assert letter_to_guess not in [*guessed_letters, *failled_letters], "You must try with new letters."
        except AssertionError as e:
            print(e)
            letter_to_guess = ""
    return letter_to_guess



def feedback(letter_to_guess, word):
    response = letter_to_guess in word
    if response:
        guessed_letters.append(letter_to_guess)
    else:
        failled_letters.append(letter_to_guess)
    return response



def get_active_player(active_player, count_players):
    if active_player == count_players:
        active_player = 0
    else:
        active_player += 1
    return guessing_player[active_player-1]



def check_fails():
    return len(failled_letters) == 6


# Game ========================================================================
# Guessing Players
count_players = int(input("How many players are playing? "))

if count_players < 1 or count_players is None:
    print("You need at least one player to play this game.")

for i in range(count_players):
    guessing_player.append(input(f"Enter player { str(i+1) } name: "))


# Word selection
word = getpass.getpass("Enter a word to guess: ").upper()


# Guessing
failed = check_fails()
while not failed and is_winner == False:
    cls()
    
    
    # Printing the board
    player = get_active_player(active_player, count_players)
    print(f"Player: {player}")
    board(word)
    
    
    # Feedback
    is_winner = "_" not in replacement_word("_" * len(word), word)
    if check_fails():
        print("xxxxxxx You lose xxxxxxx")
        print(f"xxxxxxx Word was {word} xxxxxxx")
        break
    elif is_winner:
        print(f"------- Winner is {player}! -------")
        break
    feedback(asking_for_letter(), word)
